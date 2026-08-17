# Modelo de dados, migrations e transações

## Modelo lógico

~~~mermaid
erDiagram
    ACCOUNT ||--|| PLAYER_PROFILE : owns
    ACCOUNT ||--o{ CHARACTER : owns
    CHARACTER ||--o{ INVENTORY_ITEM : contains
    ITEM_CATALOG ||--o{ INVENTORY_ITEM : describes
    CHARACTER ||--o{ MISSION_ATTEMPT : performs
    MISSION ||--o{ MISSION_ATTEMPT : defines
    CHARACTER ||--o{ BATTLE : participates
    BATTLE ||--o{ BATTLE_ACTION : records
    CHARACTER ||--|| RANKING_ENTRY : projects
~~~

## Tabelas essenciais

### accounts

| Coluna | Tipo lógico | Restrição |
|---|---|---|
| id | UUID | PK |
| email | varchar | not null, índice único por valor normalizado |
| password_hash | varchar | not null |
| role | varchar | not null |
| status | varchar | not null |
| created_at | timestamp with time zone | not null |

### characters

| Coluna | Tipo lógico | Restrição |
|---|---|---|
| id | UUID | PK |
| account_id | UUID | FK, not null |
| name | varchar | not null, unique lower(name) |
| class_code | varchar | not null |
| level | integer | check level >= 1 |
| experience | bigint | check experience >= 0 |
| base_health | integer | check > 0 |
| base_attack | integer | check > 0 |
| base_defense | integer | check >= 0 |
| created_at | timestamptz | not null |
| version | bigint | not null |

Regra “máximo três personagens” exige verificação transacional na aplicação. Se o projeto decidir garantir sob alta concorrência, documentar uma estratégia adicional; apenas contar e inserir pode sofrer corrida.

### item_catalog

Código, nome, tipo, slot compatível, bônus, raridade e active. Catálogo é separado da posse.

### inventory_items

Identifica uma instância do item, personagem proprietário, item de catálogo, estado OWNED/EQUIPPED/CONSUMED, slot atual e versão.

Restrições:

- índice por character_id;
- unicidade parcial de slot equipado por personagem, se implementada com índice adequado;
- FK para catálogo;
- estado e slot coerentes.

### missions e mission_attempts

Mission define requisitos e recompensa. MissionAttempt captura o que ocorreu para um personagem.

Campos críticos da tentativa:

- status;
- started_at e finished_at;
- reward_granted_at;
- reward_key única;
- version.

### battles

Campos:

- character_id;
- enemy_code ou snapshot do inimigo;
- status;
- current_turn;
- player_health, enemy_health;
- player_mana;
- winner;
- result_accounted_at;
- version;
- created_at e finished_at.

### battle_actions

- battle_id;
- request_id;
- turn_number;
- actor;
- action_type;
- skill_code;
- damage;
- occurred_at.

Restrição única: battle_id + request_id. Essa restrição é a última barreira contra repetição concorrente; a aplicação ainda deve devolver comportamento idempotente.

### ranking_entries

Projeção de leitura por personagem: wins, losses, level_snapshot, score e updated_at. A origem de verdade continua sendo o resultado contabilizado.

## Sequência sugerida de migrations

| Arquivo | Conteúdo |
|---|---|
| V1__create_accounts.sql | Conta, status e unicidade de e-mail |
| V2__create_characters.sql | Personagem, FK, checks e versão |
| V3__create_items_and_inventory.sql | Catálogo, posse, índices e slots |
| V4__create_missions.sql | Missões e tentativas |
| V5__create_battles.sql | Batalha e ações |
| V6__create_rankings.sql | Projeção e índices |
| V7__add_security_and_query_indexes.sql | Índices observados após consultas |

Não edite migration já aplicada em ambiente compartilhado. Crie uma nova.

## Limites transacionais

| Caso de uso | Alterações atômicas |
|---|---|
| Criar personagem | verificar limite, criar personagem e itens iniciais |
| Equipar | validar posse/slot, desequipar anterior, equipar novo, atualizar versão |
| Concluir missão | validar estado, marcar concluída, aplicar XP/item, marcar recompensa |
| Ação de batalha | registrar idempotência, aplicar dano/custo, avançar turno, finalizar |
| Contabilizar resultado | marcar resultado e atualizar ranking uma vez |

## Isolamento e concorrência

PostgreSQL usa Read Committed como nível padrão. Isso não torna uma sequência “ler, decidir, gravar” automaticamente segura contra concorrência. Para batalha, use coluna version e optimistic locking. Para unicidade/idempotência, use restrição no banco e tratamento da violação. Para operações que exigirem lock explícito, documente ordem de aquisição para reduzir deadlocks.

## Índices orientados por consulta

Criar apenas após listar consultas:

- accounts por lower(email);
- characters por account_id;
- inventory_items por character_id e estado;
- mission_attempts por character_id, mission_id e status;
- battle_actions por battle_id e turn_number;
- rankings pela ordenação pública.

Valide com EXPLAIN (ANALYZE, BUFFERS) em dados de teste suficientes. Um índice que nunca serve a consulta aumenta custo de escrita.

## Dados de teste

- migrations criam estrutura, não dados de produção secretos;
- seed local pode usar migration específica de ambiente ou bootstrap controlado;
- testes criam seus próprios dados;
- UUIDs e relógio previsíveis facilitam asserções;
- limpeza não pode mascarar falta de isolamento entre testes.

## Checklist de revisão de banco

- [ ] FK e nulabilidade refletem a regra;
- [ ] valores monetários não existem no MVP;
- [ ] enum persistido tem estratégia de evolução;
- [ ] timestamps usam fuso adequado;
- [ ] migrations funcionam em banco vazio;
- [ ] rollback da aplicação não deixa recompensa parcial;
- [ ] repetição encontra restrição de idempotência;
- [ ] consulta paginada tem ordenação determinística;
- [ ] logs não expõem hash ou token.
