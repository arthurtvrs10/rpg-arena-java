# Contributing to RPG Arena

Thank you for your interest in contributing to **RPG Arena**! This project is an open-source educational laboratory designed to practice real-world software engineering with Java 21, Spring Boot, PostgreSQL, and modern architecture practices.

---

## 1. Code of Conduct

All contributors and participants agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md). Please be respectful and constructive in all interactions.

---

## 2. Getting Started

1. **Check Existing Work:** Explore the [GitHub Issues](https://github.com/arthurtvrs10/rpg-arena-java/issues) to find tasks marked `good first issue` or `help wanted`.
2. **Fork & Clone:** Fork the repository to your account and clone it locally:
   ```bash
   git clone https://github.com/arthurtvrs10/rpg-arena-java.git
   cd rpg-arena-java
   ```
3. **Branch Strategy:** Create a dedicated branch off `main` following our branch naming convention:
   - `feat/<feature-name>` (e.g., `feat/character-leveling`)
   - `fix/<bug-description>` (e.g., `fix/jwt-expiration-check`)
   - `docs/<topic>` (e.g., `docs/update-architecture-guide`)
   - `refactor/<scope>` (e.g., `refactor/combat-action-handlers`)
   - `test/<component>` (e.g., `test/inventory-concurrency`)

---

## 3. Development Standards

- **Language & Runtime:** Java 21 LTS.
- **Pure Domain Logic:** Combat formulas and domain entity rules must remain framework-free in pure Java without Spring dependencies.
- **Security First:** Never trust `playerId` sent by the client. Identity must always be resolved via the authenticated security context.
- **Testing Requirements:**
  - Pure domain rules require comprehensive JUnit 5 unit tests.
  - Repository and integration tests must run against PostgreSQL using Testcontainers.
  - Every pull request must maintain or improve test coverage.
- **Database Migrations:** Schema changes must be added as new Flyway migration files (`V<N>__description.sql`). Never edit existing migrations.
- **No Secrets:** Never commit `.env` files, API keys, or JWT secrets.

---

## 4. Submitting a Pull Request

1. Run the entire test suite locally to verify everything compiles and passes:
   ```bash
   ./mvnw clean verify
   ```
2. Commit your changes using [Conventional Commits](https://www.conventionalcommits.org/):
   - `feat(character): add attribute recalculation on level up`
   - `fix(auth): handle invalid JWT signature with proper problem details`
   - `test(inventory): add concurrent equipment swap test`
3. Push your branch to GitHub and open a Pull Request targeting `main`.
4. Fill out the [Pull Request Template](.github/PULL_REQUEST_TEMPLATE.md) completely with acceptance criteria and testing evidence.

---

## 5. In-Depth Documentation

For advanced contributing instructions, architectural guidelines, and Portuguese study materials:
- [English Contributing Guide](docs/en/CONTRIBUTING-GUIDE.md)
- [Architecture Guide](docs/en/ARCHITECTURE.md)
- [Product Scope](docs/en/PRODUCT-SCOPE.md)
- [Brazilian Portuguese 30-Day Roadmap](docs/pt-BR/COMECE-AQUI.md)
