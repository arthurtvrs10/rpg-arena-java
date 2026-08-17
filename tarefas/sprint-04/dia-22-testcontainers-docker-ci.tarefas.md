# Dia 22 — Testcontainers, Docker e CI

**Data:** 10/09/2026  
**Sprint:** 4  
**Tempo núcleo:** 2h30  
**Extensão:** 90 min  
**Resultado:** build reproduzível testa PostgreSQL real e gera imagem executável automaticamente.

## Antes de começar

- [ ] Docker funciona localmente.
- [ ] Suíte atual está verde.
- [ ] Crie branch chore/DE-02-ci-containers.
- [ ] Não atualize framework/dependências sem necessidade.

## O que você precisa compreender

- Testcontainers dá banco real e efêmero.
- Lifecycle e isolamento precisam ser claros.
- Dockerfile multi-stage reduz dependência do ambiente.
- Container roda como processo configurável; segredo entra em runtime.
- CI é fonte de verificação, não substitui revisão.
- Cache acelera, mas não deve esconder dependência faltante.

## Fontes oficiais

- Testcontainers: https://java.testcontainers.org/
- JUnit 5 quickstart: https://java.testcontainers.org/quickstart/junit_5_quickstart/
- Spring Boot Testcontainers: https://docs.spring.io/spring-boot/reference/testing/testcontainers.html
- Docker Java guide: https://docs.docker.com/guides/java/
- Actions Maven: https://docs.github.com/actions/guides/building-and-testing-java-with-maven

## Exemplo neutro — catálogo

Teste passa em H2, mas falha em PostgreSQL por índice parcial/tipo. Container real executa migrations e a mesma query. CI parte de checkout limpo, revelando configuração escondida no IDE.

## Tarefa prática

### 1. Testcontainers, 35 min

Configure PostgreSQL com versão alinhada ao Compose. Migre testes críticos:

- migrations/context;
- unique lower;
- reward idempotency;
- optimistic lock;
- ranking query.

Decida container compartilhado por classe/suíte e isolamento de dados.

### 2. Suíte, 20 min

Separe, se útil:

- unitários rápidos;
- integração;
- verificação completa.

Não dependa de ordem. Configure timeout no concorrente.

### 3. Dockerfile, 30 min

Crie build multi-stage:

- etapa Maven;
- runtime JRE;
- usuário não root, quando viável;
- JAR único;
- porta configurável;
- health;
- sem .env/secrets.

Use .dockerignore.

### 4. Compose completo, 20 min

App + PostgreSQL:

- depends_on com health;
- variáveis;
- rede;
- volume;
- healthchecks;
- ordem;
- restart documentado.

Teste docker compose up --build.

### 5. GitHub Actions, 30 min

Workflow em push/PR:

- checkout;
- Java 21;
- cache Maven;
- mvnw verify;
- relatório;
- build de imagem opcional após testes;
- permissões mínimas.

Fixe major versions conhecidas das actions e revise atualizações depois.

### 6. Evidência, 15 min

Abra PR, aguarde CI e corrija qualquer passo oculto.

## Critérios de aceite

- [ ] testes críticos usam PostgreSQL real;
- [ ] migrations rodam no teste;
- [ ] suíte não depende do banco local;
- [ ] imagem constrói;
- [ ] container não contém segredo;
- [ ] Compose aguarda banco saudável;
- [ ] CI parte de checkout limpo;
- [ ] PR fica verde.

## Testes obrigatórios

- Docker desligado produz diagnóstico claro para integração;
- mvnw verify;
- docker build;
- compose do zero;
- health;
- CI em PR;
- busca de segredo na imagem/config;
- container reinicia sem corromper migration.

## Evidências

- testes containerizados;
- Dockerfile/.dockerignore;
- compose;
- workflow;
- captura/link da CI;
- commit: ci(build): verify postgres integration and container image.

## Perguntas de recuperação

1. Que risco H2 mascara?
2. Quem executa migrations no teste?
3. Por que multi-stage?
4. Onde segredo entra?
5. O que CI limpa revela?

## Erros comuns

- usar latest;
- copiar .env para imagem;
- root sem pensar;
- CI pulando integração;
- teste compartilhando dados;
- Compose considerar started como ready.

## Extensão opcional

Adicione análise de dependências ou SBOM apenas se a pipeline Must já estiver estável.

## Conteúdo

“Do clone ao teste com PostgreSQL real em uma pipeline”.

## Correção e conferência — só depois da tentativa

O teste deve criar container, aplicar Flyway e executar contra PostgreSQL sem serviço manual. A imagem recebe configuração em runtime. A pipeline deve falhar se migration, teste concorrente ou build da aplicação falhar.
