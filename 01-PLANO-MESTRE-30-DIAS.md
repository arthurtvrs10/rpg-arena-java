# Plano mestre de 30 dias

## Objetivo do produto

Entregar uma API de RPG de turnos em que uma pessoa cria conta e personagens, equipa itens, inicia missões, disputa batalhas por turnos e aparece em um ranking. O sistema deve impedir acesso aos recursos de outro jogador, processar recompensas uma única vez e suportar tentativas concorrentes de ação sem corromper a partida.

## Estratégia de entrega

O mês é dividido em quatro sprints de uma semana. Cada sprint produz uma fatia demonstrável. O quadro usa Scrum para objetivos, review e retrospectiva; Kanban para limitar trabalho em andamento a uma tarefa.

| Sprint | Período | Objetivo | Incremento demonstrável | Porta de qualidade |
|---|---|---|---|---|
| 1 | 17 a 22/08 | Definir e iniciar o núcleo do produto | Repositório executável, banco versionado e progressão de personagem testada | Build verde, primeira migration, regras puras com testes |
| 2 | 24 a 29/08 | Proteger identidade e recursos do jogador | Cadastro, login, personagem e inventário isolados por proprietário | Matriz de autorização, testes de acesso cruzado e Bruno |
| 3 | 31/08 a 05/09 | Implementar missão e combate consistentes | Missão com recompensa única e batalha por turnos concorrente | Transações, idempotência, optimistic locking e testes reais |
| 4 | 07 a 12/09 | Tornar o projeto entregável | Ranking, segurança endurecida, documentação, CI, Docker e release | Pipeline verde, smoke test, README e demo |

O dia 13/09 é reservado a descanso e auditoria leve da entrega.

## Visão diária

### Sprint 1 — Produto, domínio e base executável

| Dia | Data | Tarefa | Saída concreta |
|---:|---|---|---|
| 1 | 17/08 | Visão, escopo e backlog | Product Goal, MVP, fora de escopo e backlog ordenado |
| 2 | 18/08 | Linguagem do domínio e invariantes | Glossário, agregados, estados e regras numeradas |
| 3 | 19/08 | Arquitetura modular e ADRs | Pacotes por funcionalidade e três decisões registradas |
| 4 | 20/08 | Base técnica e banco | Aplicação, PostgreSQL, Flyway, healthcheck e build |
| 5 | 21/08 | Progressão de personagem | Regra de XP/nível em Java puro e testes |
| 6 | 22/08 | Review e retrospectiva | PR revisado, demo, retro, vídeo e duas candidaturas |

### Sprint 2 — Segurança, personagem e inventário

| Dia | Data | Tarefa | Saída concreta |
|---:|---|---|---|
| 7 | 24/08 | Modelo de ameaça e autenticação | Fluxo de identidade, papéis e ameaças priorizadas |
| 8 | 25/08 | Cadastro, login e JWT | Tokens válidos, senhas protegidas e erros seguros |
| 9 | 26/08 | Propriedade e isolamento | Política de acesso e testes de jogador A contra B |
| 10 | 27/08 | Criação de personagem | Classes, atributos, limite e contrato REST |
| 11 | 28/08 | Inventário e equipamento | Equipar/desequipar transacional com invariantes |
| 12 | 29/08 | Integração da sprint | Testes, Bruno, PR, demo, retro e três candidaturas |

### Sprint 3 — Missões, combate e concorrência

| Dia | Data | Tarefa | Saída concreta |
|---:|---|---|---|
| 13 | 31/08 | Máquina de estados de missão | Transições válidas e inválidas testadas |
| 14 | 01/09 | Recompensa idempotente | XP e item aplicados exatamente uma vez |
| 15 | 02/09 | Motor de combate puro | Dano determinístico e testes de regras |
| 16 | 03/09 | Turnos, habilidades e recursos | Comandos de ação e encerramento de batalha |
| 17 | 04/09 | Concorrência e repetição | Versão otimista e chave de idempotência |
| 18 | 05/09 | API de batalha | Cenários completos no Bruno, PR, demo e quatro candidaturas |

### Sprint 4 — Qualidade de produção e portfólio

| Dia | Data | Tarefa | Saída concreta |
|---:|---|---|---|
| 19 | 07/09 | Ranking e consultas | Projeção paginada, índices e plano de consulta |
| 20 | 08/09 | Segurança ofensiva | BOLA, enumeração, abuso e respostas seguras |
| 21 | 09/09 | Contrato, erros e observabilidade | OpenAPI, problem details, logs e healthcheck |
| 22 | 10/09 | Testcontainers, Docker e CI | Banco real nos testes e pipeline automatizado |
| 23 | 11/09 | Desempenho e release candidate | EXPLAIN, N+1, smoke test e tag candidata |
| 24 | 12/09 | Release e apresentação | Deploy, README final, vídeo, retro e cinco candidaturas |

## Definition of Ready

Uma tarefa pode entrar em andamento somente quando:

- o problema e o usuário afetado estão claros;
- existe resultado observável;
- regras e casos de erro foram listados;
- dependências estão disponíveis;
- a tarefa cabe em um dia ou foi fatiada;
- critérios de aceite podem ser testados;
- não depende de “pesquisar tudo sobre o assunto”.

## Definition of Done

Uma tarefa está concluída somente quando:

- regra implementada sem duplicação óbvia;
- teste adequado ao risco está verde;
- cenário feliz e pelo menos dois cenários de falha foram verificados;
- segurança por proprietário foi checada quando aplicável;
- migration é aditiva e reproduzível quando há banco;
- coleção Bruno ou contrato OpenAPI foi atualizado quando há endpoint;
- nenhum segredo foi versionado;
- commit explica a intenção;
- documentação e diário registram decisões;
- você consegue explicar a solução em até três minutos.

## Limites de escopo

Não adicionar durante o mês: microsserviços, Kafka, Kubernetes, frontend gráfico, WebSocket, PvP em tempo real, Redis, pagamentos ou geração de conteúdo por IA. Esses itens só entram após o MVP e apenas mediante uma necessidade medida.

## Placar semanal

Use esta fórmula apenas como diagnóstico, não como competição:

- 1 ponto por tarefa concluída pela Definition of Done;
- 1 ponto por dia com teste verde;
- 1 ponto por PR realmente revisado;
- 1 ponto por demo;
- 1 ponto por retrospectiva com ação concreta;
- 1 ponto por candidatura personalizada.

Meta mínima: concluir o incremento de cada sprint. Se o placar cair, reduza escopo antes de aumentar horas.
