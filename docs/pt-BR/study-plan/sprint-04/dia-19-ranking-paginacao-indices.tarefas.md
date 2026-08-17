# Dia 19 — Ranking, paginação e índices

**Data:** 07/09/2026  
**Sprint:** 4 — Qualidade de produção e portfólio  
**Tempo núcleo:** 2h  
**Extensão:** 60 min  
**Resultado:** ranking público, determinístico, paginado e apoiado por consulta analisável.

## Sprint Goal

Transformar o incremento em uma release reproduzível, segura, observável, documentada, testada e publicada.

## Antes de começar

- [ ] Faça revisão 1–3–7 da Sprint 3.
- [ ] Confirme como resultado é contabilizado uma vez.
- [ ] Crie branch feat/RA-01-ranking.
- [ ] Gere volume de teste suficiente para observar consulta.

## O que você precisa compreender

- Ranking é leitura; pode ser projeção.
- Resultado contabilizado exige idempotência.
- Paginação sem ordenação total pode repetir/pular registros.
- Índice nasce da consulta, não do nome da coluna.
- EXPLAIN mostra plano; ANALYZE executa.
- Resposta pública minimiza dados.

## Fontes oficiais

- PostgreSQL indexes: https://www.postgresql.org/docs/current/indexes.html
- Multicolumn indexes: https://www.postgresql.org/docs/current/indexes-multicolumn.html
- EXPLAIN: https://www.postgresql.org/docs/current/using-explain.html
- Spring Data paging: https://docs.spring.io/spring-data/jpa/reference/repositories/query-methods-details.html#repositories.special-parameters

## Exemplo neutro — placar de vendedores

Ordenar apenas por vendas permite empate instável. Adicionar data/id fixa ordem. A projeção atualiza uma vez por pedido confirmado. Resposta pública não inclui salário ou e-mail.

## Tarefa prática

### 1. Contrato, 15 min

Defina campos públicos:

- position;
- characterName;
- classCode;
- level;
- wins;
- losses;
- score.

Defina page, size máximo e ordem: wins desc, losses asc, level desc, id asc.

### 2. Origem e projeção, 20 min

Escolha:

- consulta agregada de battles; ou
- ranking_entries atualizado no resultado.

Use projeção se MI/BA idempotência está sólida. Registre como reconstruir.

### 3. Atualização, 25 min

Ao finalizar/contabilizar batalha:

- confirmar FINISHED;
- verificar result_accounted_at;
- atualizar wins/losses;
- marcar contabilizado na mesma transação;
- impedir repetição.

### 4. Consulta/paginação, 25 min

Implemente página e filtro opcional de classe. Rejeite size acima do máximo ou normalize conforme contrato. Não aceite propriedade arbitrária de sort.

### 5. Índice e EXPLAIN, 25 min

Com dados de teste:

1. execute query;
2. capture EXPLAIN;
3. proponha índice alinhado à ordem/filtro;
4. aplique migration;
5. execute novamente;
6. compare plano, linhas e buffers.

Não prometa velocidade só porque índice existe.

### 6. Testes/Bruno, 10 min

Teste empate, página vazia, máximo, filtro e ausência de dados privados.

## Critérios de aceite

- [ ] resultado é contabilizado uma vez;
- [ ] ordenação total é determinística;
- [ ] tamanho tem máximo;
- [ ] campos privados não aparecem;
- [ ] consulta tem teste;
- [ ] índice está em migration;
- [ ] plano antes/depois está registrado;
- [ ] página vazia é válida.

## Testes obrigatórios

- empate completo resolvido por id;
- mesma batalha contabilizada duas vezes;
- 21 itens com size 20;
- page além do fim;
- size 0/negativo/acima;
- filtro inexistente;
- procurar email/accountId no JSON.

## Evidências

- decisão de projeção;
- migration;
- EXPLAIN antes/depois;
- testes/Bruno;
- commit: feat(ranking): add deterministic paged leaderboard.

## Perguntas de recuperação

1. Por que ordem precisa ser total?
2. Qual é a origem de verdade?
3. O que EXPLAIN ANALYZE faz?
4. Por que sort livre é risco?
5. Como reconstruir projeção?

## Erros comuns

- listar tudo;
- order apenas por wins;
- índice sem consulta;
- expor e-mail;
- atualizar ranking fora da transação;
- contar batalha repetida.

## Extensão opcional

Compare paginação por offset e cursor. Não troque no MVP; registre quando cursor seria melhor.

## Conteúdo

“Um ranking não é só ORDER BY: empate, índice e idempotência”.

## Correção e conferência — só depois da tentativa

A ordem deve terminar em identificador estável. A atualização só ocorre quando result_accounted_at está vazio e fica na mesma transação do marker. O índice precisa refletir filtro e prefixo da ordenação; o plano em conjunto de dados pequeno pode ainda escolher seq scan legitimamente.
