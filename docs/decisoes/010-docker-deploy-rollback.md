# ADR-010 — Docker, deploy único e rollback

**Status:** Aceita — 20/08/2026.

## Decisão

Dockerfile multi-stage executa a aplicação sem root. Compose reúne API e PostgreSQL local. Produção usa uma imagem imutável e PostgreSQL gerenciado; rollback reaponta para imagem anterior compatível.

## Consequências

Build e smoke são reproduzíveis. Migrations incompatíveis exigem estratégia expand/contract. Plataforma é escolhida na Semana 21 por custo, HTTPS, logs, backup e plano de saída.
