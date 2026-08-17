# Dia 13 — Máquina de estados de missão

**Data:** 31/08/2026  
**Sprint:** 3 — Missões, combate e concorrência  
**Tempo núcleo:** 2h  
**Extensão:** 60 min  
**Resultado:** tentativa de missão com transições explícitas e estados terminais protegidos.

## Sprint Goal

Permitir missão e batalha por turnos sem efeitos duplicados, incluindo transações, idempotência e conflito concorrente observável.

## Antes de começar

- [ ] Faça revisão 1–3–7 da Sprint 2.
- [ ] Leia REG-MI.
- [ ] Crie branch feat/MI-01-mission-state.
- [ ] Defina apenas duas missões para teste.

## O que você precisa compreender

- Máquina de estados enumera transições aceitas e rejeitadas.
- Estado terminal impede repetição destrutiva.
- Catálogo de missão define oferta; tentativa captura execução.
- Data de término é efeito da transição, não campo arbitrário.
- Relógio injetável torna teste determinístico.
- Pré-condição de nível pertence ao início da tentativa.

## Fontes

- Java enum/API: https://docs.oracle.com/en/java/javase/21/docs/api/
- Spring Data transactions: https://docs.spring.io/spring-data/jpa/reference/jpa/transactions.html
- Documento local: ../../docs/03-REGRAS-DE-NEGOCIO.md

## Exemplo neutro — atendimento

Ticket OPEN pode ir a RESOLVED ou CANCELLED. RESOLVED não volta a OPEN sem comando específico de reabertura. closedAt nasce na transição. A tabela aceitar qualquer string não torna a transição válida.

## Tarefa prática

### 1. Tabela de transição, 20 min

Preencha:

| Estado atual | Comando | Próximo | Permitido? | Efeito |
|---|---|---|---|---|
| nenhum | start | ACTIVE | sim | startedAt |
| ACTIVE | complete | COMPLETED | sim | finishedAt |
| ACTIVE | fail | FAILED | sim | finishedAt |
| COMPLETED | complete | ? | não/idempotente? | definir |
| FAILED | complete | ? | não | nenhum |

Escolha comportamento de complete repetido sem ainda aplicar recompensa.

### 2. Modelo, 25 min

Implemente MissionAttempt com:

- id;
- characterId e missionId;
- status;
- timestamps;
- reward marker;
- version;
- métodos complete/fail.

Sem setters de status.

### 3. Catálogo e início, 20 min

Modele Mission com code, active, minLevel, reward XP/item. Caso de uso start:

- owner;
- personagem;
- missão ativa;
- nível;
- ausência de tentativa ACTIVE duplicada;
- criação ACTIVE.

### 4. Persistência, 20 min

Crie migration, índices e constraint/estratégia para tentativa ativa. Mapeie enum de forma consciente.

### 5. Testes, 25 min

- inicia válida;
- missão inativa;
- nível insuficiente;
- duplicada ativa;
- complete ativa;
- fail ativa;
- complete completed;
- complete failed;
- timestamp por clock controlado;
- tentativa de B.

### 6. API/Bruno/evidência, 10 min

Implemente início e, se couber, transição sem recompensa. Atualize contrato.

## Critérios de aceite

- [ ] estados e setas estão documentados;
- [ ] apenas ACTIVE termina;
- [ ] terminal não muda;
- [ ] timestamps vêm da transição;
- [ ] nível é verificado;
- [ ] tentativa pertence a personagem próprio;
- [ ] clock é testável;
- [ ] migration reproduz.

## Testes obrigatórios

Execute toda célula relevante da tabela. Verifique estado antes/depois de falha. Teste duas tentativas ativas sequenciais e registre estratégia para concorrência.

## Evidências

- tabela;
- domínio/testes;
- migration;
- requests;
- commit: feat(mission): enforce attempt state transitions.

## Perguntas de recuperação

1. Por que status não deve ter setter?
2. Quando minLevel é verificado?
3. Quem fornece finishedAt?
4. O que significa estado terminal?
5. Como impedir duas ACTIVE?

## Erros comuns

- ifs apenas no Controller;
- string livre;
- timestamp vindo do cliente;
- missão e tentativa como mesma entidade;
- concluir FAILED;
- conceder recompensa antes da transição.

## Extensão opcional

Teste uma constraint/índice parcial que impeça mais de uma tentativa ACTIVE por personagem e missão, confirmando no PostgreSQL real.

## Conteúdo

“Modelando missão como estado, não como campo editável”.

## Correção e conferência — só depois da tentativa

ACTIVE → COMPLETED/FAILED são as únicas transições do MVP. COMPLETED e FAILED são terminais. Uma repetição de complete pode retornar resultado anterior somente quando integrada à idempotência; não deve reexecutar efeitos. O objeto altera status e timestamp juntos.
