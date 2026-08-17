# Referências e pesquisa sem IA

Este arquivo é seu mapa de consulta. Comece pela fonte primária, leia a seção necessária e produza um experimento pequeno. Não tente ler uma documentação inteira antes de trabalhar.

## Java e build

| Necessidade | Fonte | Onde começar |
|---|---|---|
| Java 21 | https://docs.oracle.com/en/java/javase/21/ | Language Updates e API Specification |
| Maven | https://maven.apache.org/guides/getting-started/ | Build lifecycle, POM e dependencies |
| Git | https://git-scm.com/docs | git-switch, git-commit, git-rebase, git-log |
| Exercícios Git | https://skills.github.com/ | Introduction to GitHub e Review pull requests |

## Spring

| Necessidade | Fonte | Onde começar |
|---|---|---|
| Spring Boot | https://docs.spring.io/spring-boot/reference/index.html | Using, configuration, testing, container images |
| Spring Web MVC | https://docs.spring.io/spring-framework/reference/web/webmvc.html | Annotated controllers e HTTP message conversion |
| Validação | https://docs.spring.io/spring-framework/reference/core/validation/beanvalidation.html | Bean Validation |
| Transações | https://docs.spring.io/spring-framework/reference/data-access/transaction.html | Declarative transaction management |
| Spring Data JPA | https://docs.spring.io/spring-data/jpa/reference/ | Repositories, transactions e locking |
| Locking JPA | https://docs.spring.io/spring-data/jpa/reference/jpa/locking.html | Lock metadata |
| Spring Security | https://docs.spring.io/spring-security/reference/index.html | Architecture, authentication, authorization |
| JWT Resource Server | https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/jwt.html | JWT validation; compare with your chosen implementation |
| Actuator | https://docs.spring.io/spring-boot/reference/actuator/ | Endpoints, health e observability |

Regra: mantenha a versão Spring Boot que já funciona no projeto durante as quatro sprints. Leia a documentação correspondente à versão do seu POM.

## Banco e persistência

| Necessidade | Fonte | Onde começar |
|---|---|---|
| SQL PostgreSQL | https://www.postgresql.org/docs/current/sql.html | SELECT, DDL, constraints e EXPLAIN |
| Concorrência | https://www.postgresql.org/docs/current/mvcc.html | MVCC e isolamento |
| Isolamento | https://www.postgresql.org/docs/current/transaction-iso.html | Read Committed e anomalias |
| Locks | https://www.postgresql.org/docs/current/explicit-locking.html | Table e row locks, deadlocks |
| Índices | https://www.postgresql.org/docs/current/indexes.html | Tipos, multicoluna e índices parciais |
| EXPLAIN | https://www.postgresql.org/docs/current/using-explain.html | Planos e custos |
| Hibernate ORM | https://hibernate.org/orm/documentation/ | User Guide da sua versão |
| Flyway | https://documentation.red-gate.com/flyway | Migrations, validate e repair |

## API e segurança

| Necessidade | Fonte | Onde começar |
|---|---|---|
| Semântica HTTP | https://www.rfc-editor.org/rfc/rfc9110.html | Methods e status codes |
| Problem Details | https://www.rfc-editor.org/rfc/rfc9457.html | Members e extensão |
| OpenAPI 3.1 | https://spec.openapis.org/oas/v3.1.1.html | Paths, schemas e responses |
| OWASP API Security | https://owasp.org/www-project-api-security/ | Top 10 e recursos |
| Top 10 API 2023 | https://owasp.org/API-Security/editions/2023/en/0x11-t10/ | BOLA, auth, function-level auth |
| Password Storage | https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html | Algoritmos e parâmetros |
| REST Security | https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html | Tokens, status e validação |

## Testes e entrega

| Necessidade | Fonte | Onde começar |
|---|---|---|
| JUnit | https://docs.junit.org/current/user-guide/ | Writing tests, assertions e parameterized tests |
| Mockito | https://javadoc.io/doc/org.mockito/mockito-core/latest/org.mockito/org/mockito/Mockito.html | Verification e stubbing |
| Testcontainers | https://java.testcontainers.org/ | Quickstart e JUnit 5 |
| Testcontainers JUnit | https://java.testcontainers.org/quickstart/junit_5_quickstart/ | Container lifecycle |
| Bruno testes | https://docs.usebruno.com/testing/tests/introduction | Testes e execução |
| Bruno assertions | https://docs.usebruno.com/testing/tests/assertions | Status, body e headers |
| Docker Compose | https://docs.docker.com/compose/gettingstarted/ | Serviços e execução |
| Ordem/healthcheck | https://docs.docker.com/compose/how-tos/startup-order/ | depends_on e service_healthy |
| Actions + Maven | https://docs.github.com/actions/guides/building-and-testing-java-with-maven | Workflow e cache |

## Exemplos mantidos pelos projetos

- Spring Petclinic: https://github.com/spring-projects/spring-petclinic
- Spring Guides: https://spring.io/guides
- Spring Security samples: https://github.com/spring-projects/spring-security-samples
- Testcontainers Java examples: https://github.com/testcontainers/testcontainers-java/tree/main/examples
- GitHub Actions examples para Java: https://docs.github.com/actions/guides/building-and-testing-java-with-maven

Use exemplos para observar uma decisão específica. Não copie a arquitetura inteira de um sistema cujo problema é diferente.

## Como formular uma busca

### Boa

~~~text
site:docs.spring.io/spring-data/jpa optimistic locking @Version
~~~

~~~text
site:postgresql.org/docs current unique index lower email
~~~

~~~text
site:docs.usebruno.com assertions response body
~~~

~~~text
site:docs.spring.io/spring-security authorize request role
~~~

### Ruim

~~~text
projeto rpg spring completo github pronto
~~~

Essa busca tende a produzir cópia sem compreensão e versões incompatíveis.

## Como ler um exemplo

1. Qual problema ele resolve?
2. Qual é a entrada e a saída?
3. Qual contrato da biblioteca está sendo usado?
4. Qual parte é configuração e qual é regra?
5. Que suposição pode não valer no RPG?
6. Qual o menor experimento para confirmar?
7. Como você escreveria com nomes do seu domínio?

## Diagnóstico por mensagem de erro

1. preserve a mensagem completa;
2. encontre a primeira causa do seu código na stack;
3. identifique versão da biblioteca;
4. busque texto significativo entre aspas mais o domínio oficial;
5. confirme no manual da mesma versão;
6. crie teste que reproduz;
7. corrija uma causa;
8. rode novamente e registre.

## Hierarquia de confiança

1. especificação/RFC;
2. documentação da versão usada;
3. repositório oficial e testes do projeto;
4. issue oficial com mantenedor;
5. artigo do autor/projeto;
6. fonte secundária, sempre confirmada.

## Ficha de estudo

- Pergunta:
- Fonte e seção:
- Versão:
- Previsão:
- Experimento:
- Resultado:
- Regra em minhas palavras:
- Caso em que não se aplica:
- Próxima revisão: amanhã / 3 dias / 7 dias.
