# Dia 17 — Concorrência, optimistic locking e idempotência

**Data:** 04/09/2026  
**Sprint:** 3  
**Tempo núcleo:** 2h  
**Extensão:** 90 min  
**Resultado:** duas requisições para o mesmo turno não produzem dois efeitos.

## Antes de começar

- [ ] Batalha funciona sequencialmente.
- [ ] battle_actions possui requestId.
- [ ] Crie branch feat/BA-05-concurrency.
- [ ] Leia documentação de isolamento antes de escolher lock.

## O que você precisa compreender

- Read Committed permite que duas transações leiam a mesma versão lógica.
- Optimistic locking detecta alteração pela coluna version.
- Idempotência trata repetição da mesma intenção; locking trata intenções concorrentes.
- São controles complementares.
- Conflito deve virar comportamento explícito, não 500 genérico.
- Retry automático cego pode executar ação fora do turno.

## Fontes oficiais

- PostgreSQL isolation: https://www.postgresql.org/docs/current/transaction-iso.html
- PostgreSQL locking: https://www.postgresql.org/docs/current/explicit-locking.html
- Spring Data locking: https://docs.spring.io/spring-data/jpa/reference/jpa/locking.html
- Hibernate locking: https://docs.jboss.org/hibernate/orm/current/userguide/html_single/Hibernate_User_Guide.html#locking

## Exemplo neutro — última vaga

Duas pessoas leem “1 vaga”. Sem controle, ambas reservam. Version detecta que a segunda grava estado antigo. Idempotency-Key impede que retry da primeira crie segunda reserva. Problemas diferentes, controles diferentes.

## Tarefa prática

### 1. Linha do tempo, 20 min

Desenhe T1 e T2:

- ambas leem Battle version 5;
- validam turno;
- calculam dano;
- T1 grava version 6;
- T2 tenta gravar.

Escreva resultado esperado e resposta pública.

### 2. ADR-003 e ADR-004, 25 min

Compare:

- sem lock;
- pessimista;
- otimista;
- serialização na aplicação.

Escolha otimista. Para idempotência, defina unique battle_id + request_id, hash/conteúdo e retry.

### 3. Implementação, 30 min

- coluna version mapeada;
- transação no caso de uso;
- consulta de requestId existente antes/apos conflito;
- constraint única;
- tradução de conflito para BATTLE_CONCURRENTLY_MODIFIED;
- nada de retry genérico automático.

### 4. Teste concorrente, 35 min

Use duas threads e uma barreira/latch:

1. estado inicial conhecido;
2. ambas prontas;
3. libere;
4. aguarde com timeout;
5. uma ação efetiva;
6. outra conflito ou resposta idempotente se mesma chave;
7. confira vida, turno, version e contagem de ações.

Repita com mesma requestId e com ids diferentes.

### 5. Bruno/manual, 20 min

Bruno pode provar repetição sequencial. Para concorrência real, use teste automatizado ou runner paralelo controlado. Documente limitação.

### 6. Evidência, 10 min

Atualize SECURITY/API/ADR e commit.

## Critérios de aceite

- [ ] version existe e incrementa;
- [ ] conflito não vira efeito duplo;
- [ ] requestId único por batalha;
- [ ] mesma chave devolve efeito único;
- [ ] chave igual/corpo diferente falha;
- [ ] teste usa sincronização e timeout;
- [ ] estado final é verificado no banco;
- [ ] conflito tem código público estável.

## Testes obrigatórios

- duas ids diferentes, mesma versão;
- mesma id, mesmo corpo;
- mesma id, corpo diferente;
- retry após resposta perdida simulada;
- ação após T1 finalizar batalha;
- conflito não deixa battle_action órfã.

## Evidências

- ADR-003/004;
- migration;
- teste concorrente;
- resultado repetido;
- commit: feat(battle): prevent duplicate concurrent turn effects.

## Perguntas de recuperação

1. O que version detecta?
2. O que requestId garante?
3. Por que controles são complementares?
4. Por que retry automático é perigoso?
5. O que o teste precisa verificar além da exceção?

## Erros comuns

- apenas synchronized local;
- Thread.sleep como coordenação;
- version no DTO sem no banco;
- retry infinito;
- unique sem tradução;
- testar somente retorno e não estado final.

## Extensão opcional

Compare um teste com lock pessimista. Registre tempo de bloqueio e risco de deadlock, sem trocar a decisão sem evidência.

## Conteúdo

“Duas ações no mesmo turno: idempotência não é locking”.

## Correção e conferência — só depois da tentativa

Com requestIds diferentes e mesma versão, somente uma transação deve confirmar. A outra recebe conflito e precisa reler antes de nova intenção. Com o mesmo requestId/corpo, ambas convergem para um único registro/efeito.

Se duas ações estão na tabela ou a vida caiu duas vezes, a garantia falhou.
