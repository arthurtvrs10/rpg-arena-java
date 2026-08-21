# Plano de homologação

## Objetivo

Comprovar que a versão 1.0 atende jornada, regras, segurança, dados e operação antes da tag pública.

## Ambientes

| Ambiente | Uso | Dados |
|---|---|---|
| unit | domínio e aplicação sem infraestrutura | builders determinísticos |
| integration | PostgreSQL real via Testcontainers | criado por teste/migrations |
| local | API + PostgreSQL por Compose | seed fictício documentado |
| staging | smoke, segurança e carga mínima | contas fictícias |
| production | demonstração pública | somente dados fictícios/controlados |

## Entrada para homologação

- todos os requisitos Must implementados;
- migrations executadas em banco vazio e upgrade do último marco;
- CI e quality gates verdes;
- OpenAPI e Bruno correspondentes ao commit candidato;
- imagem Docker identificada pelo SHA;
- nenhum blocker ou critical aberto;
- riscos residuais registrados.

## Suite funcional ponta a ponta

| ID | Fluxo | Resultado esperado |
|---|---|---|
| HML-01 | registrar, login, refresh e logout | tokens/rotação/revogação corretos |
| HML-02 | criar três personagens e tentar o quarto | três sucessos e um conflito sem resíduo |
| HML-03 | equipar, desequipar e consumir | slots, pilhas e stats consistentes |
| HML-04 | aceitar missão, viajar e gerar encontro | versão, posição e objetivo corretos |
| HML-05 | batalha com ataque, defesa, skill e item | turnos, custos, cooldown e eventos corretos |
| HML-06 | finalizar batalha e reiniciar API | XP, loot, missão e ranking persistem |
| HML-07 | escolher ramificação e resgatar missão | consequências e recompensa únicas |
| HML-08 | comprar, vender e consultar ledger | saldos fecham exatamente |
| HML-09 | admin cria, valida, publica e arquiva | somente versão válida é usada por novas instâncias |
| HML-10 | consultar ranking público | ordem determinística e dados mínimos |

## Suite de falhas e segurança

- token ausente, expirado, adulterado e de conta bloqueada;
- PLAYER em cada rota administrativa;
- jogador A usando personagem, item, missão e batalha de B;
- payload com role, ownerId, dano, XP, preço ou ouro;
- ação fora de turno, habilidade sem mana e item sem quantidade;
- viagem sem conexão e compra fora do local;
- publicação com referência inexistente/ciclo inválido;
- resposta 500 e logs sem dados sensíveis.

## Suite de idempotência e concorrência

1. Repetir a mesma chave e corpo para ação, viagem, compra, venda, resgate e publish.
2. Reutilizar a chave com corpo diferente.
3. Enviar duas ações simultâneas com a mesma versão de batalha.
4. Enviar duas compras simultâneas do último item.
5. Concluir/resgatar a mesma missão simultaneamente.
6. Equipar/vender o mesmo item simultaneamente.
7. Confirmar um efeito, um ledger e um resultado contabilizado.

## Dados e migrations

- criar banco vazio e executar todas as migrations;
- iniciar na migration do marco anterior e atualizar;
- validar constraints de FK, check, unique e índices;
- confirmar rollback de criação de personagem, recompensa, ação e economia;
- verificar `timestamptz`, UUID e nulabilidade;
- executar `EXPLAIN (ANALYZE, BUFFERS)` das consultas de ranking, inventário, missões e batalha.

## Qualidade e desempenho

- unitários de domínio: feliz, erro e limite por regra crítica;
- integração com PostgreSQL sem H2 para comportamento de persistência;
- ArchUnit impedindo dependência proibida;
- JaCoCo: gate definido para domínio/aplicação, sem meta usada como substituto de qualidade;
- carga de referência: 25 usuários concorrentes por 10 minutos;
- alvo: leitura p95 <= 400 ms, comando p95 <= 800 ms e erro inesperado < 1%;
- registrar p50, p95, p99, throughput, erros, gargalo e hardware/ambiente.

## Operação

- clone limpo executado por pessoa/ambiente diferente;
- `docker compose up --build` deixa serviços saudáveis;
- liveness não depende do banco; readiness falha quando banco está indisponível;
- smoke pós-deploy executa health, login fictício e ranking;
- backup é restaurado em ambiente separado;
- rollback volta para imagem anterior e contrato compatível;
- alertas possuem link para runbook.

## Critérios de saída

- 100% dos Must atendidos e rastreados;
- HML-01–10 aprovados;
- matriz SEC-T01–12 aprovada;
- zero duplicidade nos testes concorrentes;
- zero blocker/critical e nenhum high sem mitigação aprovada;
- setup limpo e smoke de produção aprovados;
- README, OpenAPI, Bruno, changelog e release notes revisados;
- tag aponta para o mesmo commit/imagem implantado.

## Evidências a arquivar

`evidencias/v1.0.0/` deve conter: saída do CI, relatório de testes, JaCoCo, Bruno runner, migration, EXPLAIN, carga, revisão OWASP, smoke, backup/restore, imagens do deploy, changelog, versão do OpenAPI e link do episódio final.

## Termo de aceite

A release é aceita quando o checklist acima está assinado no GitHub Release/issue de homologação pelo mantenedor. Exceção exige risco residual, justificativa, impacto, prazo e issue pública, exceto vulnerabilidade que deva permanecer privada.
