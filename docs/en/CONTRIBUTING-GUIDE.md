# Contributing Guide — RPG Arena

This document provides technical guidelines and workflow instructions for contributing to the **RPG Arena** codebase.

---

## 1. Branching & PR Strategy

We follow a structured branch naming convention:

- `feat/<short-description>`: New domain feature or application capability.
- `fix/<short-description>`: Bug fix or corrective behavior change.
- `docs/<short-description>`: Documentation, ADRs, or specification changes.
- `refactor/<short-description>`: Code refactoring with zero external behavior modification.
- `test/<short-description>`: Adding unit, integration, or contract tests.
- `chore/<short-description>`: Build tooling, CI automation, or dependencies.

All work must be merged into `main` via Pull Requests. Direct pushes to `main` are restricted.

---

## 2. Commit Message Standards

We strictly adhere to [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/):

```text
<type>(<scope>): <short imperative description>

[optional body]

[optional footer(s)]
```

### Examples
- `feat(character): implement XP calculation and level progression`
- `fix(battle): prevent action submission during opponent turn`
- `docs(adr): record ADR-002 pure java combat engine decision`
- `test(inventory): add concurrent equipment swap testcontainers test`

---

## 3. Coding & Engineering Guidelines

1. **Keep Domain Models Clean:** Do not import Spring dependencies (`org.springframework.*`) or persistence annotations into pure domain logic classes.
2. **Handle Optional & Nulls Cleanly:** Prefer Java `Optional<T>` for query results that may be absent. Avoid returning raw `null`.
3. **Immutability by Default:** Prefer Java `record` for DTOs, value objects, commands, and query objects.
4. **Exceptions & HTTP Mapping:** Throw domain-specific exceptions (e.g., `CharacterNotFoundException`, `InvalidBattleStateException`) and handle them cleanly in `GlobalExceptionHandler` mapping to RFC 7807 Problem Details.
5. **No Blind Catching:** Never write empty `catch (Exception e) {}` blocks. Log unexpected errors with context.

---

## 4. Local Build & Test Verification

Before pushing your changes, run:

```bash
# Verify formatting, compile, and run all unit + integration tests
./mvnw clean verify
```

Ensure that:
- All unit tests pass.
- Testcontainers starts and executes against PostgreSQL cleanly.
- Code coverage is maintained.

---

## 5. Review & Approval Process

1. Open your PR against `main`.
2. Fill out all sections of [PULL_REQUEST_TEMPLATE.md](../../.github/PULL_REQUEST_TEMPLATE.md).
3. The maintainer (`@arthurtvrs10`) will review your code for domain correctness, test coverage, and architecture compliance.
4. Once approved and CI is green, the PR will be squash-merged.
