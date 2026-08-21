# Sistemas de jogo e conteúdo inicial

Este documento fixa os números da primeira jornada demonstrável. Eles podem ser balanceados depois da `v0.4.0`, mas mudanças devem criar nova versão de conteúdo e atualizar testes.

## Classes iniciais

| Código | HP | Mana | Ataque | Defesa | Velocidade | Crescimento por nível | Kit inicial |
|---|---:|---:|---:|---:|---:|---|---|
| WARRIOR | 120 | 30 | 16 | 12 | 8 | +12 HP, +2 ataque, +2 defesa, +1 mana | Espada de treino, armadura de couro, 2 poções |
| MAGE | 80 | 100 | 22 | 6 | 10 | +7 HP, +3 ataque, +8 mana, +1 defesa | Cajado de aprendiz, manto simples, 2 poções |
| RANGER | 95 | 60 | 19 | 8 | 14 | +9 HP, +2 ataque, +1 defesa, +5 mana | Arco curto, capuz de couro, 2 poções |

O atributo ataque representa poder físico/mágico unificado na 1.0. Separar os dois fica pós-MVP.

## Progressão

XP para sair do nível `L`: `100 × L²`.

| Nível atual | XP para o próximo | XP acumulada total aproximada |
|---:|---:|---:|
| 1 | 100 | 100 |
| 2 | 400 | 500 |
| 3 | 900 | 1.400 |
| 4 | 1.600 | 3.000 |
| 5 | 2.500 | 5.500 |

Cap: nível 50. A versão de demonstração precisa provar apenas níveis 1–5, mas a fórmula e os limites cobrem 1–50.

## Habilidades iniciais

| Código | Classe/nível | Tipo | Custo | Cooldown | Poder/efeito |
|---|---|---|---:|---:|---|
| POWER_STRIKE | WARRIOR 1 | dano | 8 mana | 2 | poder 8 |
| IRON_GUARD | WARRIOR 3 | defesa | 10 mana | 3 | redução 60% do próximo dano |
| ARCANE_BOLT | MAGE 1 | dano | 12 mana | 1 | poder 12 |
| EMBER_MARK | MAGE 3 | efeito | 18 mana | 3 | BURN 4 por 3 turnos |
| QUICK_SHOT | RANGER 1 | dano | 9 mana | 1 | poder 7 |
| TOXIC_ARROW | RANGER 3 | efeito | 16 mana | 3 | POISON 3 por 3 turnos |

Habilidade inicial da classe é concedida na criação. Habilidade de nível 3 é desbloqueada no level up.

## Equipamentos e consumíveis

| Código | Tipo/slot | Stack | Compra | Venda | Bônus/efeito |
|---|---|---:|---:|---:|---|
| TRAINING_SWORD | EQUIPMENT/WEAPON | 1 | 40 | 16 | +3 ataque |
| APPRENTICE_STAFF | EQUIPMENT/WEAPON | 1 | 40 | 16 | +3 ataque, +8 mana |
| SHORT_BOW | EQUIPMENT/WEAPON | 1 | 40 | 16 | +3 ataque, +1 velocidade |
| LEATHER_ARMOR | EQUIPMENT/CHEST | 1 | 35 | 14 | +3 defesa, +8 HP |
| SIMPLE_ROBE | EQUIPMENT/CHEST | 1 | 35 | 14 | +2 defesa, +12 mana |
| LEATHER_HOOD | EQUIPMENT/HEAD | 1 | 25 | 10 | +1 defesa, +1 velocidade |
| HEALTH_POTION | CONSUMABLE | 10 | 15 | 6 | cura 30 HP |
| MANA_POTION | CONSUMABLE | 10 | 18 | 7 | restaura 25 mana |
| WOLF_PELT | MATERIAL | 20 | — | 5 | loot vendável |
| CRYPT_KEY | QUEST | 1 | — | — | item de missão não vendável |
| OBSIDIAN_RING | EQUIPMENT/ACCESSORY | 1 | — | 60 | +4 ataque, +4 defesa |

Raridades: `COMMON`, `UNCOMMON`, `RARE`, `EPIC`. O conteúdo acima é Common, exceto Obsidian Ring (Rare).

## Combate

### Ordem e ciclo

1. Snapshot de personagem/inimigo.
2. Maior velocidade começa; empate favorece jogador.
3. Jogador envia ação quando for seu turno.
4. Sistema valida, aplica e registra.
5. Se não terminou, inimigo escolhe ação pela política versionada.
6. Cooldowns/efeitos avançam nos limites definidos.
7. Repetir até WON, LOST ou FLED.

### Fórmulas

- ataque básico: `max(1, attack - defense)`;
- habilidade: `max(1, attack + skillPower - defense)`;
- defesa comum: 40% de redução no próximo dano;
- cura: limitada ao máximo;
- fuga: `clamp(10, 90, 50 + 5 × diferençaDeVelocidade)`;
- todo arredondamento inteiro é para baixo.

Não existe crítico na primeira versão. Quando adicionado, deve usar `RandomSource`, snapshot e testes determinísticos.

## Inimigos iniciais

| Código | Nível | HP | Ataque | Defesa | Vel. | XP | Loot |
|---|---:|---:|---:|---:|---:|---:|---|
| GREY_WOLF | 1 | 55 | 12 | 4 | 12 | 45 | 70% 1 Wolf Pelt; 15% Health Potion |
| FOREST_BANDIT | 2 | 80 | 16 | 7 | 9 | 80 | 60% 8–15 ouro; 20% Health Potion |
| CRYPT_GUARDIAN | 3 | 150 | 22 | 12 | 7 | 180 | 100% Crypt Key; 10% Obsidian Ring |

Política inicial: usar skill se disponível e mana suficiente; senão ataque básico. Grey Wolf não possui skill; Bandit usa Power Strike; Guardian é boss e não permite fuga.

## Mundo inicial

| Código | Região | Tipo | Seguro | Conexões de saída |
|---|---|---|:---:|---|
| VILA_DE_ASTER | VALE_DE_ASTER | vila | sim | FLORESTA_SUSSURRANTE (0 ouro) |
| FLORESTA_SUSSURRANTE | VALE_DE_ASTER | exploração | não | VILA_DE_ASTER (0), CRIPTA_RUINADA (10) |
| CRIPTA_RUINADA | VALE_DE_ASTER | masmorra | não | FLORESTA_SUSSURRANTE (10) |
| ARENA_DE_OBSIDIANA | VALE_DE_ASTER | arena | sim | VILA_DE_ASTER (5) |

Para permitir ida da vila à arena, publicar também a conexão VILA_DE_ASTER → ARENA_DE_OBSIDIANA. Conexões são direcionadas e cada direção é explícita.

### Encontros

- Vila e Arena: nenhum encontro aleatório.
- Floresta, nível 1–2: Grey Wolf peso 70; Forest Bandit peso 30; chance explícita de nenhum encontro peso 20.
- Cripta, nível 3+: Crypt Guardian em encontro de missão; não aleatório comum.

## Comerciante inicial

**Mara, a Intendente** (`MARA_QUARTERMASTER`) em `VILA_DE_ASTER`.

| Item | Estoque inicial | Preço de compra | Preço de venda pelo jogador |
|---|---:|---:|---:|
| HEALTH_POTION | 20 | 15 | 6 |
| MANA_POTION | 15 | 18 | 7 |
| TRAINING_SWORD | 2 | 40 | 16 |
| LEATHER_ARMOR | 2 | 35 | 14 |

O comerciante compra Wolf Pelt por 5. Preço sempre vem do servidor e fica registrado no ledger.

## Missão principal: Ecos da Floresta

**Código:** `ECOS_DA_FLORESTA`  
**Nível mínimo:** 1  
**Local de aceite:** Vila de Aster  
**Abandonável:** sim, antes da escolha final.

### Objetivos

1. Viajar para a Floresta Sussurrante.
2. Vencer um Grey Wolf.
3. Obter uma Wolf Pelt.
4. Voltar à Vila de Aster.
5. Escolher entregar a pele a Mara ou ao Caçador Errante.

### Ramificações

| Escolha | Condição | Efeito | Recompensa final |
|---|---|---|---|
| AJUDAR_MARA | possuir 1 Wolf Pelt | remove pele; flag `MARA_TRUSTED` | 120 XP, 30 ouro, 2 Health Potions |
| AJUDAR_CACADOR | possuir 1 Wolf Pelt | remove pele; flag `HUNTER_TRUSTED` | 150 XP, 15 ouro, habilidade/passivo narrativo futuro; na 1.0 concede 1 Mana Potion |

Após a escolha, a outra opção fica permanentemente indisponível nessa instância. Recompensa é resgatada por comando separado e uma única vez.

## Missão secundária: Chave da Cripta

Desbloqueada após nível 3 e `MARA_TRUSTED` ou `HUNTER_TRUSTED`. Objetivos: viajar à cripta, derrotar o Crypt Guardian, obter Crypt Key e retornar. Recompensa: 400 XP, 100 ouro e Obsidian Ring garantido se a tabela de loot não o concedeu; nunca duplicar o anel.

## Ranking

Campos públicos: posição, nome do personagem, classe, nível, vitórias e derrotas. Score informativo: `wins × 100 - losses × 25 + level × 10`; a ordenação oficial continua vitórias desc, derrotas asc, nível desc, UUID asc.

## Seed mínimo de demonstração

- 3 classes;
- 6 habilidades;
- 11 itens;
- 3 inimigos;
- 1 região e 4 locais;
- 6 conexões direcionadas;
- 2 tabelas/encontros;
- 1 comerciante e 4 estoques;
- 2 missões, sendo uma ramificada;
- 1 conta ADMIN criada apenas por variável/bootstrap seguro em ambiente local.

## Critério de balanceamento

A jornada principal deve ser completável com qualquer classe sem grind obrigatório. Teste/simulação verifica que cada classe vence Grey Wolf usando ação válida e ao menos uma estratégia. Balanceamento não pode alterar regras de integridade, somente versões de conteúdo.
