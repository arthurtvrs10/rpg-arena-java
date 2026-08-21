# RPG Arena

Open-source turn-based RPG backend built with Java 21 and Spring Boot to practice domain modeling, REST APIs, PostgreSQL, security, testing, Docker, and software architecture.

## Status

![Java](https://img.shields.io/badge/Java-21-ED8B00) ![Spring Boot](https://img.shields.io/badge/Spring_Boot-4.1-6DB33F) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-18-4169E1) ![License](https://img.shields.io/badge/License-MIT-7C3AED)

## Why this project exists

RPG Arena is a portfolio-grade backend used to study and demonstrate domain modeling, transactions, security, automated testing, delivery, and technical communication through a public YouTube series.

## Core features

- Accounts, JWT sessions, roles, and resource ownership.
- Rich character and deterministic turn-based combat domains.
- Inventory, equipment, loot, progression, skills, and quests.
- World graph, travel, encounters, NPCs, and economy.
- Administrative and versioned content publishing.
- PostgreSQL, Flyway, OpenAPI, Bruno, Testcontainers, Docker, CI, metrics, and deployment.

## Architecture

Modular monolith organized by domain. Each module contains domain, application, infrastructure, and interface boundaries. See [architecture documentation](docs/architecture/).

## Quick start

```bash
git clone https://github.com/arthurtvrs10/rpg-arena-java.git
cd rpg-arena-java
cp .env.example .env
docker compose up --build
```

API documentation: `http://localhost:8080/swagger-ui.html`

## Test

```bash
./mvnw clean verify
```

## Roadmap

See [ROADMAP.md](ROADMAP.md).

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md), select an issue labeled `good first issue`, and open a pull request.

## Security

Report vulnerabilities according to [SECURITY.md](SECURITY.md).

## License

MIT. See [LICENSE](LICENSE).
