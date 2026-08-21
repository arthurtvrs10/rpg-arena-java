# Catálogo de eventos de domínio

Eventos são fatos no passado, imutáveis e com `eventId`, `occurredAt`, `aggregateId`, `aggregateVersion`, `eventType` e payload mínimo. Eles não carregam senha, token, e-mail ou entidade inteira.

| Evento | Produtor | Payload mínimo | Consumidores | Idempotência |
|---|---|---|---|---|
| AccountRegistered | account | accountId, role | audit | eventId+consumer |
| AccountBlocked | account | accountId, actorId, reason | session, audit | eventId+consumer |
| CharacterCreated | character | characterId, accountId, classVersionId | inventory, world, audit | characterId/consumer |
| ExperienceGranted | progression | characterId, amount, sourceType, sourceId | level policy, audit | sourceId+characterId |
| CharacterLeveledUp | progression | characterId, oldLevel, newLevel | skills, ranking | eventId+consumer |
| SkillUnlocked | progression | characterId, skillVersionId | audit | pair unique |
| ItemGranted | inventory | characterId, itemVersionId, quantity, sourceId | quest/audit | sourceId+item |
| ItemConsumed | inventory | characterId, entryId, itemVersionId, quantity | quest/combat | eventId+consumer |
| ItemEquipped | inventory | characterId, entryId, slot | audit | eventId+consumer |
| BattleStarted | combat | battleId, characterId, enemyVersionId | quest/audit | battleId |
| BattleActionExecuted | combat | battleId, turn, actor, actionType | quest/audit | battleId+sequence |
| BattleFinished | combat | battleId, characterId, status, enemyVersionId | result accounting | battleId |
| BattleResultAccounted | combat | battleId, characterId, xp, lootSummary | quest, ranking, audit | battleId+consumer |
| QuestAccepted | quest | instanceId, characterId, questVersionId | audit | instanceId |
| QuestObjectiveAdvanced | quest | instanceId, objectiveCode, current, target, sourceEventId | audit | sourceEventId+objective |
| QuestChoiceMade | quest | instanceId, nodeCode, choiceCode | audit | instanceId+node |
| QuestCompleted | quest | instanceId, characterId | audit | instanceId |
| QuestRewardGranted | quest | instanceId, summary | audit | instanceId |
| CharacterTraveled | world | characterId, originVersionId, destinationVersionId, cost | quest, encounter | travelLogId |
| EncounterGenerated | world | encounterId, characterId, enemyVersionId | combat | encounterId |
| ItemBought | economy | transactionId, characterId, itemVersionId, quantity, total | quest/audit | transactionId |
| ItemSold | economy | transactionId, characterId, itemVersionId, quantity, total | quest/audit | transactionId |
| ContentPublished | content | type, definitionId, versionId, actorId | cache inexistente/audit | versionId |
| ContentArchived | content | type, versionId, actorId | audit | versionId |

## Regras

1. Nome é passado e estável.
2. Evento só é publicado após o agregado aceitar a mudança.
3. Se consumidor participa da mesma transação, falha provoca rollback quando o requisito exige atomicidade.
4. Cada consumidor registra processamento antes/depois na mesma transação do efeito.
5. Evento repetido produz zero efeito adicional.
6. Não usar evento para evitar uma chamada síncrona necessária à decisão atual.
7. Na v1.0 não existe broker externo; publicação é interna.

## Exemplo de envelope

```json
{
  "eventId": "00000000-0000-0000-0000-000000000001",
  "eventType": "BattleFinished",
  "aggregateId": "00000000-0000-0000-0000-000000000002",
  "aggregateVersion": 9,
  "occurredAt": "2026-10-10T18:30:00Z",
  "payload": {
    "characterId": "00000000-0000-0000-0000-000000000003",
    "status": "WON",
    "enemyVersionId": "00000000-0000-0000-0000-000000000004"
  }
}
```
