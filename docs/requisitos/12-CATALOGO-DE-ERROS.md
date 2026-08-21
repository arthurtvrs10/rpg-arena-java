# Catálogo de erros

Todos usam `application/problem+json`, `traceId`, `timestamp` e `instance`. O mesmo código mantém significado em toda a v1.

| HTTP | Código | Quando usar |
|---:|---|---|
| 400 | VALIDATION_FAILED | formato, obrigatório, tamanho ou combinação estrutural inválida |
| 400 | FORBIDDEN_FIELD | payload tenta definir campo controlado pelo servidor |
| 400 | INVALID_CHARACTER_NAME | nome fora das regras |
| 400 | INVALID_QUANTITY | quantidade fora de 1–99/limite aplicável |
| 401 | INVALID_CREDENTIALS | e-mail/senha inválidos sem enumeração |
| 401 | INVALID_TOKEN | access ausente, expirado, adulterado ou inválido |
| 401 | INVALID_REFRESH_TOKEN | refresh ausente, expirado ou revogado |
| 401 | REFRESH_TOKEN_REUSED | refresh já usado; família revogada |
| 403 | ACCESS_DENIED | papel não permite a operação |
| 403 | ACCOUNT_INACTIVE | conta bloqueada |
| 404 | RESOURCE_NOT_FOUND | inexistente ou privado de outro owner |
| 404 | CHARACTER_NOT_FOUND | alias opcional; baseline prefere RESOURCE_NOT_FOUND |
| 404 | CONTENT_NOT_FOUND | conteúdo administrativo inexistente |
| 409 | EMAIL_ALREADY_IN_USE | e-mail normalizado já cadastrado |
| 409 | CHARACTER_NAME_IN_USE | nome já cadastrado sem diferença de caixa |
| 409 | CHARACTER_LIMIT_REACHED | três personagens ativos |
| 409 | CHARACTER_BUSY | batalha/comando impede a operação |
| 409 | CHARACTER_ARCHIVED | personagem não aceita gameplay |
| 409 | CHARACTER_CLASS_UNAVAILABLE | classe não publicada |
| 409 | INVENTORY_FULL | capacidade insuficiente |
| 409 | ITEM_NOT_EQUIPPABLE | item/tipo/slot incompatível |
| 409 | EQUIPMENT_SLOT_OCCUPIED | usado quando troca automática não se aplica |
| 409 | ITEM_IN_USE | item equipado/bloqueado |
| 409 | ITEM_NOT_USABLE | consumível não permitido |
| 409 | INVENTORY_CONCURRENTLY_MODIFIED | versão obsoleta de inventário/item |
| 409 | BATTLE_NOT_IN_PROGRESS | ação em estado terminal/não iniciado |
| 409 | NOT_YOUR_TURN | ator não possui turno |
| 409 | COMBATANT_DEFEATED | ator/alvo já derrotado |
| 409 | SKILL_NOT_AVAILABLE | habilidade desconhecida, alvo ou regra geral |
| 409 | INSUFFICIENT_RESOURCE | mana insuficiente |
| 409 | SKILL_ON_COOLDOWN | cooldown maior que zero |
| 409 | FLEE_NOT_ALLOWED | chefe/estado proíbe fuga |
| 409 | BATTLE_CONCURRENTLY_MODIFIED | expectedVersion obsoleta |
| 409 | IDEMPOTENCY_CONFLICT | mesma chave com outro corpo |
| 409 | IDEMPOTENCY_IN_PROGRESS | primeiro comando ainda processando |
| 409 | QUEST_REQUIREMENTS_NOT_MET | pré-requisitos não atendidos |
| 409 | QUEST_ALREADY_ACTIVE | linha de missão já ativa |
| 409 | INVALID_QUEST_STATE | transição inválida |
| 409 | CHOICE_NOT_AVAILABLE | opção inexistente/bloqueada |
| 409 | REWARD_ALREADY_GRANTED | chave diferente após recompensa; sem novo efeito |
| 409 | TRAVEL_NOT_ALLOWED | destino sem conexão/restrição |
| 409 | INSUFFICIENT_GOLD | ouro insuficiente |
| 409 | MERCHANT_UNAVAILABLE | comerciante inativo/outro local |
| 409 | STOCK_UNAVAILABLE | estoque insuficiente |
| 409 | STOCK_CONCURRENTLY_MODIFIED | versão do estoque obsoleta |
| 409 | PURCHASE_NOT_ALLOWED | regra de compra não atendida |
| 409 | SALE_NOT_ALLOWED | regra de venda não atendida |
| 409 | CONTENT_NOT_EDITABLE | versão não está em rascunho |
| 409 | PUBLISHED_CONTENT_IMMUTABLE | tentativa de alterar publicado |
| 409 | CONTENT_CODE_IN_USE | código estável já existe |
| 422 | CONTENT_VALIDATION_FAILED | rascunho estruturalmente recebido, mas semanticamente inconsistente |
| 500 | INTERNAL_ERROR | falha inesperada com mensagem pública genérica |

## Exemplo

```json
{
  "type": "https://rpg-arena.dev/problems/not-your-turn",
  "title": "Ação não permitida",
  "status": 409,
  "code": "NOT_YOUR_TURN",
  "detail": "A batalha aguarda outra ação.",
  "instance": "/api/v1/battles/00000000-0000-0000-0000-000000000000/actions",
  "timestamp": "2026-11-10T18:30:00Z",
  "traceId": "01J..."
}
```

Nunca usar a mensagem de exceção do banco como `detail`. Para validação, `errors[]` contém `field`, `code` e `message`.
