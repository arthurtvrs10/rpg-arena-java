# Mapa de status da implementação

Atualize este arquivo somente em PR de release ou ao concluir uma fatia verificável.

Legenda: `PLANNED`, `IN_PROGRESS`, `IMPLEMENTED`, `VERIFIED`, `RELEASED`.

| Área | Estado atual | Evidência exigida para VERIFIED | Release |
|---|---|---|---|
| Fundação Spring Boot | IMPLEMENTED | `./mvnw test` e CI | v0.1 |
| Arquitetura modular | PLANNED | ArchUnit + diagrama correspondente | v0.1 |
| Personagem em domínio | PLANNED | testes RN-CHR | v0.1 |
| Combate em domínio | PLANNED | batalha determinística completa | v0.1 |
| PostgreSQL/Flyway | PLANNED | migrate vazio/upgrade | v0.2 |
| Inventário/equipamento | PLANNED | transação + concorrência | v0.2 |
| Progressão/habilidades | PLANNED | múltiplos níveis e cap | v0.2 |
| Missão/recompensa | PLANNED | estados + idempotência | v0.2 |
| REST/Problem Details | PLANNED | OpenAPI + testes HTTP | v0.3 |
| Conta/JWT/refresh | PLANNED | auth/rotação/reuso | v0.3 |
| Ownership/RBAC | PLANNED | SEC-T01–12 | v0.3 |
| Bruno jornada | PLANNED | runner verde | v0.3 |
| Mundo/viagem | PLANNED | grafo + viagem + encontro | v0.4 |
| Economia | PLANNED | compra/venda concorrente | v0.4 |
| Narrativa | PLANNED | dois finais reproduzidos | v0.4 |
| Conteúdo administrativo | PLANNED | draft→publish→gameplay | v0.4 |
| Docker/Compose | PLANNED | clone limpo | rc.1 |
| Observabilidade | PLANNED | trace + métricas | rc.1 |
| Performance/segurança | PLANNED | relatórios e gates | rc.1 |
| Deploy/rollback | PLANNED | HTTPS + smoke + ensaio | v1.0 |

Nenhum item `PLANNED` deve ser anunciado no README, vídeo ou currículo como implementado.
