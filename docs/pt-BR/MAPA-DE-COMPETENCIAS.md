# Mapa de competências e evidências

Use este arquivo para conferir se o mês gerou prova concreta, não apenas estudo.

| Competência final | Tarefas principais | Evidência mínima | Pergunta de defesa |
|---|---|---|---|
| Backend Java/Spring Boot | 4, 8, 10, 11, 18 | aplicação executável, casos de uso e endpoints | Como a requisição atravessa as camadas? |
| Orientação a objetos e regras | 2, 5, 13, 15, 16 | invariantes, máquinas de estado e testes puros | Que estado impossível seu modelo impede? |
| PostgreSQL, SQL e migrations | 4, 10, 11, 13, 19 | migrations, constraints, EXPLAIN | Que regra está garantida no banco e por quê? |
| Transações | 11, 14, 17, 19 | rollback e efeitos atômicos | Qual é a unidade transacional? |
| API REST | 8–11, 18, 21 | OpenAPI, DTOs, erros e status | Por que escolheu 409 neste caso? |
| Autenticação/autorização | 7–9, 20 | matriz, JWT e testes A/B | Por que JWT não impede BOLA? |
| Isolamento por jogador | 9, 11, 12, 18, 20 | A tenta recurso de B em quatro módulos | Onde a identidade efetiva é obtida? |
| Testes automatizados | 5, 12, 14–17, 22 | unitários, integração, segurança e concorrência | Qual teste protege o maior risco? |
| Bruno | 8–12, 18, 21, 24 | coleção com jornada e falhas | O que Bruno prova além dos unitários? |
| Git/branches/PR/commits | todos, sábados | issues, branches curtas, PRs e reviews | Como o histórico explica a evolução? |
| Docker | 4, 22, 24 | Compose, Dockerfile e health | Como uma pessoa sobe tudo do zero? |
| CI | 22–24 | workflow verde no commit da release | O que impede merge quebrado? |
| Publicação e documentação | 21, 24 | URL, release, README e OpenAPI | Qual limitação conhecida ficou? |
| Decisões técnicas | 3, 7, 17, 19 | ADRs com alternativas e gatilhos | Que evidência faria mudar a decisão? |
| Processos seletivos | 6, 12, 18, 24 | 14 candidaturas e feedback | O que uma entrevista revelou? |

## Portas de qualidade finais

### Porta A — comportamento

- jornada completa;
- erros previsíveis;
- regras terminais;
- ranking.

### Porta B — integridade

- recompensa única;
- ação única;
- rollback;
- conflito concorrente;
- migrations.

### Porta C — segurança

- tokens;
- papéis;
- propriedade;
- mass assignment;
- segredos/logs.

### Porta D — entrega

- clone limpo;
- verify;
- Compose;
- CI;
- deploy/smoke;
- release.

### Porta E — explicação

- pitch de 60 segundos;
- demo de oito minutos;
- quatro ADRs;
- uma limitação honesta;
- próximo passo ligado a evidência.

## Regra de honestidade

Marque competência como demonstrada somente quando existir um link, teste, commit, request, diagrama ou gravação. “Eu estudei” não é evidência de entrega.
