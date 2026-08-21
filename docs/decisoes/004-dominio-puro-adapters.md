# ADR-004 — Domínio puro e adapters

**Status:** Aceita — 20/08/2026.

## Decisão

Entidades, value objects, políticas e eventos de domínio não importam Spring, JPA, Jackson ou HTTP. Application define portas; infrastructure implementa persistência; interfaces traduz REST.

## Consequências

Existe custo explícito de mapeamento, compensado por regras testáveis e fronteiras legíveis. Entidade JPA nunca é DTO de resposta.
