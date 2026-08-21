# ADR-009 — Optimistic locking e constraints

**Status:** Aceita — 20/08/2026.

## Decisão

Agregados mutáveis usam versão otimista. Invariantes de unicidade/idempotência têm constraint no PostgreSQL. Conflitos são traduzidos para 409 de negócio.

## Consequências

Não fazer retry oculto de comando não comutativo. Cliente recebe versão atualizada e decide reenviar. Testes concorrentes provam batalha, estoque, inventário e recompensa.
