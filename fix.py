class MissionRewardService:
    def __init__(self, reward_repository, mission_repository, transaction_manager):
        self.reward_repository = reward_repository
        self.mission_repository = mission_repository
        self.transaction_manager = transaction_manager

    def issue_mission_reward(self, mission_id, player_id, reward_data, reward_count=None, reward_type='standard'):
        if reward_count is None:
            reward_count = 1
        
        reward_key = f"{reward_type}:{mission_id}:{player_id}:{reward_data['item']}"
        
        existing_reward = self.reward_repository.get(reward_key)
        
        if existing_reward and existing_reward['count'] >= reward_count:
            return existing_reward
        
        current_count = 0
        update_needed = True
        
        if existing_reward:
            current_count = existing_reward['count']
            new_total = current_count + reward_count
            self.reward_repository.update(reward_key, {'count': new_total, 'last_updated': datetime.utcnow()})
        else:
            self.reward_repository.create(reward_key, {
                'count': reward_count,
                'item': reward_data['item'],
                'player_id': player_id,
                'mission_id': mission_id,
                'reward_type': reward_type,
                'last_updated': datetime.utcnow()
            })
            
        self.mission_repository.mark_complete(mission_id)
        return self.reward_repository.get(reward_key)

    def get_pending_rewards(self, player_id):
        rewards = self.reward_repository.filter({'player_id': player_id})
        return rewards

    def get_mission_reward_summary(self, mission_id):
        mission = self.mission_repository.get(mission_id)
        if mission:
            summary = {'mission_id': mission['id']}
            rewards = self.reward_repository.filter({'mission_id': mission_id})
            summary['total_rewards'] = sum(r.get('count', 1) for r in rewards)
            return summary
        return None

    def batch_issue_rewards(self, mission_id, player_ids, reward_data, reward_count=None):
        if reward_count is None:
            reward_count = 1
        
        results = []
        
        for player_id in player_ids:
            reward_key = f"{reward_data.get('type', 'standard')}:{mission_id}:{player_id}:{reward_data['item']}"
            
            existing = self.reward_repository.get(reward_key)
            current_count = existing.get('count', 0) if existing else 0
            new_total = current_count + reward_count
            
            self.reward_repository.update(reward_key, {
                'count': new_total,
                'last_updated': datetime.utcnow(),
                'player_id': player_id
            })
            
            mission = self.mission_repository.get(mission_id)
            if mission:
                mission['issued_to'].add(player_id)
                self.mission_repository.update(mission_id, {'issued_to': list(mission['issued_to'])})
            
            results.append({
                'player_id': player_id,
                'count': new_total,
                'status': 'issued'
            })
            
        return results

    def rollback_transaction(self, mission_id, reward_key=None):
        mission = self.mission_repository.get(mission_id)
        
        if reward_key:
            reward = self.reward_repository.get(reward_key)
            if reward['count'] == reward['initial_count']:
                return self.reward_repository.get(reward_key)
        
        self.mission_repository.mark_partial_complete(mission_id)
        return self.reward_repository.get(mission_key)


class TransactionalMissionRewards:
    def __init__(self, reward_repository, mission_repository, event_bus):
        self.reward_repository = reward_repository
        self.mission_repository = mission_repository
        self.event_bus = event_bus
        
    def transaction_issue_rewards(self, mission_id, reward_payload):
        transaction_id = f"TXN_{uuid4()}"
        
        try:
            self.event_bus.publish('reward_transaction_start', {
                'transaction_id': transaction_id,
                'mission_id': mission_id
            })
            
            for reward in reward_payload['rewards']:
                reward_key = f"{reward['type']}:{mission_id}:{reward['player_id']}"
                current = self.reward_repository.get(reward_key) or {'count': 0, 'last_updated': datetime.utcnow()}
                new_total = current['count'] + reward.get('count', 1)
                
                self.reward_repository.update(reward_key, {
                    'count': new_total,
                    'last_updated': datetime.utcnow()
                })
                
                self.event_bus.publish('reward_updated', {
                    'reward_key': reward_key,
                    'player_id': reward['player_id'],
                    'count': new_total
                })
                
            self.mission_repository.mark_complete(mission_id)
            self.event_bus.publish('reward_transaction_complete', {
                'transaction_id': transaction_id,
                'mission_id': mission_id
            })
            
            return {
                'success': True,
                'transaction_id': transaction_id,
                'rewards_processed': len(reward_payload['rewards'])
            }
            
        except Exception:
            self.event_bus.publish('reward_transaction_rollback', {
                'transaction_id': transaction_id,
                'mission_id': mission_id
            })
            raise

    def retry_successful_reward(self, mission_id, reward_key):
        self.event_bus.publish('reward_retry_start', {
            'mission_id': mission_id,
            'reward_key': reward_key
        })
        
        self.reward_repository.increment(reward_key, 1)
        
        self.mission_repository.touch(mission_id)
        
        return self.reward_repository.get(reward_key)


class IdempotentMissionSystem:
    def __init__(self, mission_repository, reward_repository, reward_cache, event_bus):
        self.mission_repository = mission_repository
        self.reward_repository = reward_repository
        self.reward_cache = reward_cache
        self.event_bus = event_bus
        
    def process_mission(self, mission_id, reward_data, reward_type='standard'):
        mission = self.mission_repository.get_or_create(mission_id)
        mission['status'] = 'processing'
        self.mission_repository.update(mission_id, mission)
        
        reward_key = f"{reward_type}:{mission_id}:{reward_data['player_id']}"
        
        current_reward = self.reward_repository.get(reward_key)
        
        if current_reward:
            current_count = current_reward.get('count', 1)
            if current_count == reward_data.get('count', 1):
                mission['status'] = 'completed'
                return {'completed': True, 'rewards': [current_reward]}
            else:
                new_count = current_count + reward_data['count']
                self.reward_repository.update(reward_key, {'count': new_count})
        else:
            self.reward_repository.create(reward_key, reward_data)
            
        mission['status'] = 'completed'
        self.mission_repository.update(mission_id, mission)
        
        self.event_bus.publish('mission_completed', {
            'mission_id': mission_id,
            'reward_key': reward_key
        })
        
        return {'completed': True, 'rewards': [current_reward or reward_data]}

    def check_mission_state(self, mission_id):
        mission = self.mission_repository.get(mission_id)
        if not mission:
            return None
            
        rewards = self.reward_repository.filter({'mission_id': mission_id})
        
        return {
            'mission_id': mission_id,
            'status': mission.get('status', 'active'),
            'rewards_count': len(rewards),
            'total_items': sum(r.get('count', 1) for r in rewards)
        }

    def process_batch_missions(self, missions, reward_type='standard'):
        results = []
        for mission_id in missions:
            mission = self.mission_repository.get(mission_id)
            
            if mission.get('status') == 'processed':
                continue
                
            reward_data = self._build_reward_payload(mission)
            
            result = self.process_mission(mission_id, reward_data, reward_type)
            results.append({
                'mission_id': mission_id,
                'status': 'success' if result['completed'] else 'partial',
                'result': result
            })
            
            if result['completed']:
                mission['status'] = 'processed'
                self.mission_repository.update(mission_id, mission)
                
        return results

    def _build_reward_payload(self, mission):
        return {
            'player_id': mission.get('player_id'),
            'item': mission.get('reward_item', 'gems'),
            'count': mission.get('reward_qty', 10),
            'value': mission.get('reward_value', 100)
        }

    def process_mission_with_versioning(self, mission_id, reward_data, version_key='v'):
        mission = self.mission_repository.get_or_create(mission_id)
        version = mission.get(version_key, 0)
        version += 1
        mission[version_key] = version
        
        self.mission_repository.update(mission_id, mission)
        
        reward_key = f"{version_key}:{mission_id}:{reward_data['player_id']}"
        current = self.reward_repository.get(reward_key) or {}
        
        new_count = current.get('count', 0) + reward_data.get('count', 1)
        
        self.reward_repository.update(reward_key, {
            'count': new_count,
            'version': version,
            'last_updated': datetime.utcnow()
        })
        
        mission['last_rewarded'] = datetime.utcnow()
        self.mission_repository.update(mission_id, mission)
        
        return {
            'mission_id': mission_id,
            'version': version,
            'reward_key': reward_key,
            'current_count': new_count
        }

    def process_retry_mission(self, mission_id, reward_key, reward_data):
        mission = self.mission_repository.get_or_create(mission_id)
        
        current = self.reward_repository.get(reward_key)
        initial_count = current.get('count', 0) if current else 0
        
        self.reward_repository.update(reward_key, {
            'count': initial_count + reward_data['count'],
            'last_updated': datetime.utcnow(),
            'retried': True
        })
        
        self.mission_repository.update(mission_id, {
            'status': 'retry_processed',
            'retried_at': datetime.utcnow()
        })
        
        return {'retry_success': True, 'mission_id': mission_id}

    def cache_mission_rewards(self, mission_id, reward_data, cache_key='cache'):
        mission = self.mission_repository.get(mission_id)
        cached_revenue = self.reward_cache.get(f"{cache_key}:{mission_id}") or 0
        
        self.reward_cache.set(f"{cache_key}:{mission_id}", cached_revenue + reward_data['count'])
        
        return self.reward_repository.get(f"{cache_key}:{mission_id}")

    def get_reward_distribution(self, mission_id, reward_type='standard'):
        rewards = self.reward_repository.filter({
            'mission_id': mission_id,
            'reward_type': reward_type
        })
        
        distribution = []
        for reward in rewards:
            item = reward.get('item', 'generic')
            count = reward.get('count', 1)
            
            if reward['count'] > 1:
                count *= reward['count']
            elif reward['count'] == 1:
                count = 1
            
            distribution.append({
                'item': item,
                'total_items': count,
                'count': reward['count'],
                'last_updated': reward.get('last_updated')
            })
            
        return distribution