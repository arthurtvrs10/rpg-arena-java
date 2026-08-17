# RPG Arena API

API REST de um RPG por turnos construída para demonstrar desenvolvimento backend com Java, Spring Boot, PostgreSQL, segurança, consistência transacional, concorrência, testes e entrega automatizada.

## O que o sistema faz

- cadastro e autenticação de jogadores;
- criação e progressão de personagens;
- inventário com equipamento por slots;
- missões com recompensas idempotentes;
- batalhas PvE por turnos;
- controle de concorrência nas ações;
- ranking paginado;
- administração de catálogos;
- documentação OpenAPI, healthcheck e logs.

## Stack

- Java 21;
- Spring Boot;
- Spring Web, Validation, Security e Data JPA;
- PostgreSQL e Flyway;
- JUnit, Mockito, Spring Boot Test e Testcontainers;
- Bruno;
- Docker e Docker Compose;
- GitHub Actions;
- OpenAPI.

## Arquitetura

O projeto usa monólito modular e organização por funcionalidade. Cada módulo separa API, aplicação, domínio e infraestrutura sem criar microsserviços prematuros.

~~~mermaid
flowchart TD
    C["Cliente / Bruno"] --> API["REST API"]
    API --> MOD["Módulos de negócio"]
    MOD --> DB["PostgreSQL"]
    MOD --> OBS["Logs e métricas"]
~~~

Módulos principais: auth, player, character, inventory, mission, battle e ranking.

## Decisões de projeto

- identidade é obtida do token, não de playerId confiado ao cliente;
- regras de combate são Java puro e não dependem do Spring;
- missão e recompensa compartilham uma transação;
- ações repetidas usam chave de idempotência;
- batalha usa optimistic locking;
- ranking é uma projeção de leitura;
- PostgreSQL real é usado nos testes de persistência críticos;
- o MVP permanece monólito modular.

As decisões completas ficam em docs/adr.

## Pré-requisitos

- Java 21;
- Docker com Docker Compose;
- Git;
- Bruno para executar a coleção.

## Execução local

1. Clone o repositório.
2. Copie .env.example para .env e preencha apenas valores locais.
3. Suba o PostgreSQL:

~~~bash
docker compose up -d postgres
~~~

4. Execute testes:

~~~bash
./mvnw verify
~~~

5. Inicie a aplicação:

~~~bash
./mvnw spring-boot:run
~~~

6. Confirme o healthcheck e abra a documentação indicada pelo projeto.

Para executar tudo em containers:

~~~bash
docker compose up --build
~~~

## Configuração

| Variável | Obrigatória | Descrição |
|---|---|---|
| DB_URL | Sim | URL JDBC do PostgreSQL |
| DB_USERNAME | Sim | Usuário da aplicação |
| DB_PASSWORD | Sim | Senha da aplicação |
| JWT_SECRET | Sim | Segredo longo fora do repositório |
| JWT_EXPIRATION | Não | Validade configurável do token |
| SPRING_PROFILES_ACTIVE | Não | Perfil de execução |

Nenhum segredo real deve ser versionado.

## Testes

~~~bash
./mvnw test
./mvnw verify
~~~

A estratégia inclui:

- testes unitários das regras e máquinas de estado;
- testes de aplicação para casos de uso;
- testes de integração com PostgreSQL via Testcontainers;
- testes de segurança e propriedade;
- cenários de contrato e fluxo no Bruno.

## Fluxo demonstrável

1. cadastrar jogador;
2. autenticar;
3. criar personagem;
4. equipar item;
5. iniciar e concluir missão;
6. verificar recompensa única;
7. iniciar batalha;
8. executar ações até o encerramento;
9. consultar ranking;
10. tentar acessar recurso de outro jogador e receber rejeição.

## Documentação

- Escopo do produto: docs/PRODUCT-SCOPE.md
- Contrato da API: docs/API.md
- Modelo de domínio: docs/DOMAIN.md
- Decisões: docs/adr
- Coleção executável: bruno
- Guia de contribuição: CONTRIBUTING.md

## Roadmap

- 1.0: MVP PvE, ranking e qualidade de entrega;
- 1.1: histórico e replay de batalha;
- 1.2: eventos de domínio e outbox;
- 2.0: PvP assíncrono, somente após validar o modelo.

## Estado

Projeto em desenvolvimento orientado por quatro sprints. Consulte o quadro do repositório e o changelog para o incremento atual.

## Autor

Substitua esta seção por nome, LinkedIn, e-mail profissional e uma frase objetiva sobre sua busca por oportunidades backend Java.
