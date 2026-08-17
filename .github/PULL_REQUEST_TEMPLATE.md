## Description

<!-- Provide a concise summary of the changes introduced by this pull request. -->

### Associated Issue / Task
Fixes #<!-- Issue number here, e.g. #12 -->
Related to Epic: <!-- e.g. [EPIC-01] -->

---

## Type of Change

- [ ] `feat`: New feature / domain capability
- [ ] `fix`: Bug fix
- [ ] `docs`: Documentation updates
- [ ] `refactor`: Code refactoring without behavioral change
- [ ] `test`: Unit / integration / contract tests
- [ ] `chore`: Tooling / CI / build configuration

---

## Architectural & Security Verification

- [ ] Pure domain logic contains zero Spring framework dependencies.
- [ ] Identity is resolved strictly from the JWT security context (no client-trusted `playerId`).
- [ ] Transaction boundaries (`@Transactional`) are properly defined for multi-aggregate mutations.
- [ ] Concurrency-sensitive operations use optimistic locking (`@Version`) or idempotency keys.
- [ ] Database migrations are additive and tested with Flyway.
- [ ] No secrets, passwords, or test tokens are committed.

---

## Verification & Testing Evidence

### Automated Tests Executed
```bash
./mvnw clean verify
```

- [ ] Unit tests added / updated and passing.
- [ ] Testcontainers integration tests passing.
- [ ] Bruno API collection updated (if endpoint changed).

### Evidence / Screenshots
<!-- Attach test outputs, Bruno execution logs, or relevant terminal captures -->

---

## Checklist for Reviewers

- [ ] Code follows project formatting and Java 21 conventions.
- [ ] Acceptance criteria from the issue are completely satisfied.
- [ ] Documentation (README / ADRs / OpenAPI) updated where appropriate.
