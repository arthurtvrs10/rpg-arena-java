# Dia 23 — Performance, N+1 e release candidate

**Data:** 11/09/2026  
**Sprint:** 4  
**Tempo núcleo:** 2h30  
**Extensão:** 60 min  
**Resultado:** gargalos básicos medidos, defeitos bloqueadores fechados e candidato de release produzido.

## Antes de começar

- [ ] Não adicione funcionalidade.
- [ ] Gere dados de teste realistas.
- [ ] Crie branch fix/RC-01-stabilization.
- [ ] Defina orçamento de tempo; não “otimize tudo”.

## O que você precisa compreender

- Medição vem antes da otimização.
- N+1 é padrão de consultas repetidas por associação.
- Fetch eager não é correção universal.
- Índice melhora certas leituras e custa escrita/espaço.
- Release candidate congela escopo para estabilizar.
- Smoke test verifica sobrevivência do fluxo crítico.

## Fontes oficiais

- PostgreSQL EXPLAIN: https://www.postgresql.org/docs/current/using-explain.html
- PostgreSQL indexes: https://www.postgresql.org/docs/current/indexes.html
- Hibernate fetching: https://docs.jboss.org/hibernate/orm/current/userguide/html_single/Hibernate_User_Guide.html#fetching
- Spring Boot production-ready: https://docs.spring.io/spring-boot/reference/actuator/

## Exemplo neutro — pedidos

Listar 20 pedidos e carregar cliente individualmente gera 21 consultas. Correção pode ser projeção/fetch join específico, não tornar toda relação eager. Compare quantidade e plano.

## Tarefa prática

### 1. Cenários medidos, 20 min

Escolha:

- listar personagens;
- inventário;
- ranking;
- consultar batalha.

Registre dataset, número de chamadas, tempo e consultas. Não use apenas um registro.

### 2. Auditoria N+1, 25 min

Observe SQL em ambiente controlado. Conte queries para página de 20. Se houver N+1:

- identifique associação;
- escolha projeção, entity graph ou fetch join específico;
- teste paginação;
- compare.

### 3. EXPLAIN, 25 min

Analise ranking e uma busca por owner. Registre plano e índices usados. Remova apenas índice claramente redundante mediante justificativa; não faça mudança arriscada no fim.

### 4. Smoke test, 30 min

Do zero:

- build;
- migrations;
- health;
- cadastro/login;
- personagem/equipamento;
- missão/recompensa/retry;
- batalha/retry;
- ranking;
- ataque BOLA.

### 5. Triagem de defeitos, 25 min

Classifique:

- P0: segurança/perda de dados/execução — bloqueia;
- P1: fluxo Must — bloqueia;
- P2: qualidade contornável — documenta/corrige se couber;
- P3: melhoria — roadmap.

Corrija P0/P1. Não esconda P2.

### 6. Release candidate, 15 min

- changelog;
- versão;
- tag 1.0.0-rc.1;
- imagem;
- CI;
- backup/rollback de migration documentado;
- checklist de deploy.

## Critérios de aceite

- [ ] medição tem dataset;
- [ ] N+1 foi verificado;
- [ ] índices ligam a consulta;
- [ ] smoke test passa;
- [ ] zero P0/P1 aberto;
- [ ] riscos P2 documentados;
- [ ] RC tem tag/changelog;
- [ ] CI verde.

## Testes obrigatórios

- query count em listagem;
- EXPLAIN do ranking;
- verify;
- compose do zero;
- Bruno smoke;
- BOLA;
- idempotência;
- concorrência.

## Evidências

- relatório curto de medição;
- planos;
- issue/triagem;
- tag RC;
- commit: perf(query): remove measured n-plus-one in read paths.

## Perguntas de recuperação

1. Como detectar N+1?
2. Por que eager não resolve tudo?
3. Qual custo de índice?
4. O que bloqueia release?
5. O que smoke test não substitui?

## Erros comuns

- otimizar sem medir;
- benchmark no primeiro request apenas;
- eager em tudo;
- índice em toda FK/coluna sem análise;
- feature nova na RC;
- fechar bug só porque não reproduziu uma vez.

## Extensão opcional

Faça um teste de carga pequeno do endpoint de ranking, com limites e sem atacar serviço público. Registre apenas como baseline.

## Conteúdo

“Como encontrei N+1 e validei a correção”.

## Correção e conferência — só depois da tentativa

Uma correção válida reduz consultas/tempo no mesmo cenário sem quebrar paginação/resultado. Seq scan em tabela pequena não é automaticamente defeito. Se não houver N+1 medido, registre “não observado” e não invente refatoração.
