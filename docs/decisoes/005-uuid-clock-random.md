# ADR-005 — UUID, Clock e RandomSource

**Status:** Aceita — 20/08/2026.

## Decisão

IDs são UUID gerados pelo servidor. Tempo e aleatoriedade entram por abstrações injetáveis. Instantes são UTC.

## Consequências

Testes controlam IDs, relógio e sorte; batalhas e encontros são reproduzíveis. Não usar `Instant.now()`, `UUID.randomUUID()` ou `new Random()` espalhados pelo domínio.
