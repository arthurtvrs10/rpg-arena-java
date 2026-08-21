# ADR-006 — REST v1 e Problem Details

**Status:** Aceita — 20/08/2026.

## Decisão

API JSON sob `/api/v1`, OpenAPI 3.0 e erros baseados em Problem Details com `code`, `traceId`, timestamp e violações de campo.

## Consequências

Códigos são estáveis; mensagens podem evoluir. Mudança incompatível após RC é adiada ou cria nova versão. Controllers não expõem entidades ou detalhes técnicos.
