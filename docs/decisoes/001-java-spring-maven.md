# ADR-001 — Java 21, Spring Boot 4.1.x e Maven

**Status:** Aceita — 20/08/2026.

## Contexto

O projeto precisa demonstrar backend Java moderno, build reproduzível e ecossistema compatível com REST, segurança, dados e testes.

## Decisão

Usar Java 21, Spring Boot 4.1.x e Maven Wrapper. Dependências seguem o BOM do Spring; versões explícitas exigem justificativa.

## Consequências

Recursos da linguagem podem usar Java 21. A temporada não migra de framework/versão sem vulnerabilidade ou incompatibilidade bloqueadora. Toda pessoa usa `./mvnw`, não uma versão global de Maven.
