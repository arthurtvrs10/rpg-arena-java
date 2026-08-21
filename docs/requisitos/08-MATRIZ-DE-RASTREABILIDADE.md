# Matriz de rastreabilidade

Esta matriz liga todos os requisitos por intervalo. Dentro de cada intervalo, cada requisito deve aparecer pelo código completo no nome/descrição do teste ou na anotação da issue.

## Funcionais

| Requisitos | Casos de uso | Histórias | Regras | Módulo | Semanas | Evidência mínima |
|---|---|---|---|---|---|---|
| RF-AUT-001–003,009–010 | UC-01, UC-02 | US-AUT-01 | RN-AUT-001–007 | account | 11–12 | unitário de normalização/senha + integração register/login + Bruno |
| RF-AUT-004–006 | UC-03 | US-AUT-02 | RN-AUT-007–010 | account | 11 | integração de rotação/reuso/logout |
| RF-AUT-007 | UC-02/05 | US-AUT-01 | RN-AUT-011–012 | account | 11–12 | teste perfil próprio e BOLA |
| RF-AUT-008 | UC-19 | US-SEC-01 | RN-AUT-005, RN-ADM-007 | account | 16/20 | RBAC, revogação e auditoria |
| RF-CHR-001–005 | UC-04 | US-CHR-01 | RN-CHR-001–006 | character | 3,5,10 | domínio + transação + endpoint |
| RF-CHR-003–004 | UC-05 | US-SEC-01 | RN-CHR-009–011 | character | 10–12 | owner A/B + arquivamento |
| RF-CHR-006,009 | UC-04/06/12 | US-INV-01, US-CBT-02 | RN-CHR-007–012 | character | 3–7 | testes de limites e stats derivados |
| RF-CHR-007–008,012 | UC-13 | US-CHR-02 | RN-PRG-001–006 | progression | 7–8 | tabela de XP, múltiplos níveis, cap |
| RF-CHR-010–011 | UC-12 | US-CBT-02 | RN-PRG-007–008 | progression | 7,12 | desbloqueio e elegibilidade |
| RF-INV-001–006,009 | UC-06 | US-INV-01 | RN-INV-001–007,011 | inventory | 6,10 | repository + transação + concorrência |
| RF-INV-007 | UC-07/12 | US-INV-02 | RN-INV-007–009 | inventory | 14 | consumo fora/dentro do combate |
| RF-INV-008,010 | UC-13/15/16 | US-INV-02 | RN-INV-010–011 | inventory | 6,14 | loot reproduzível e corrida |
| RF-CBT-001–003,017 | UC-11 | US-CBT-01 | RN-CBT-001–003 | combat | 4,12 | batalha inicial, snapshot e exclusividade |
| RF-CBT-004–009,011–012 | UC-12 | US-CBT-02 | RN-CBT-004–016, RN-EFF-* | combat | 4,7,12 | suite de ações/estados/efeitos |
| RF-CBT-010,016 | UC-12 | US-CBT-02 | RN-CBT-016 | combat | 4,12 | ordem e imutabilidade de eventos |
| RF-CBT-013 | UC-13 | US-QST-03 | RN-CBT-020 | combat/progression | 8,12 | contabilização única transacional |
| RF-CBT-014–015 | UC-12 | US-CBT-03 | RN-CBT-017–019 | combat | 10,12 | repetição e duas threads/requests |
| RF-QST-001–004,009–010,012 | UC-08/13/14 | US-QST-01/03 | RN-QST-001–007,012 | quest | 8,12 | máquina de estados e recompensa |
| RF-QST-005–008,011 | UC-09 | US-QST-02 | RN-QST-008–013 | quest/content | 15 | árvore, escolha, abandono e versionamento |
| RF-WLD-001–007 | UC-10 | US-WLD-01 | RN-WLD-001–006 | world | 13 | grafo, viagem, custo e encontro |
| RF-ECO-001–009 | UC-15/16 | US-ECO-01/02 | RN-ECO-001–009 | economy | 14 | compra/venda + rollback + corrida |
| RF-ECO-010 | UC-18 | US-ADM-01 | RN-ECO-010 | economy/content | 16 | ajuste auditado |
| RF-ADM-001–008 | UC-18 | US-ADM-01 | RN-ADM-001–008 | content | 15–16 | validação, publish, imutabilidade, RBAC |
| RF-RNK-001–004 | UC-17 | US-RNK-01 | RN-RNK-001–005 | ranking | 19–20 | ordenação, página e dados públicos |
| RF-OPS-001–006 | UC-17/18/19 | US-OPS-01 | políticas operacionais | shared/ops | 18–21 | OpenAPI, Bruno runner, health, log e métrica |

## Não funcionais

| Requisitos | Semanas | Mecanismo | Evidência |
|---|---|---|---|
| RNF-SEC-001–005 | 11–12,20,23 | Spring Security, allowlist, scanner, matriz | suíte de segurança e relatório OWASP |
| RNF-DAT-001–004 | 5–8,14 | Flyway, constraints, transações, UTC/UUID | migrate vazio/upgrade e testes PostgreSQL |
| RNF-CON-001 | 6,10,12,14 | `@Version`, unique index e retry controlado | cenários concorrentes |
| RNF-API-001–003 | 9–12,19 | OpenAPI, DTOs, Problem Details | diff contrato/implementação e Bruno |
| RNF-PER-001–002 | 19–20,23 | teste de carga, EXPLAIN, logs SQL | relatório p50/p95/p99 e plano antes/depois |
| RNF-REL-001–002 | 8,10,14,21 | idempotência, backup, rollback, smoke | repetição, ensaio e runbook |
| RNF-TST-001–003 | 3–23 | Clock/RandomSource, JUnit, Testcontainers | suíte e mapa risco→teste |
| RNF-ARC-001–002 | 2–20 | monólito modular, portas e ArchUnit | diagrama, ADR e teste arquitetural |
| RNF-OBS-001–002 | 20 | logs JSON, traceId e Micrometer | consulta de trace e métricas sem IDs |
| RNF-OPS-001–002 | 2,18–23 | Docker Compose e GitHub Actions | clone limpo e pipeline verde |
| RNF-DOC-001 | 1–24 | revisão por release | README/OpenAPI/Bruno/ADRs versionados |
| RNF-PRI-001 | 9–23 | minimização e DTO público | testes de contrato e revisão de dados |

## Matriz requisito → release

| Release | Requisitos concluídos |
|---|---|
| v0.1.0 | modelo puro de RF-CHR-001/006 e RF-CBT-003–005/011–012 |
| v0.2.0 | persistência e RF-CHR-005/007–010, RF-INV-002–009, RF-CBT-002/006/010/013/017, RF-QST-003–004/009–010 |
| v0.3.0 | RF-AUT-001–007/009–010, HTTP de personagem/inventário/combate/missão, RF-CBT-014–016, RF-RNK-001–002/004 |
| v0.4.0 | mundo, economia, narrativa, administração e itens/efeitos restantes |
| v1.0.0-rc.1 | todos RNF Must, documentação executável e performance medida |
| v1.0.0 | deploy, governança, homologação e riscos residuais publicados |

## Política de cobertura

Uma linha da matriz só pode ser marcada “Atendida” quando há link para implementação, teste e evidência. “Código criado” sem teste/contrato não atende requisito. “Documento criado” sem comportamento executável não atende requisito funcional.
