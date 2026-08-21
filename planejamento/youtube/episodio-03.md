# Episódio 03 - PostgreSQL, Flyway e inventário transacional

- **Semanas:** 5 e 6
- **Publicação planejada:** 04/10/2026
- **Duração:** 12-18 minutos
- **Thumbnail:** SEM DUPLICAR ITENS

## Hook

Um item duplicado por concorrência destrói a confiança no jogo.

## Promessa

Persistir sem contaminar o domínio e garantir inventário consistente.

## Demonstração final

Migration do zero, rollback e duas atualizações concorrentes.

## Blocos técnicos

- ERD
- Flyway
- Adapters JPA
- Transações e locks

## Roteiro

1. Abra com a consequência do problema.
2. Mostre o estado anterior em até 30 segundos.
3. Explique a decisão e uma alternativa descartada.
4. Mostre somente os trechos de código necessários.
5. Execute teste ou Bruno para provar a regra.
6. Mostre o resultado ponta a ponta.
7. Conte um erro real e o que mudou.
8. Feche com: Confira o ERD e o teste concorrente no PR.

## Shot list

- Abertura falando para câmera ou tela com título.
- Diagrama limpo do problema.
- Diff antes/depois.
- Execução de teste.
- Demo funcional.
- GitHub PR/release.

## Shorts relacionados

- Semana 5: Migration não é um SQL solto
- Semana 6: Rollback de inventário em 30 segundos

## Descrição base

Neste episódio da série RPG Arena, eu mostro persistir sem contaminar o domínio e garantir inventário consistente. Código, documentação e release: https://github.com/arthurtvrs10/rpg-arena-java
