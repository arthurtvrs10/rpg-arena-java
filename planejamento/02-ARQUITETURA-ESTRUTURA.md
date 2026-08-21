# Arquitetura e estrutura

## Escolha principal

Monólito modular orientado por domínio. Cada módulo controla regras, casos de uso, persistência e interfaces. Dependências entre módulos passam por portas, eventos ou contratos explícitos.

## Camadas dentro de cada módulo

- **domain:** entidades, value objects, agregados, policies, eventos e erros de negócio.
- **application:** casos de uso, portas, comandos, consultas e transações.
- **infrastructure:** JPA, adapters, mensageria interna, config e integrações.
- **interfaces:** REST, DTOs, mappers e tratamento HTTP.

## Estrutura de pastas

```text
rpg-arena/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── workflows/ci.yml
│   └── PULL_REQUEST_TEMPLATE.md
├── bruno/RPG-Arena/
├── docs/
│   ├── adr/
│   ├── api/
│   ├── architecture/
│   ├── content/
│   ├── database/
│   ├── game-design/
│   ├── operations/
│   ├── performance/
│   ├── portfolio/
│   ├── security/
│   └── testing/
├── src/main/java/io/github/arthurtvrs10/rpgarena/
│   ├── account/{domain,application,infrastructure,interfaces}/
│   ├── character/{domain,application,infrastructure,interfaces}/
│   ├── combat/{domain,application,infrastructure,interfaces}/
│   ├── inventory/{domain,application,infrastructure,interfaces}/
│   ├── progression/{domain,application,infrastructure,interfaces}/
│   ├── quest/{domain,application,infrastructure,interfaces}/
│   ├── world/{domain,application,infrastructure,interfaces}/
│   ├── economy/{domain,application,infrastructure,interfaces}/
│   └── shared/{domain,infrastructure}/
├── src/main/resources/db/migration/
├── src/test/java/...
├── compose.yaml
├── Dockerfile
├── pom.xml
└── README.md
```

## Regras arquiteturais

1. Domain não importa Spring, JPA ou web.
2. Interfaces chama application; nunca acessa repository diretamente.
3. Application controla transação e usa portas.
4. Infrastructure implementa portas e traduz erros técnicos.
5. Entidade JPA não é resposta HTTP.
6. Módulo não acessa classes internas de outro módulo.
7. Eventos internos carregam dados mínimos e possuem idempotência quando necessário.
8. Toda exceção técnica vira resultado/erro controlado antes do contrato HTTP.
9. Regras críticas recebem teste unitário; mapeamento, SQL, transação e segurança recebem integração.
10. Mudança arquitetural relevante exige ADR.

## Stack

- Java 21.
- Spring Boot 4.1.x.
- Maven Wrapper.
- PostgreSQL e Flyway.
- Spring Data JPA e Spring Security.
- JWT access/refresh.
- JUnit, Mockito, Testcontainers, ArchUnit e JaCoCo.
- Bruno e OpenAPI/springdoc.
- Docker, Compose, GitHub Actions, Actuator e Micrometer.

## Dependências permitidas

`interfaces -> application -> domain`

`infrastructure -> application/domain`

O domínio permanece no centro. Dependências externas apontam para dentro.

## ADRs obrigatórios

- Linguagem e versão.
- Framework e build.
- Banco e estratégia de migrations.
- Monólito modular.
- UUID e relógio.
- REST e formato de erro.
- JWT e sessão.
- Eventos internos e idempotência.
- Optimistic locking.
- Deploy e rollback.
