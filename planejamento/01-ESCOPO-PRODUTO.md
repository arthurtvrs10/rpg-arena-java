# Escopo do produto - RPG Arena

## Metadados do repositório

- **Repository name:** rpg-arena-java
- **Description:** Open-source turn-based RPG backend built with Java 21 and Spring Boot to practice domain modeling, REST APIs, PostgreSQL, security, testing, Docker, and software architecture.
- **Visibility:** Public
- **License:** MIT
- **Topics:** java, spring-boot, postgresql, ddd, rest-api, spring-security, jwt, docker, junit, testcontainers, open-source, rpg, turn-based-game, backend, software-architecture
- **Package base:** `io.github.arthurtvrs10.rpgarena`

## Visão

Backend de um RPG por turnos, open source, criado para demonstrar engenharia de software aplicada: regras de domínio, persistência, API, segurança, testes, operações e entrega.

## Atores

- **PLAYER:** administra a própria conta e os próprios personagens.
- **ADMIN:** gerencia catálogo, mundo, NPCs, missões e publicação de conteúdo.
- **CONTRIBUTOR:** contribui por issues e pull requests; não possui papel dentro do jogo.

## Funcionalidades da versão 1.0

1. Cadastro, login, refresh, logout, bloqueio e papéis.
2. Criação de personagem com classe, atributos, vida, mana, nível e XP.
3. Combate por turnos com ataque, defesa, habilidade, item, efeitos e fuga.
4. Inventário, pilhas, equipamento, consumíveis, loot e restrições.
5. Progressão, level up, habilidades, cooldown e eventos de domínio.
6. Missões, objetivos, máquina de estados, recompensas e idempotência.
7. Mundo em grafo, viagens, encontros e posição persistente.
8. NPCs, comerciantes, estoque, compra, venda e concorrência.
9. Missões ramificadas, diálogo, escolhas e consequências versionadas.
10. API administrativa para conteúdo em rascunho, publicado e arquivado.
11. OpenAPI, Bruno, logs, métricas, healthchecks, Docker e deploy.

## Fora do escopo da versão 1.0

- Interface gráfica, aplicativo mobile ou frontend completo.
- Multiplayer em tempo real, PvP e chat.
- Microserviços, Kafka, Kubernetes e service mesh.
- Pagamentos, marketplace e monetização.
- IA generativa dentro do jogo.
- Escala para milhões de jogadores.

## Regras críticas

- Jogador só acessa personagens próprios.
- Batalha respeita turno, estado, custo e idempotência.
- Recompensa de missão só é aplicada uma vez.
- Compra/venda nunca deixa moeda, estoque ou inventário parcialmente atualizados.
- Conteúdo publicado é versionado; instâncias antigas não mudam silenciosamente.
- Senhas, tokens e segredos nunca aparecem em respostas, logs ou Git.

## Modelo de dados mínimo

| Grupo | Tabelas principais |
|---|---|
| Conta | account, refresh_token |
| Personagem | character, character_stats |
| Combate | battle, battle_participant, battle_event |
| Inventário | item_definition, inventory_entry, equipment |
| Progressão | skill_definition, character_skill |
| Missões | quest_definition, quest_instance, quest_objective_progress |
| Mundo | region, location, location_edge, character_location |
| Economia | merchant, merchant_stock, economy_transaction |
| Operação | audit_event |

## Endpoints mínimos

| Área | Endpoints |
|---|---|
| Auth | POST /auth/register, /login, /refresh, /logout |
| Character | POST/GET /characters, GET/PATCH /characters/{id} |
| Inventory | GET /characters/{id}/inventory, POST /equip, /unequip, /consume |
| Battle | POST /battles, POST /battles/{id}/actions, GET /battles/{id} |
| Quest | GET /quests, POST /quests/{id}/accept, /abandon, /claim |
| World | GET /world/locations, POST /characters/{id}/travel |
| Economy | GET /merchants/{id}, POST /buy, /sell |
| Admin | CRUD /admin/items, /quests, /locations, /merchants e POST /publish |

## Critério de produto pronto

A versão 1.0 está pronta quando um usuário externo consegue executar ou acessar a API, criar conta e personagem, concluir a jornada principal, rodar testes, entender decisões e contribuir seguindo apenas o repositório.
