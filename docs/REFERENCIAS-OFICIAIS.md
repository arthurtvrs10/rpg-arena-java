# Referências oficiais

Use estas fontes antes de fóruns, vídeos ou respostas de IA. Pesquise pelo comportamento específico, reproduza um exemplo mínimo e registre a decisão no projeto.

## Java e build

- Java 21: https://docs.oracle.com/en/java/javase/21/
- Maven: https://maven.apache.org/guides/
- Maven Wrapper: https://maven.apache.org/wrapper/

## Spring

- Spring Boot: https://docs.spring.io/spring-boot/
- Spring Framework: https://docs.spring.io/spring-framework/reference/
- Spring Data JPA: https://docs.spring.io/spring-data/jpa/reference/
- Spring Security: https://docs.spring.io/spring-security/reference/
- Bean Validation: https://jakarta.ee/specifications/bean-validation/
- Spring Boot Actuator: https://docs.spring.io/spring-boot/reference/actuator/

## Banco

- PostgreSQL: https://www.postgresql.org/docs/current/
- Transações: https://www.postgresql.org/docs/current/tutorial-transactions.html
- Índices: https://www.postgresql.org/docs/current/indexes.html
- EXPLAIN: https://www.postgresql.org/docs/current/using-explain.html
- Flyway: https://documentation.red-gate.com/flyway/

## API e segurança

- HTTP Semantics: https://www.rfc-editor.org/rfc/rfc9110
- Problem Details: https://www.rfc-editor.org/rfc/rfc9457
- OpenAPI 3.0: https://spec.openapis.org/oas/v3.0.3
- OWASP API Security: https://owasp.org/API-Security/
- OWASP Password Storage: https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html
- JWT: https://www.rfc-editor.org/rfc/rfc7519

## Testes e ferramentas

- JUnit: https://docs.junit.org/current/user-guide/
- Mockito: https://javadoc.io/doc/org.mockito/mockito-core/latest/org.mockito/org/mockito/Mockito.html
- AssertJ: https://assertj.github.io/doc/
- Testcontainers Java: https://java.testcontainers.org/
- ArchUnit: https://www.archunit.org/userguide/html/000_Index.html
- JaCoCo: https://www.jacoco.org/jacoco/trunk/doc/
- Bruno: https://docs.usebruno.com/

## Docker e GitHub

- Docker: https://docs.docker.com/
- Docker Compose: https://docs.docker.com/compose/
- GitHub Actions: https://docs.github.com/actions
- GitHub Issues: https://docs.github.com/issues
- GitHub pull requests: https://docs.github.com/pull-requests

## Método de pesquisa sem IA

1. Abra o requisito/regra que precisa implementar.
2. Identifique a palavra-chave técnica: `optimistic locking`, `transaction rollback`, `security ownership`, etc.
3. Consulte a documentação oficial da tecnologia.
4. Faça um spike mínimo fora da feature quando houver incerteza.
5. Escreva um teste que prove o comportamento.
6. Registre o trade-off em ADR ou PR.
