# Arquitetura e estrutura de pastas

## Escolha

Monólito modular organizado por funcionalidade. Cada funcionalidade contém API, aplicação, domínio e infraestrutura. A separação serve para explicitar responsabilidades e dependências sem custo operacional de microsserviços.

## Estrutura alvo do repositório

~~~text
rpg-arena/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── feature.md
│   │   └── bug.md
│   ├── workflows/
│   │   └── ci.yml
│   └── PULL_REQUEST_TEMPLATE.md
├── bruno/
│   ├── environments/
│   ├── 01-auth/
│   ├── 02-characters/
│   ├── 03-inventory/
│   ├── 04-missions/
│   ├── 05-battles/
│   └── 06-ranking/
├── docs/
│   ├── adr/
│   ├── diagrams/
│   ├── API.md
│   ├── DOMAIN.md
│   ├── PRODUCT-SCOPE.md
│   └── SECURITY.md
├── src/
│   ├── main/
│   │   ├── java/com/seunome/rpgarena/
│   │   │   ├── shared/
│   │   │   │   ├── config/
│   │   │   │   ├── error/
│   │   │   │   ├── security/
│   │   │   │   └── validation/
│   │   │   ├── auth/
│   │   │   │   ├── api/
│   │   │   │   ├── application/
│   │   │   │   ├── domain/
│   │   │   │   └── infrastructure/
│   │   │   ├── player/
│   │   │   ├── character/
│   │   │   ├── inventory/
│   │   │   ├── mission/
│   │   │   ├── battle/
│   │   │   └── ranking/
│   │   └── resources/
│   │       ├── db/migration/
│   │       ├── application.yml
│   │       ├── application-local.yml
│   │       └── application-test.yml
│   └── test/
│       └── java/com/seunome/rpgarena/
│           ├── architecture/
│           ├── auth/
│           ├── character/
│           ├── inventory/
│           ├── mission/
│           └── battle/
├── .env.example
├── .gitignore
├── compose.yml
├── Dockerfile
├── LICENSE
├── pom.xml
├── README.md
└── CHANGELOG.md
~~~

## Estrutura interna de uma funcionalidade

Exemplo conceitual para battle:

~~~text
battle/
├── api/
│   ├── BattleController
│   ├── CreateBattleRequest
│   ├── PerformActionRequest
│   └── BattleResponse
├── application/
│   ├── CreateBattleUseCase
│   ├── PerformBattleActionUseCase
│   └── port/
├── domain/
│   ├── Battle
│   ├── Combatant
│   ├── BattleAction
│   ├── BattleStatus
│   └── rule/
└── infrastructure/
    ├── persistence/
    └── mapping/
~~~

Não é necessário criar todas as subpastas antecipadamente. Crie uma pasta quando houver responsabilidade real.

## Dependências permitidas

~~~mermaid
flowchart TD
    API["API"] --> APP["Application"]
    APP --> DOM["Domain"]
    INF["Infrastructure"] --> APP
    INF --> DOM
~~~

- API conhece casos de uso e DTOs, não regras de persistência.
- Application orquestra transação, autorização e portas.
- Domain contém estado, comportamento e invariantes; não depende do Spring.
- Infrastructure implementa persistência, token, relógio e outras portas.
- Shared contém apenas elementos genuinamente transversais.

## Regras de dependência

- Controller não acessa Repository.
- Entidade JPA não é retornada pela API.
- Domínio não importa Controller, SecurityContext, JPA Repository ou DTO HTTP.
- Um módulo não altera tabela interna de outro por atalho.
- Identificadores atravessam limites; objetos internos só quando contrato explícito.
- Shared não vira depósito de classes sem dono.
- Toda exceção pública passa pelo mapeamento padronizado.

## Casos de uso e transações

O limite transacional fica no método de caso de uso que representa uma unidade de negócio. Exemplos:

- equipar item;
- concluir missão e conceder recompensa;
- executar ação e avançar batalha;
- contabilizar resultado.

Operação somente de leitura pode declarar intenção read-only. Não abra transação longa envolvendo rede ou espera humana.

## Portas recomendadas

- PasswordHasher;
- TokenIssuer;
- CurrentActor;
- Clock;
- RandomSource;
- BattleRepository;
- IdempotencyRepository.

Essas portas permitem testar decisões sem subir o framework.

## ADRs obrigatórios

### ADR-001 — Monólito modular

Registrar contexto, alternativas (camadas globais, microsserviços), decisão, consequências e sinais de revisão.

### ADR-002 — Autorização por identidade

Registrar por que playerId do cliente não é fonte de verdade e como propriedade é verificada.

### ADR-003 — Concorrência da batalha

Comparar bloqueio pessimista, optimistic locking e serialização; escolher versão otimista para o MVP.

### ADR-004 — Idempotência

Definir escopo da chave, resposta repetida, persistência e tempo de retenção.

## Sinais de arquitetura ruim

- serviço com centenas de linhas e múltiplos motivos de mudança;
- regra duplicada em Controller e Service;
- qualquer módulo acessa qualquer Repository;
- domínio anêmico no qual setters permitem estado impossível;
- anotação transacional usada sem entender a unidade de negócio;
- DTO de entrada reutilizado como entidade;
- pacote shared cresce mais rápido que os módulos;
- microsserviço proposto sem problema operacional medido.

## Como explicar em entrevista

“Usei um monólito modular porque o produto e a equipe são pequenos. Organizei por funcionalidade para manter regras e persistência próximas, com domínio independente do framework. Isso reduz custo operacional agora e preserva limites que podem orientar separação futura se métricas e organização justificarem.”
