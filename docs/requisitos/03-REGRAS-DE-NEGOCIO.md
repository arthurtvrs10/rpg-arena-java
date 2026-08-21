# Regras de negócio

Os códigos abaixo devem aparecer nos testes e, quando aplicável, nos erros da API. Validação de DTO protege formato; estas regras protegem o negócio em qualquer interface.

## Conta, autenticação e sessão

| Código | Regra | Erro estável |
|---|---|---|
| RN-AUT-001 | E-mail é obrigatório, convertido para minúsculas, sem espaços externos e único após normalização. | `EMAIL_ALREADY_IN_USE` |
| RN-AUT-002 | Senha possui 10–72 caracteres e deve conter letra e número; texto puro existe apenas durante a operação de cadastro/login. | `WEAK_PASSWORD` |
| RN-AUT-003 | Nome público possui 3–32 caracteres e não pode ser apenas espaço. | `INVALID_DISPLAY_NAME` |
| RN-AUT-004 | Nova conta nasce `ACTIVE` e `PLAYER`; somente bootstrap controlado cria o primeiro `ADMIN`. | `ROLE_NOT_ALLOWED` |
| RN-AUT-005 | Conta `BLOCKED` não recebe access ou refresh token. | `ACCOUNT_INACTIVE` |
| RN-AUT-006 | Login inválido sempre retorna `INVALID_CREDENTIALS`, sem confirmar existência do e-mail. | `INVALID_CREDENTIALS` |
| RN-AUT-007 | Access token expira em 15 minutos e contém subject UUID, papel, issuer, emissão e expiração. | `INVALID_TOKEN` |
| RN-AUT-008 | Refresh token expira em 7 dias, é armazenado por hash e usado uma única vez. | `INVALID_REFRESH_TOKEN` |
| RN-AUT-009 | Reutilização de refresh token revogado encerra toda a família de sessão. | `REFRESH_TOKEN_REUSED` |
| RN-AUT-010 | Logout revoga o refresh token da sessão; access token expira naturalmente. | — |
| RN-AUT-011 | Identidade efetiva sempre vem do contexto autenticado, nunca de `accountId` no payload. | `ACCESS_DENIED` |
| RN-AUT-012 | Recurso privado pertencente a outra conta responde 404 e não revela metadados. | `RESOURCE_NOT_FOUND` |

## Personagem e atributos

| Código | Regra | Erro estável |
|---|---|---|
| RN-CHR-001 | Nome possui 3–24 caracteres após trim e aceita letras, números, espaço, hífen e apóstrofo. | `INVALID_CHARACTER_NAME` |
| RN-CHR-002 | Nome de personagem é único sem diferenciar maiúsculas/minúsculas. | `CHARACTER_NAME_IN_USE` |
| RN-CHR-003 | Conta pode manter no máximo três personagens `ACTIVE`. | `CHARACTER_LIMIT_REACHED` |
| RN-CHR-004 | Classe precisa estar `PUBLISHED` na criação. | `CHARACTER_CLASS_UNAVAILABLE` |
| RN-CHR-005 | Personagem nasce no nível 1, XP 0, vida/mana máximas, estado `ACTIVE` e local inicial da classe. | — |
| RN-CHR-006 | Atributos base, derivados, nível, XP, ouro, posição e propriedade não são aceitos do cliente. | `FORBIDDEN_FIELD` |
| RN-CHR-007 | Vida fica entre 0 e vida máxima; mana fica entre 0 e mana máxima. | `INVALID_ATTRIBUTE_VALUE` |
| RN-CHR-008 | Cura não ressuscita personagem derrotado durante uma batalha; dano nunca é negativo. | `INVALID_CHARACTER_STATE` |
| RN-CHR-009 | Personagem `ARCHIVED` não inicia missão, viagem, compra ou batalha. | `CHARACTER_ARCHIVED` |
| RN-CHR-010 | Personagem só pode ser arquivado sem batalha ativa e sem comando crítico em processamento. | `CHARACTER_BUSY` |
| RN-CHR-011 | Apenas o proprietário consulta ou altera o personagem. | `RESOURCE_NOT_FOUND` |
| RN-CHR-012 | Atributos derivados são recalculados a partir de base, nível, equipamento e efeitos persistentes; nunca são origem da verdade. | — |

## Progressão e habilidades

| Código | Regra | Erro estável |
|---|---|---|
| RN-PRG-001 | XP concedida é inteira, positiva e não pode ser retirada. | `INVALID_EXPERIENCE` |
| RN-PRG-002 | XP necessária para passar do nível `L` é `100 × L²`. | — |
| RN-PRG-003 | Ao alcançar o limiar, ele é subtraído e o processamento continua enquanto houver XP e nível menor que 50. | — |
| RN-PRG-004 | O nível nunca diminui e não ultrapassa 50. | `LEVEL_LIMIT_REACHED` |
| RN-PRG-005 | No nível 50, XP excedente é descartada e o valor armazenado permanece 0. | — |
| RN-PRG-006 | Subida de nível aplica crescimento da classe e restaura vida/mana máximas. | — |
| RN-PRG-007 | Habilidade é desbloqueada uma única vez ao cumprir classe, nível e pré-requisitos. | `SKILL_NOT_ELIGIBLE` |
| RN-PRG-008 | Habilidade não publicada não pode ser aprendida por nova concessão. | `SKILL_UNAVAILABLE` |

## Inventário, equipamento e consumíveis

| Código | Regra | Erro estável |
|---|---|---|
| RN-INV-001 | Inventário comporta no máximo 40 pilhas; item não empilhável ocupa uma pilha por instância. | `INVENTORY_FULL` |
| RN-INV-002 | Quantidade de pilha fica entre 1 e `maxStack` da versão do item. | `INVALID_ITEM_QUANTITY` |
| RN-INV-003 | Item só pode ser manipulado pelo proprietário do personagem. | `RESOURCE_NOT_FOUND` |
| RN-INV-004 | Item equipado deve existir no inventário, estar `OWNED`, ser equipamento e aceitar o slot. | `ITEM_NOT_EQUIPPABLE` |
| RN-INV-005 | Cada slot comporta exatamente zero ou um item. | `EQUIPMENT_SLOT_OCCUPIED` |
| RN-INV-006 | Equipar troca o item anterior na mesma transação e recalcula atributos. | — |
| RN-INV-007 | Item equipado não pode ser vendido ou consumido. | `ITEM_IN_USE` |
| RN-INV-008 | Consumível precisa estar publicado na versão usada, possuir quantidade e ser permitido no contexto atual. | `ITEM_NOT_USABLE` |
| RN-INV-009 | Consumo remove uma unidade e apaga a pilha ao chegar a zero. | — |
| RN-INV-010 | Loot é calculado por tabela versionada e `RandomSource`; falha de capacidade não concede parte silenciosa. | `INVENTORY_FULL` |
| RN-INV-011 | Atualização concorrente usa versão; uma gravação vence e a outra recebe conflito explícito. | `INVENTORY_CONCURRENTLY_MODIFIED` |

## Combate

### Estados

`CREATED -> IN_PROGRESS -> WON | LOST | FLED | CANCELLED`. Estados terminais não mudam.

### Fórmulas

- Dano básico: `max(1, ataqueDoAtor - defesaDoAlvo)`.
- Dano de habilidade: `max(1, ataqueDoAtor + poderDaHabilidade - defesaDoAlvo)`.
- Defesa: reduz em 40% o próximo dano recebido, arredondado para baixo, mantendo dano mínimo 1.
- Cura: `min(vidaMaxima, vidaAtual + poderDeCura)`.
- Chance de fuga: `clamp(10, 90, 50 + 5 × (velocidadeJogador - velocidadeInimigo))` por cento, usando `RandomSource`.
- Primeiro turno: maior velocidade; empate favorece o personagem.

| Código | Regra | Erro estável |
|---|---|---|
| RN-CBT-001 | Apenas personagem ativo, vivo e sem outra batalha ativa inicia batalha. | `CHARACTER_NOT_ELIGIBLE` |
| RN-CBT-002 | Inimigo e encontro precisam estar publicados e elegíveis para o local/nível. | `ENEMY_UNAVAILABLE` |
| RN-CBT-003 | A batalha guarda snapshot dos atributos e versões de conteúdo; publicação posterior não a altera. | — |
| RN-CBT-004 | Apenas `IN_PROGRESS` recebe ações. | `BATTLE_NOT_IN_PROGRESS` |
| RN-CBT-005 | Somente participante indicado por `currentTurn` age. | `NOT_YOUR_TURN` |
| RN-CBT-006 | Ator e alvo precisam estar vivos no início da ação. | `COMBATANT_DEFEATED` |
| RN-CBT-007 | `BASIC_ATTACK` não custa recurso e usa poder zero. | — |
| RN-CBT-008 | `DEFEND` aplica uma proteção que expira após reduzir o próximo dano ou no fim da batalha. | — |
| RN-CBT-009 | `SKILL` exige habilidade conhecida, alvo válido, mana suficiente e cooldown zero. | `SKILL_NOT_AVAILABLE` |
| RN-CBT-010 | Falha na habilidade não consome mana, item, turno ou cooldown. | — |
| RN-CBT-011 | Cooldowns reduzem uma unidade ao final do turno do proprietário, sem ficar negativos. | — |
| RN-CBT-012 | `USE_ITEM` exige consumível permitido e remove exatamente uma unidade na mesma transação da ação. | `ITEM_NOT_USABLE` |
| RN-CBT-013 | `FLEE` é proibida em batalha de chefe e não concede XP, loot ou vitória. | `FLEE_NOT_ALLOWED` |
| RN-CBT-014 | Vida nunca fica negativa; após chegar a zero, o sistema finaliza antes de trocar o turno. | — |
| RN-CBT-015 | Após ação válida do jogador, a política do inimigo decide e executa no mesmo comando, salvo se a batalha terminou. | — |
| RN-CBT-016 | Cada ação gera evento imutável com número de turno, ator, tipo, valores e instante. | — |
| RN-CBT-017 | `Idempotency-Key` é única por conta, operação e batalha. | `IDEMPOTENCY_CONFLICT` |
| RN-CBT-018 | Mesma chave e mesmo hash devolvem o primeiro resultado; mesma chave e corpo diferente retorna 409. | `IDEMPOTENCY_CONFLICT` |
| RN-CBT-019 | A versão esperada deve ser a atual; versão obsoleta não grava evento. | `BATTLE_CONCURRENTLY_MODIFIED` |
| RN-CBT-020 | XP, loot, missão e ranking decorrentes do resultado são contabilizados uma única vez. | `RESULT_ALREADY_ACCOUNTED` |

## Efeitos de status

| Código | Regra |
|---|---|
| RN-EFF-001 | `POISON` causa dano fixado no snapshot no início do turno por duração configurada. |
| RN-EFF-002 | `BURN` causa dano no fim do turno por duração configurada. |
| RN-EFF-003 | `STUN` consome no máximo um turno e não pode acumular duração no MVP. |
| RN-EFF-004 | Reaplicar o mesmo efeito usa a política da definição: `REFRESH`, `STACK` ou `IGNORE`. |
| RN-EFF-005 | Efeito não continua depois do estado terminal. |

## Missões e narrativa

| Código | Regra | Erro estável |
|---|---|---|
| RN-QST-001 | Somente versão `PUBLISHED` pode gerar nova instância. | `QUEST_UNAVAILABLE` |
| RN-QST-002 | Instância guarda ID e versão da definição aceita. | — |
| RN-QST-003 | Pré-requisitos de nível, local, missão anterior e classe devem ser atendidos no aceite. | `QUEST_REQUIREMENTS_NOT_MET` |
| RN-QST-004 | No máximo uma instância `ACTIVE` da mesma linha de missão por personagem. | `QUEST_ALREADY_ACTIVE` |
| RN-QST-005 | Objetivo avança apenas por evento compatível e identificador de evento ainda não processado. | — |
| RN-QST-006 | Progresso nunca excede a meta do objetivo. | — |
| RN-QST-007 | Missão só fica `COMPLETED` quando todos os objetivos obrigatórios e o nó final estiverem concluídos. | `QUEST_NOT_COMPLETE` |
| RN-QST-008 | Escolha precisa existir no nó atual e cumprir condições. | `CHOICE_NOT_AVAILABLE` |
| RN-QST-009 | Escolha confirmada é imutável e suas consequências são aplicadas atomicamente. | `CHOICE_ALREADY_MADE` |
| RN-QST-010 | Apenas `ACTIVE` pode ser abandonada e somente se `abandonable=true`. | `QUEST_NOT_ABANDONABLE` |
| RN-QST-011 | `COMPLETED`, `FAILED`, `ABANDONED` e `REWARDED` são terminais, exceto `COMPLETED -> REWARDED`. | `INVALID_QUEST_STATE` |
| RN-QST-012 | Recompensa pertence à instância e é concedida uma única vez na mesma transação. | `REWARD_ALREADY_GRANTED` |
| RN-QST-013 | Arquivar definição impede novos aceites, mas não altera instâncias existentes. | — |

## Mundo e viagem

| Código | Regra | Erro estável |
|---|---|---|
| RN-WLD-001 | O local atual e o destino devem estar publicados e ligados por conexão ativa na direção solicitada. | `TRAVEL_NOT_ALLOWED` |
| RN-WLD-002 | Personagem não viaja com batalha ativa, arquivado ou sem cumprir restrição da conexão. | `CHARACTER_BUSY` |
| RN-WLD-003 | Custo de viagem é inteiro e não negativo; não pode deixar ouro negativo. | `INSUFFICIENT_GOLD` |
| RN-WLD-004 | Débito, mudança de posição e registro de viagem são atômicos e idempotentes. | `TRAVEL_CONCURRENTLY_MODIFIED` |
| RN-WLD-005 | Encontros são filtrados por local, nível, estado e peso antes do sorteio. | — |
| RN-WLD-006 | Um sorteio sem opção elegível produz viagem sem encontro, não erro. | — |

## Economia

| Código | Regra | Erro estável |
|---|---|---|
| RN-ECO-001 | Ouro é inteiro entre 0 e `Long.MAX_VALUE`; cálculos usam operações exatas. | `INVALID_GOLD_AMOUNT` |
| RN-ECO-002 | Personagem só negocia com comerciante publicado, ativo e no mesmo local. | `MERCHANT_UNAVAILABLE` |
| RN-ECO-003 | Quantidade de compra/venda fica entre 1 e 99 por comando. | `INVALID_QUANTITY` |
| RN-ECO-004 | Preço efetivo vem do servidor e do snapshot da operação; cliente envia item e quantidade, não preço. | `FORBIDDEN_FIELD` |
| RN-ECO-005 | Compra exige ouro, estoque e capacidade; débito, estoque, inventário e ledger são atômicos. | `PURCHASE_NOT_ALLOWED` |
| RN-ECO-006 | Venda exige posse, item vendável e não equipado; remoção, crédito, estoque e ledger são atômicos. | `SALE_NOT_ALLOWED` |
| RN-ECO-007 | Estoque e ouro nunca ficam negativos, inclusive sob concorrência. | `STOCK_UNAVAILABLE` |
| RN-ECO-008 | A versão do estoque detecta corrida; comprar o último item produz apenas um sucesso. | `STOCK_CONCURRENTLY_MODIFIED` |
| RN-ECO-009 | Compra e venda usam idempotência; repetição não altera saldos novamente. | `IDEMPOTENCY_CONFLICT` |
| RN-ECO-010 | Ajuste administrativo exige motivo de 10–200 caracteres e evento de auditoria. | `ADJUSTMENT_REASON_REQUIRED` |

## Conteúdo administrativo

| Código | Regra | Erro estável |
|---|---|---|
| RN-ADM-001 | Código funcional é único por tipo de conteúdo, em maiúsculas e formato `[A-Z0-9_]{3,50}`. | `CONTENT_CODE_IN_USE` |
| RN-ADM-002 | Nova versão nasce `DRAFT` e pode ser editada somente nesse estado. | `CONTENT_NOT_EDITABLE` |
| RN-ADM-003 | Publicação exige schema válido, referências existentes e ausência de ciclo proibido. | `CONTENT_VALIDATION_FAILED` |
| RN-ADM-004 | Publicação é atômica: nova versão vira ativa e anterior deixa de ser atual sem ser alterada. | — |
| RN-ADM-005 | Versão `PUBLISHED` é imutável; correção gera nova versão. | `PUBLISHED_CONTENT_IMMUTABLE` |
| RN-ADM-006 | Versão `ARCHIVED` não gera novas instâncias, mas permanece consultável por referências históricas. | — |
| RN-ADM-007 | Toda alteração guarda ator, tipo, entidade, versão, instante, operação e resumo sem segredo. | — |
| RN-ADM-008 | `PLAYER` nunca acessa rota administrativa. | `ACCESS_DENIED` |

## Ranking e paginação

| Código | Regra |
|---|---|
| RN-RNK-001 | Apenas vitória/derrota de batalha terminal contabilizada afeta ranking. |
| RN-RNK-002 | Resultado é contabilizado uma única vez por batalha. |
| RN-RNK-003 | Ordem: vitórias desc, derrotas asc, nível desc, `characterId` asc. |
| RN-RNK-004 | Página padrão é 0, tamanho padrão 20 e máximo 100. |
| RN-RNK-005 | Ranking público expõe posição, nome, classe, nível, vitórias e derrotas; nunca conta ou e-mail. |

## Política de idempotência

Comandos críticos exigem cabeçalho `Idempotency-Key` em UUID: ação de batalha, recompensa, viagem com custo, compra, venda e publicação. O escopo é `accountId + método + rota canônica + aggregateId + key`. O servidor persiste hash do corpo, status e resposta. Registros operacionais permanecem por 24 horas; chaves vinculadas a resultado/recompensa permanecem por toda a vida da entidade. Uma requisição ainda em processamento retorna `409 IDEMPOTENCY_IN_PROGRESS` ou aguarda até o limite configurado, decisão que deve permanecer igual em toda a API; para v1.0, será usado retorno 409.

## Política de arredondamento e tempo

- Divisões inteiras arredondam para baixo.
- Nenhum cálculo de jogo usa `double` para moeda.
- Regras recebem `Clock` e `RandomSource` por porta.
- Banco e eventos usam UTC; cliente recebe ISO 8601 com `Z` ou offset.
- Intervalos expiram quando `now >= expiresAt`.

## Política de erros

O código é contrato estável; a mensagem é humana e pode evoluir. Controller não devolve mensagem de SQL, nome de tabela, classe interna ou stack trace. Validação estrutural retorna 400; ausência de autenticação 401; papel proibido 403; recurso privado alheio/inexistente 404; estado, idempotência e concorrência 409; falha inesperada 500 com `traceId`.
