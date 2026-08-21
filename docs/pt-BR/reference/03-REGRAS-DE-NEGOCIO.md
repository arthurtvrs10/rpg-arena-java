# Regras de negócio

As regras são numeradas para aparecerem em histórias, testes, commits e documentação. Um teste pode se chamar de forma que revele a regra, por exemplo: shouldRejectFourthCharacter_REG_CH_03.

## Conta e identidade

| Código | Regra | Erro esperado |
|---|---|---|
| REG-AU-01 | E-mail é obrigatório, normalizado e único | EMAIL_ALREADY_IN_USE |
| REG-AU-02 | Senha nunca é armazenada ou registrada em texto puro | Falha interna segura |
| REG-AU-03 | Conta inativa não recebe token utilizável | ACCOUNT_INACTIVE |
| REG-AU-04 | Resposta de login inválido não confirma se e-mail existe | INVALID_CREDENTIALS |
| REG-AU-05 | Identidade efetiva vem do contexto autenticado | ACCESS_DENIED |
| REG-AU-06 | PLAYER não executa operação administrativa | ACCESS_DENIED |

## Personagem

| Código | Regra | Erro esperado |
|---|---|---|
| REG-CH-01 | Nome possui 3 a 24 caracteres após trim | INVALID_CHARACTER_NAME |
| REG-CH-02 | Nome é único sem diferenciar caixa | CHARACTER_NAME_IN_USE |
| REG-CH-03 | Uma conta ativa possui no máximo três personagens | CHARACTER_LIMIT_REACHED |
| REG-CH-04 | Classe deve estar ativa | CHARACTER_CLASS_UNAVAILABLE |
| REG-CH-05 | Personagem nasce no nível 1, XP 0 e vivo | Estado inicial fixo |
| REG-CH-06 | XP não é negativa e nível nunca diminui | INVALID_EXPERIENCE |
| REG-CH-07 | Subida de vários níveis em uma recompensa é permitida | Recalcular até limiar seguinte |
| REG-CH-08 | Atributos derivados não são aceitos do cliente | Campo ignorado/rejeitado |
| REG-CH-09 | Somente proprietário consulta ou altera | CHARACTER_NOT_FOUND ou ACCESS_DENIED conforme política |

## Progressão

Fórmula escolhida para o MVP:

XP necessária para ir do nível L ao próximo = 100 × L × L.

Exemplos:

- nível 1 → 2: 100 XP;
- nível 2 → 3: 400 XP adicionais;
- nível 3 → 4: 900 XP adicionais.

Decisão: manter XP acumulada no nível atual, subtraindo o limiar a cada subida. O método de concessão deve processar múltiplas subidas e devolver um resultado com nível anterior, novo nível e XP restante.

## Inventário e equipamento

| Código | Regra | Erro esperado |
|---|---|---|
| REG-IN-01 | Item de inventário pertence a um único personagem | ITEM_NOT_FOUND |
| REG-IN-02 | Só item OWNED pode ser equipado | ITEM_NOT_AVAILABLE |
| REG-IN-03 | Tipo do item precisa aceitar o slot | INCOMPATIBLE_SLOT |
| REG-IN-04 | Cada slot possui no máximo um item | Troca atômica |
| REG-IN-05 | Equipar o mesmo item no mesmo slot é idempotente | Sem alteração duplicada |
| REG-IN-06 | Item equipado não pode ser consumido ou removido | ITEM_EQUIPPED |
| REG-IN-07 | Bônus derivados são recalculados pelo servidor | Cliente não envia total |
| REG-IN-08 | Troca de equipamento ocorre em uma transação | Tudo ou nada |

Slots do MVP: MAIN_HAND, HEAD, CHEST e ACCESSORY.

## Missão

### Estados

~~~mermaid
stateDiagram-v2
    [*] --> ACTIVE
    ACTIVE --> COMPLETED
    ACTIVE --> FAILED
    COMPLETED --> [*]
    FAILED --> [*]
~~~

| Código | Regra | Erro esperado |
|---|---|---|
| REG-MI-01 | Personagem só inicia missão ativa e compatível com seu nível | MISSION_UNAVAILABLE |
| REG-MI-02 | No máximo uma tentativa ACTIVE da mesma missão por personagem | MISSION_ALREADY_ACTIVE |
| REG-MI-03 | Apenas ACTIVE pode concluir ou falhar | INVALID_MISSION_STATE |
| REG-MI-04 | Estado terminal não muda | INVALID_MISSION_STATE |
| REG-MI-05 | Recompensa pertence à tentativa, não à chamada HTTP | Identidade persistida |
| REG-MI-06 | Recompensa é aplicada exatamente uma vez | REWARD_ALREADY_GRANTED ou resposta idempotente |
| REG-MI-07 | Estado e recompensa persistem na mesma transação | Rollback conjunto |

## Batalha

### Estados

~~~mermaid
stateDiagram-v2
    [*] --> CREATED
    CREATED --> IN_PROGRESS
    CREATED --> CANCELLED
    IN_PROGRESS --> FINISHED
    IN_PROGRESS --> CANCELLED
    FINISHED --> [*]
    CANCELLED --> [*]
~~~

### Ações

- BASIC_ATTACK: sem custo e sem cooldown.
- SKILL: custo de mana e cooldown.
- DEFEND: reduz o próximo dano conforme regra simples.

### Fórmula determinística inicial

Dano bruto = ataque do ator + poder da habilidade − defesa do alvo.

Dano aplicado = máximo entre 1 e dano bruto.

Uma porta RandomSource pode fornecer variação crítica posteriormente. Nos testes, ela deve ser substituível por valor previsível.

| Código | Regra | Erro esperado |
|---|---|---|
| REG-BA-01 | Apenas IN_PROGRESS aceita ação | BATTLE_NOT_IN_PROGRESS |
| REG-BA-02 | Somente participante do turno atual age | NOT_YOUR_TURN |
| REG-BA-03 | Ator e alvo precisam estar vivos | COMBATANT_DEFEATED |
| REG-BA-04 | Habilidade precisa pertencer ao ator | SKILL_NOT_OWNED |
| REG-BA-05 | Mana precisa ser suficiente | INSUFFICIENT_RESOURCE |
| REG-BA-06 | Cooldown precisa estar zerado | SKILL_ON_COOLDOWN |
| REG-BA-07 | Pontos de vida nunca ficam negativos | Limitar a zero |
| REG-BA-08 | Ao atingir zero, verificar fim antes de trocar turno | Estado FINISHED |
| REG-BA-09 | requestId é único por batalha | Resposta idempotente |
| REG-BA-10 | Versão impede duas gravações válidas do mesmo turno | BATTLE_CONCURRENTLY_MODIFIED |
| REG-BA-11 | Resultado final é contabilizado uma vez | RESULT_ALREADY_ACCOUNTED |

## Ranking

| Código | Regra |
|---|---|
| REG-RA-01 | Apenas batalhas FINISHED e contabilizadas afetam ranking |
| REG-RA-02 | Ordem: vitórias desc, derrotas asc, nível desc, id asc |
| REG-RA-03 | Resposta pública não contém e-mail, conta ou dados privados |
| REG-RA-04 | Página e tamanho possuem limites definidos |
| REG-RA-05 | Empates permanecem determinísticos |

## Invariantes versus validação de entrada

Validação de entrada verifica forma: campo obrigatório, tamanho, formato e tipo. Invariante protege negócio mesmo quando o caso de uso não veio do HTTP. Limite de personagens, propriedade, transição e recompensa única pertencem ao domínio/aplicação; não podem existir apenas em anotações de DTO ou no Controller.

## Política de erro

Erro de domínio possui código estável. Texto pode evoluir; código é o contrato para cliente e teste. Nunca usar mensagem de exceção do banco como resposta pública.
