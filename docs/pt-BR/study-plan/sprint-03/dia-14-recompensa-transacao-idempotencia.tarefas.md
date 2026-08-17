# Dia 14 — Recompensa transacional e idempotente

**Data:** 01/09/2026  
**Sprint:** 3  
**Tempo núcleo:** 2h  
**Extensão:** 90 min  
**Resultado:** conclusão concede XP/item exatamente uma vez, inclusive sob repetição.

## Antes de começar

- [ ] MissionAttempt e Progression estão testados.
- [ ] Escolha forma da Idempotency-Key.
- [ ] Crie branch feat/MI-03-idempotent-reward.
- [ ] Escreva o que deve ocorrer em cada falha.

## O que você precisa compreender

- Retry é normal em rede; repetição não pode duplicar efeito.
- Idempotência exige identidade persistida da operação.
- Check-then-act sem constraint sofre corrida.
- Transação une estado da missão e recompensa.
- Constraint única é controle final; aplicação traduz conflito.
- Mesma chave com corpo diferente deve ser rejeitada.

## Fontes oficiais

- Spring transactions: https://docs.spring.io/spring-framework/reference/data-access/transaction.html
- Spring Data transactions: https://docs.spring.io/spring-data/jpa/reference/jpa/transactions.html
- PostgreSQL isolation: https://www.postgresql.org/docs/current/transaction-iso.html
- PostgreSQL constraints: https://www.postgresql.org/docs/current/ddl-constraints.html

## Exemplo neutro — pagamento

Cliente envia payment request com chave K. Timeout ocorre após gravação. Retry com K devolve resultado existente; não cobra outra vez. “Verificar se existe e depois inserir” precisa de unicidade porque duas requisições podem verificar antes de qualquer insert.

## Tarefa prática

### 1. Contrato de idempotência, 20 min

Defina:

- onde vem a chave;
- escopo owner + operação + tentativa;
- tamanho/formato;
- hash da requisição;
- resposta na repetição;
- mesma chave/corpo diferente;
- retenção;
- estado em processamento, se modelado.

### 2. Modelo de persistência, 20 min

Escolha:

- reward_granted_at + reward_key única na tentativa; ou
- tabela idempotency_records/reward_grants.

Para o MVP, a primeira pode bastar se uma tentativa tem uma recompensa. Registre limitação.

### 3. Caso de uso transacional, 30 min

Unidade:

1. carregar tentativa própria;
2. reconhecer chave repetida e devolver resultado;
3. validar ACTIVE;
4. completar;
5. conceder XP pelo domínio;
6. adicionar item, se previsto;
7. marcar reward;
8. persistir tudo;
9. devolver resumo.

Nenhuma chamada externa dentro da transação.

### 4. Falha e rollback, 20 min

Introduza falha controlada depois da alteração de XP e antes do marker. Teste que missão, XP e item retornam ao estado anterior.

### 5. Repetição/concorrência, 25 min

Teste:

- primeira chave K;
- retry K;
- K com conteúdo diferente;
- chave K2 após concluída;
- duas K simultâneas, se possível;
- falha e retry.

### 6. Bruno/evidência, 15 min

Faça duas chamadas idênticas e consulte XP/inventário. Atualize contrato.

## Critérios de aceite

- [ ] estado e recompensa compartilham transação;
- [ ] mesma chave não duplica;
- [ ] constraint única apoia garantia;
- [ ] corpo diferente com mesma chave falha;
- [ ] rollback remove efeito parcial;
- [ ] resposta repetida está documentada;
- [ ] owner é validado;
- [ ] teste mede XP/item, não apenas status.

## Testes obrigatórios

Estado inicial conhecido → concluir → registrar XP/item → repetir cinco vezes → estado final igual ao da primeira. Forçar exceção no meio → estado igual ao inicial. Tentar tentativa de B.

## Evidências

- contrato de idempotência;
- migration/constraint;
- teste de rollback;
- requests repetidos;
- commit: feat(mission): grant rewards exactly once in one transaction.

## Perguntas de recuperação

1. Por que retry é esperado?
2. O que a constraint resolve?
3. Qual é a unidade transacional?
4. Como mesma chave/corpo diferente se comporta?
5. Por que status 200 não prova idempotência?

## Erros comuns

- boolean em memória;
- verificar e inserir sem unique;
- marcar completed e recompensar em transações separadas;
- engolir exceção dentro de método transacional;
- chamar outra API;
- teste sem medir efeito.

## Extensão opcional

Implemente teste com barreira e duas threads. Se não conseguir estabilizar, mantenha para Dia 17 e documente a lacuna.

## Conteúdo

“O botão foi clicado duas vezes: por que a recompensa não duplica”.

## Correção e conferência — só depois da tentativa

A garantia depende de três elementos: chave persistida, unicidade atômica no banco e transação que inclui todos os efeitos. Um if rewardGranted antes de salvar não é suficiente sob concorrência.

No retry da mesma chave, devolver o resumo anterior é amigável. Uma chave nova para tentativa já terminal não deve gerar nova recompensa.
