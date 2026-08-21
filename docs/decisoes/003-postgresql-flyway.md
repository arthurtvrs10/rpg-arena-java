# ADR-003 — PostgreSQL e Flyway

**Status:** Aceita — 20/08/2026.

## Decisão

PostgreSQL é o único banco de comportamento de produção. Flyway cria e evolui o schema. Testes críticos usam PostgreSQL via Testcontainers.

## Consequências

Não usar `ddl-auto=create/update` fora de spike. Não editar migration aplicada. H2 não valida comportamento de persistência crítico. Constraints e índices fazem parte do requisito.
