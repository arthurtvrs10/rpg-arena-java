# Contrato da API

## Convenções

- Prefixo: /api/v1.
- Formato: application/json.
- Identificadores: UUID.
- Datas: ISO 8601 com fuso.
- Autenticação: Bearer token.
- Paginação: page, size e sort limitados.
- Idempotência de ação: cabeçalho Idempotency-Key ou requestId obrigatório no corpo; escolha uma abordagem e mantenha.
- Campos desconhecidos: política explícita e testada.
- Entidades JPA nunca fazem parte do contrato.

## Identidade e propriedade

Rotas podem conter characterId ou battleId para identificar o recurso, mas a autorização sempre compara o proprietário persistido com a identidade do token. Nunca aceite accountId/playerId do corpo para decidir quem é o dono.

## Formato de sucesso

Use resposta específica por caso de uso. Não embrulhe tudo em um objeto genérico sem benefício. Retorne apenas dados necessários ao cliente.

## Formato de erro

Estrutura recomendada, alinhada ao conceito de Problem Details:

~~~json
{
  "type": "https://seu-dominio.dev/problems/not-your-turn",
  "title": "Ação não permitida",
  "status": 409,
  "code": "NOT_YOUR_TURN",
  "detail": "A batalha aguarda a ação do oponente.",
  "instance": "/api/v1/battles/...",
  "timestamp": "2026-09-03T14:30:00Z",
  "traceId": "..."
}
~~~

Para validação, acrescente errors com campo e código. Não exponha nome de tabela, SQL, stack trace, token, hash ou classe interna.

## Matriz de status

| Situação | Status | Observação |
|---|---:|---|
| Recurso criado | 201 | Location quando aplicável |
| Consulta válida | 200 | Pode retornar página vazia |
| Operação sem corpo | 204 | Não combinar com JSON |
| Entrada estrutural inválida | 400 | Lista de campos |
| Token ausente/inválido | 401 | Sem revelar detalhes |
| Identidade válida sem permissão | 403 | Use política consistente |
| Recurso inexistente | 404 | Pode ocultar existência de recurso alheio |
| Conflito de regra/estado | 409 | Nome, turno, versão ou transição |
| Semântica processável porém inválida | 422 | Opcional; documentar se usar |
| Limite de requisições | 429 | Apenas se controle existir |
| Falha inesperada | 500 | Mensagem pública genérica + traceId |

## Endpoints e contratos

### POST /auth/register

Entrada:

- email;
- password;
- displayName.

Saída 201:

- accountId;
- displayName;
- createdAt.

Falhas: validação, e-mail em uso.

### POST /auth/login

Entrada: email e password.

Saída:

- accessToken;
- tokenType;
- expiresIn.

Falhas: credenciais inválidas e conta inativa com resposta que não ajuda enumeração.

### POST /characters

Entrada:

- name;
- classCode.

Saída:

- id, name, class;
- level e experience;
- atributos base e derivados;
- createdAt.

Falhas: limite, nome em uso, classe indisponível.

### GET /characters

Retorna somente personagens da identidade autenticada. Não recebe accountId.

### PUT /characters/{id}/equipment/{slot}

Entrada: inventoryItemId.

Saída:

- slot;
- item equipado;
- item anteriormente equipado, quando houver;
- atributos derivados atualizados.

Falhas: personagem não pertencente, item não pertencente, slot incompatível, versão concorrente.

### POST /characters/{id}/missions/{missionId}/attempts

Cria tentativa ACTIVE e retorna seu id, status, requisitos e horário.

### POST /mission-attempts/{id}/complete

Pode exigir Idempotency-Key. Retorna estado e resumo da recompensa. Uma repetição com a mesma chave devolve o resultado anterior; uma chave diferente para tentativa já recompensada não concede novamente.

### POST /characters/{id}/battles

Entrada: enemyCode.

Saída: snapshot inicial, estado, primeiro turno e version.

### POST /battles/{id}/actions

Entrada:

- requestId;
- actionType;
- skillCode quando aplicável;
- expectedVersion, se exposta no contrato.

Saída:

- actionId e turnNumber;
- dano/cura/custo;
- estados dos combatentes;
- próximo turno;
- status da batalha;
- version atual.

Falhas: estado, turno, recurso, cooldown, repetição com conteúdo diferente e modificação concorrente.

### GET /rankings

Parâmetros:

- page padrão 0;
- size padrão 20 e máximo 100;
- classCode opcional;
- ordenação controlada pelo servidor.

Resposta contém conteúdo e metadados de página. Nunca e-mail.

## Idempotência

Defina:

- escopo da chave: identidade + rota + recurso;
- duração de retenção;
- hash do pedido para impedir mesma chave com corpo diferente;
- status de resposta para repetição;
- comportamento quando a primeira chamada ainda está em processamento;
- restrição única no banco.

## Versionamento

Mudança compatível:

- adicionar campo opcional;
- adicionar endpoint;
- adicionar novo código de erro sem alterar significados anteriores.

Mudança incompatível:

- renomear/remover campo;
- trocar tipo;
- mudar semântica ou status esperado.

Não crie v2 durante o mês. Registre a política.

## Checklist por endpoint

- [ ] usuário e resultado;
- [ ] método e rota;
- [ ] autenticação e papel;
- [ ] propriedade;
- [ ] entrada e limites;
- [ ] saída sem dado sensível;
- [ ] cenário feliz;
- [ ] pelo menos dois erros;
- [ ] transação;
- [ ] idempotência;
- [ ] concorrência;
- [ ] OpenAPI;
- [ ] Bruno;
- [ ] teste automatizado proporcional ao risco.
