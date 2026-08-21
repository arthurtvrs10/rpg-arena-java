# RPG Arena API

[![Java 21](https://img.shields.io/badge/Java-21-orange.svg)](https://www.oracle.com/java/)
[![Spring Boot](https://img.shields.io/badge/Spring%20Boot-4.1.x-6DB33F.svg)](https://spring.io/projects/spring-boot)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Backend open source de um RPG PvE por turnos, desenvolvido como projeto de portfólio e laboratório de engenharia de software com Java, Spring Boot, PostgreSQL, segurança, testes, Docker e arquitetura orientada ao domínio.

> Estado atual: fundação do repositório. As funcionalidades estão planejadas e serão entregues durante 24 semanas. Não confunda requisito documentado com funcionalidade implementada.

## Jornada da versão 1.0

O jogador cria uma conta e um personagem, explora um mundo em grafo, enfrenta inimigos, usa habilidades e itens, evolui, conclui missões ramificadas, negocia com comerciantes e aparece no ranking. Administradores publicam versões válidas de conteúdo sem alterar jornadas em andamento.

## Escopo técnico

- Java 21 e Spring Boot 4.1.x;
- monólito modular por domínio;
- PostgreSQL, Flyway, JPA, transações e optimistic locking;
- API REST versionada, Problem Details e OpenAPI;
- JWT de acesso, refresh rotativo, RBAC e ownership;
- JUnit, Mockito, Testcontainers, ArchUnit e JaCoCo;
- Bruno, Docker Compose, GitHub Actions, logs e métricas.

## Módulos

`account`, `character`, `progression`, `inventory`, `combat`, `quest`, `world`, `economy`, `content`, `ranking` e `shared`.

## Documentação principal

- [Comece aqui](00-COMECE-AQUI.md)
- [Índice e decisões fechadas](docs/requisitos/00-INDICE-E-DECISOES-FECHADAS.md)
- [Especificação do produto](docs/requisitos/01-ESPECIFICACAO-DO-PRODUTO.md)
- [Catálogo de requisitos](docs/requisitos/02-CATALOGO-REQUISITOS.md)
- [Regras de negócio](docs/requisitos/03-REGRAS-DE-NEGOCIO.md)
- [Casos de uso](docs/requisitos/04-CASOS-DE-USO.md)
- [Histórias e critérios BDD](docs/requisitos/05-HISTORIAS-E-CRITERIOS-BDD.md)
- [Contrato OpenAPI](docs/api/openapi.yaml)
- [Modelo de dados](docs/dados/MODELO-E-DICIONARIO-DE-DADOS.md)
- [Matriz de rastreabilidade](docs/requisitos/08-MATRIZ-DE-RASTREABILIDADE.md)
- [Roadmap de 24 semanas](planejamento/03-ROADMAP-24-SEMANAS.md)
- [Plano da minissérie](planejamento/04-MINISSERIE-YOUTUBE.md)

## Planejamento

- Duração: 24 semanas, de 24/08/2026 a 07/02/2027;
- carga: 18–22 horas semanais;
- backlog: 144 tarefas;
- conteúdo: 12 episódios e 24 Shorts;
- releases: `v0.1.0`, `v0.2.0`, `v0.3.0`, `v0.4.0`, `v1.0.0-rc.1` e `v1.0.0`.

Abra `planejamento/BACKLOG-MESTRE-6-MESES.xlsx` para acompanhar o progresso e execute um arquivo por vez em `planejamento/tarefas/`.

## Execução do esqueleto atual

```bash
./mvnw clean test
./mvnw spring-boot:run
```

PostgreSQL, Flyway, Docker e demais dependências entram nas semanas indicadas pelo roadmap. Os comandos finais de infraestrutura serão liberados junto com as respectivas fatias verticais.

## Convenção de trabalho

1. Issue com requisito, regra, critérios e evidência.
2. Branch `tipo/descricao-curta`.
3. Implementação em fatia vertical.
4. Testes proporcionais ao risco.
5. Pull request ligado à issue.
6. Atualização da documentação e coleção Bruno.
7. Merge somente com CI verde.

## Repositório

- Nome: `rpg-arena-java`
- Descrição: `Open-source turn-based RPG backend built with Java 21 and Spring Boot to practice domain modeling, REST APIs, PostgreSQL, security, testing, Docker, and software architecture.`
- Licença: MIT
- Topics: `java`, `spring-boot`, `postgresql`, `ddd`, `rest-api`, `spring-security`, `jwt`, `docker`, `junit`, `testcontainers`, `open-source`, `rpg`, `turn-based-game`, `backend`, `software-architecture`.

Autor: [Arthur Tavares](https://github.com/arthurtvrs10).
