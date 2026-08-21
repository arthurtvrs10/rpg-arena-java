# Arquitetura alvo

## Estilo

Monólito modular orientado por domínio. Uma aplicação, um deploy e um banco, com fronteiras internas explícitas. Não usar pacotes globais `controller`, `service` e `repository`.

## Módulos

| Módulo | Responsabilidade | Agregados principais | Publica/consome |
|---|---|---|---|
| account | conta, senha, sessão, papéis | Account, SessionFamily | AccountRegistered, AccountBlocked |
| character | identidade e estado do personagem | Character | CharacterCreated, LevelChanged |
| progression | XP, nível e habilidades | Progression/CharacterSkill | ExperienceGranted, SkillUnlocked |
| inventory | posse, pilha, equipamento, consumo | Inventory, Equipment | ItemGranted, ItemConsumed |
| combat | batalha, turno, ação e resultado | Battle | BattleStarted, BattleFinished |
| quest | instância, objetivo, escolha e recompensa | QuestInstance | QuestCompleted, RewardGranted |
| world | locais, conexões, posição, encontro | CharacterLocation | CharacterTraveled, EncounterGenerated |
| economy | ouro, estoque, compra, venda | MerchantStock/Transaction | ItemBought, ItemSold |
| content | definições, versões e publicação | ContentVersion | ContentPublished |
| ranking | projeção pública | RankingEntry | consome BattleFinished/LevelChanged |
| shared | IDs, Clock, RandomSource, erros, idempotência e eventos | serviços técnicos mínimos | suporte |

## Camadas por módulo

```text
<module>/
├── domain/
│   ├── model/
│   ├── policy/
│   ├── event/
│   └── exception/
├── application/
│   ├── command/
│   ├── query/
│   ├── port/in/
│   └── port/out/
├── infrastructure/
│   ├── persistence/
│   ├── config/
│   └── adapter/
└── interfaces/
    └── rest/
        ├── dto/
        └── mapper/
```

Dependências: `interfaces -> application -> domain`; `infrastructure -> application/domain`. Domínio não importa Spring, JPA, Jackson ou HTTP.

## Estrutura alvo do repositório

```text
rpg-arena/
├── .github/
├── bruno/RPG-Arena/
├── docs/
│   ├── requisitos/
│   ├── arquitetura/
│   ├── dados/
│   ├── api/
│   ├── game-design/
│   ├── decisoes/
│   └── qualidade/
├── planejamento/
│   ├── tarefas/
│   └── youtube/
├── src/main/java/io/github/arthurtvrs10/rpgarena/
│   ├── account/
│   ├── character/
│   ├── progression/
│   ├── inventory/
│   ├── combat/
│   ├── quest/
│   ├── world/
│   ├── economy/
│   ├── content/
│   ├── ranking/
│   └── shared/
├── src/main/resources/db/migration/
├── src/test/java/io/github/arthurtvrs10/rpgarena/
├── compose.yaml
├── Dockerfile
├── pom.xml
└── README.md
```

## Comunicação entre módulos

- Chamada síncrona por porta para decisão necessária no mesmo comando.
- Evento de domínio interno para consequências desacopladas.
- Na v1.0, eventos críticos que precisam atomicidade executam na mesma transação; não há broker.
- Handlers devem ser idempotentes por `eventId + consumer`.
- Módulo pode referenciar ID/contrato público de outro, nunca entidade interna ou repository.

## Agregados e transações

Não criar um agregado gigante para toda a jornada. Character protege stats/progressão; Inventory protege posse/equipamento; Battle protege turno/estado; QuestInstance protege missão; MerchantStock protege estoque. O caso de uso coordena múltiplos agregados na transação quando o requisito exige atomicidade.

## Interfaces técnicas obrigatórias

```java
public interface ClockPort { Instant now(); }
public interface RandomSource { int nextInt(int originInclusive, int boundExclusive); }
public interface IdGenerator { UUID newId(); }
public interface DomainEventPublisher { void publish(Collection<DomainEvent> events); }
```

O código concreto pode usar `java.time.Clock` diretamente por adapter; o objetivo é impedir tempo e sorte globais nos testes.

## Persistência

- Domínio não recebe anotações JPA.
- Adapters mapeiam domain ↔ persistence model.
- Repositories de aplicação retornam Optional/resultado de domínio, não `JpaRepository` para controllers.
- `@Transactional` fica no caso de uso/application service ou boundary explícito.
- Optimistic lock traduz para código de conflito de negócio.
- Constraints de banco são última barreira de invariantes concorrentes.

## API

- Prefixo `/api/v1`.
- Controllers finos: DTO, validação de forma, identidade e chamada de caso.
- Problem Details centralizado.
- OpenAPI é revisado junto com a implementação.
- Sem entidade JPA em request/response.
- Idempotency-Key e version são explícitos nos comandos críticos.

## Segurança

Spring Security autentica; casos de uso/repositories protegem ownership. A política 404 para recurso alheio é uniforme. ADMIN não acessa dados privados por padrão. A matriz completa está em `docs/requisitos/06-MATRIZ-PERMISSOES-E-SEGURANCA.md`.

## Testes por risco

- domínio: JUnit/AssertJ, sem Spring;
- aplicação: portas fake/mock e transação lógica;
- persistência: Testcontainers PostgreSQL;
- web: `@WebMvcTest`/integração HTTP;
- segurança: matriz allow/deny;
- arquitetura: ArchUnit;
- jornada: Bruno runner e smoke;
- concorrência: threads/requests coordenadas contra PostgreSQL real.

## Regras de dependência verificadas por ArchUnit

1. `..domain..` não depende de Spring/JPA/Jackson.
2. `..interfaces..` não acessa `..infrastructure.persistence..`.
3. módulo não acessa pacote não público de outro módulo.
4. controllers terminam em `Controller`; casos de uso em `UseCase`/`Handler` conforme convenção.
5. DTOs ficam em interfaces e não são entidades.

## Observabilidade

Filtro cria/valida traceId; logs estruturados registram operação, duração, status e IDs técnicos necessários, sem token ou e-mail quando não indispensável. Métricas usam nomes estáveis e labels de baixa cardinalidade. Auditoria é domínio persistido; logs não substituem auditoria.

## Diagramas

- `diagramas/contexto.mmd`
- `diagramas/modulos.mmd`
- `diagramas/sequencia-combate.mmd`
- `diagramas/estado-batalha.mmd`
- `diagramas/estado-missao.mmd`
- `diagramas/modelo-dados.mmd`

## Decisão de simplicidade

Não introduzir Redis, Kafka, cache, CQRS completo, event sourcing ou microserviços antes de medição/requisito. Ranking é projeção no mesmo PostgreSQL; eventos são internos; idempotência é persistida no banco.
