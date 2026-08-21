# Product Scope — archived 30-day version

> **REFERENCE ONLY:** the current approved specification is maintained in `../requisitos/`.

## 1. Executive Summary

**RPG Arena** is a RESTful API backend for a turn-based RPG. Authenticated players create characters, manage inventories with slot-based equipment, embark on state-driven missions, execute tactical turn-based combat actions, and compete on a public leaderboard.

The project serves as a comprehensive demonstration of real-world backend engineering in Java 21, Spring Boot, PostgreSQL, Spring Security, transactional consistency, concurrency control, Testcontainers, Docker, and CI/CD pipelines.

---

## 2. Problem Statement

Many portfolio projects demonstrate trivial CRUD operations without exposing challenging software engineering decisions—such as complex domain rules, state machine transitions, concurrent updates, idempotency guarantees, authorization boundaries, or automated test pipelines.

RPG Arena uses an accessible, engaging domain (a turn-based RPG) to make these backend engineering concepts explicit, testable, and demonstrable.

---

## 3. Target Personas

### 1. Player
Wants to create and progress characters, manage equipment, undertake quests, and battle enemies with confidence that their game progress and items cannot be accessed or corrupted by other players.

### 2. Administrator
Wants to maintain catalogs of game items, classes, abilities, and missions without accidental exposure to player credentials.

### 3. Technical Evaluator
Wants to clone and run the repository locally, review Architecture Decision Records (ADRs), inspect automated tests, verify clean concurrency handling, and assess engineering trade-offs with zero external guesswork.

---

## 4. MVP Scope & Goals

By the end of the 4-week roadmap (**2026-09-12**), the MVP delivers an end-to-end demonstrable cycle:

1. **Player Registration & Auth:** Register account and obtain signed JWT token.
2. **Character Creation:** Create up to 3 unique characters per account.
3. **Inventory Management:** Inspect inventory and equip/unequip gear with atomic slot verification.
4. **Mission Lifecycle:** Start, execute, and complete missions with strictly idempotent reward processing.
5. **Turn-Based Combat:** Initiate PvE combat, execute deterministic turn actions, enforce cooldowns, and handle concurrent turn attempts with optimistic locking.
6. **Leaderboard:** Query deterministic, paginated player rankings.
7. **Cross-Player Isolation:** Enforce ownership authorization across all player endpoints.
8. **DevOps & Verification:** Reproduce the entire environment with a single `docker compose up` command and verify with `./mvnw verify`.

---

## 5. Feature Breakdown (MoSCoW Matrix)

| Priority | Feature / Capability | Description |
|---|---|---|
| **MUST** | Identity & Security | Player registration, BCrypt password hashing, JWT authentication, `PLAYER` and `ADMIN` roles |
| **MUST** | Ownership Authorization | Identity resolved strictly from JWT; prevention of Broken Object-Level Authorization (BOLA/IDOR) |
| **MUST** | Character Progression | Pure Java XP and leveling formula, class attributes, max 3 characters per player |
| **MUST** | Inventory & Slots | Slot compatibility (`WEAPON`, `ARMOR`, `ACCESSORY`), atomic item swap, inventory limit validation |
| **MUST** | Mission State Machine | Finite state machine (`DRAFT`, `ACTIVE`, `COMPLETED`, `FAILED`); terminal state immutability |
| **MUST** | Idempotent Rewards | Single transaction for quest completion and reward grant; deduplication key support |
| **MUST** | Turn-Based Combat | Deterministic pure Java combat engine, turn ownership verification, action points, cooldowns |
| **MUST** | Concurrency Control | Optimistic locking (`@Version`) on battle entity to prevent race conditions during action processing |
| **MUST** | Paginated Ranking | Fast read projection of leaderboards with database indexes and execution plan verification |
| **MUST** | Infrastructure & CI | Flyway migrations, Testcontainers suite, Docker Compose setup, GitHub Actions pipeline |
| **SHOULD** | Battle Replay Logs | Detailed chronological event log of all actions taken in a battle |
| **SHOULD** | OpenAPI / Swagger UI | Interactive API documentation and RFC 7807 Problem Details |
| **COULD** | Admin CRUD Endpoints | Dedicated endpoints for managing quest and item catalogs |
| **WON'T** | Real-time Multiplayer | WebSocket / Real-time PvP (deferred to Post-MVP v2.0) |
| **WON'T** | Graphical Interface | Frontend web/mobile UI (the project is strictly a backend lab) |
| **WON'T** | Microservices / Kafka | Premature distributed architecture (Modular Monolith is enforced) |

---

## 6. Core Business Rules & Invariants

1. **Account Limits:** An active account can own at most 3 characters simultaneously.
2. **Name Uniqueness:** Character names are unique across the system (case-insensitive).
3. **Strict Ownership:** A player can only view or mutate characters, inventories, and active sessions belonging to their account.
4. **Item Ownership:** An equipped item must reside in the character's inventory.
5. **Single Item Per Slot:** An equipment slot accommodates at most one item at a time; equipping a new item swaps the current item atomically.
6. **Mission Lifecycle:** Quests follow strict transitions (`DRAFT` → `ACTIVE` → `COMPLETED` / `FAILED`). Completed or failed attempts cannot be modified.
7. **Atomic Reward Processing:** Completing a mission and granting its rewards (XP, items, gold) occur within a single database transaction.
8. **Idempotent Actions:** Submitting the same action request or reward claim multiple times produces no duplicate effects.
9. **Combat State Transitions:** Battles transition across `CREATED` → `IN_PROGRESS` → `FINISHED` / `CANCELLED`.
10. **Turn Ownership:** Only the active participant whose turn it is may submit a combat command.
11. **Defeated Combatants:** A character with 0 HP is marked defeated and cannot take actions.
12. **Skill Constraints:** Skills require sufficient resource points (mana/energy) and zero remaining cooldown.
13. **Deterministic Combat Resolution:** Combat calculations rely exclusively on pure domain formulas with seeded or controlled dice rolls.
14. **Ranking Integrity:** Only completed and officially recorded battles are factored into global rankings.

---

## 7. Non-Functional Requirements

| Category | Requirement & Verification |
|---|---|
| **Security** | Zero trust in client-provided `playerId`. Identity must be extracted from the authenticated JWT token. |
| **Transactional Consistency** | Inventory swaps and mission reward distributions are atomic (`@Transactional`). |
| **Concurrency** | Battles employ JPA optimistic locking (`@Version`) to safely handle simultaneous actions. |
| **Idempotency** | Action and reward requests accept an `Idempotency-Key` header to prevent double processing. |
| **Database Integrity** | All schema modifications are executed via immutable Flyway SQL migrations. |
| **Automated Testing** | Multi-tier test suite: pure unit tests for domain logic; Testcontainers PostgreSQL for database integration. |
| **API Standards** | RESTful principles, standard HTTP status codes, and RFC 7807 Problem Details for errors. |
| **Operational Readiness** | Containerized with Docker Compose; verifiable with health checks via Spring Boot Actuator. |
| **CI Automation** | Automated build and test verification on every pull request via GitHub Actions. |

---

## 8. Initial Endpoint Specifications

| Method | Endpoint | Access | Purpose |
|---|---|---|---|
| `POST` | `/api/v1/auth/register` | Public | Create player account |
| `POST` | `/api/v1/auth/login` | Public | Authenticate and obtain JWT |
| `GET` | `/api/v1/me` | `PLAYER` | Get current player profile |
| `POST` | `/api/v1/characters` | `PLAYER` | Create new character |
| `GET` | `/api/v1/characters` | `PLAYER` | List current player's characters |
| `GET` | `/api/v1/characters/{id}` | `PLAYER` | Get character details (owner only) |
| `GET` | `/api/v1/characters/{id}/inventory` | `PLAYER` | List character's inventory |
| `PUT` | `/api/v1/characters/{id}/equipment/{slot}` | `PLAYER` | Equip item into specific slot |
| `DELETE`| `/api/v1/characters/{id}/equipment/{slot}` | `PLAYER` | Unequip item from slot |
| `POST` | `/api/v1/characters/{id}/missions/{missionId}/attempts` | `PLAYER` | Start mission attempt |
| `POST` | `/api/v1/mission-attempts/{id}/complete` | `PLAYER` | Complete mission attempt & claim reward |
| `POST` | `/api/v1/characters/{id}/battles` | `PLAYER` | Start PvE battle |
| `POST` | `/api/v1/battles/{id}/actions` | `PLAYER` | Execute combat action |
| `GET` | `/api/v1/battles/{id}` | `PLAYER` | Get battle state & turn status |
| `GET` | `/api/v1/rankings` | Public | Paginated leaderboard |
| `POST` | `/api/v1/admin/items` | `ADMIN` | Create catalog item |
| `POST` | `/api/v1/admin/missions` | `ADMIN` | Create catalog mission |
