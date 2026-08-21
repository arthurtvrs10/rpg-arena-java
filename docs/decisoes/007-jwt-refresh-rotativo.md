# ADR-007 — JWT curto e refresh rotativo

**Status:** Aceita — 20/08/2026.

## Decisão

Access JWT de 15 minutos; refresh opaco de 7 dias, armazenado por hash e rotacionado a cada uso. Reuso revoga a família. Subject é account UUID.

## Consequências

JWT não substitui ownership. Logout revoga refresh; bloqueio revoga famílias. Segredo/chave nunca é versionado. Implementação precisa de teste de expiração, adulteração e reuse detection.
