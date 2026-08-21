# ADR-008 — Idempotência persistida

**Status:** Aceita — 20/08/2026.

## Decisão

Comandos com efeito crítico exigem `Idempotency-Key`. O banco persiste escopo, hash do request e resposta. Mesma chave/corpo devolve a resposta; corpo diferente conflita.

## Consequências

Timeout do cliente não duplica ação, compra ou recompensa. Requer canonicalização do payload, unique constraint e limpeza de registros operacionais expirados.
