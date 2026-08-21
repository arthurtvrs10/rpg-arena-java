# Casos de uso

## Convenções

- O ator autenticado nunca informa o proprietário.
- Toda pré-condição também deve ser validada no servidor.
- Fluxos críticos recebem `Idempotency-Key` e transação conforme as regras.
- “Sem alteração” significa rollback completo e ausência de evento de sucesso.

## Mapa

| ID | Caso de uso | Ator | Resultado |
|---|---|---|---|
| UC-01 | Cadastrar conta | Visitante | conta PLAYER ativa |
| UC-02 | Autenticar | Visitante | access e refresh tokens |
| UC-03 | Renovar ou encerrar sessão | Jogador/Admin | sessão rotacionada ou revogada |
| UC-04 | Criar personagem | Jogador | personagem e kit inicial |
| UC-05 | Consultar/arquivar personagem | Jogador | recurso próprio retornado/arquivado |
| UC-06 | Equipar ou desequipar | Jogador | equipamento e atributos consistentes |
| UC-07 | Consumir item | Jogador | efeito aplicado uma vez |
| UC-08 | Aceitar missão | Jogador | instância ligada à versão |
| UC-09 | Avançar narrativa | Jogador | escolha e consequências persistidas |
| UC-10 | Viajar | Jogador | posição/custo/encontro atualizados |
| UC-11 | Iniciar batalha | Jogador | batalha com snapshot e turno |
| UC-12 | Executar ação | Jogador | turno e estado atualizados |
| UC-13 | Finalizar resultado de batalha | Sistema | XP, loot, missão e ranking uma vez |
| UC-14 | Resgatar recompensa de missão | Jogador | recompensa única |
| UC-15 | Comprar item | Jogador | ouro, estoque e inventário atualizados |
| UC-16 | Vender item | Jogador | item, ouro, estoque e ledger atualizados |
| UC-17 | Consultar ranking | Público | página sem dados privados |
| UC-18 | Publicar conteúdo | Admin | nova versão imutável e auditada |
| UC-19 | Bloquear conta | Admin | sessões revogadas e acesso impedido |

## UC-01 — Cadastrar conta

**Ator:** Visitante.  
**Entrada:** `email`, `password`, `displayName`.  
**Pré-condição:** nenhuma sessão necessária.  
**Pós-condição:** conta `ACTIVE/PLAYER`, sem sessão criada automaticamente.

### Fluxo principal

1. Visitante envia cadastro.
2. Sistema valida formato e força allowlist.
3. Sistema normaliza e-mail e verifica unicidade.
4. Sistema codifica a senha.
5. Sistema cria conta, perfil e auditoria na mesma transação.
6. Sistema responde 201 sem senha/hash.

### Alternativas

- E-mail existente: 409 `EMAIL_ALREADY_IN_USE`.
- Senha fraca ou campo inválido: 400 com violações.
- Campo proibido como `role`: 400 `FORBIDDEN_FIELD`.

## UC-02 — Autenticar

**Entrada:** `email`, `password`.  
**Pós-condição:** família de sessão e refresh hash persistidos; tokens emitidos.

1. Sistema normaliza o e-mail.
2. Valida credenciais sem revelar qual parte falhou.
3. Confirma conta ativa.
4. Cria família de sessão.
5. Emite access de 15 minutos e refresh de 7 dias.
6. Registra evento de login sem token.

Falhas: 401 `INVALID_CREDENTIALS`; 403 `ACCOUNT_INACTIVE`; 429 apenas quando rate limiting estiver implementado.

## UC-03 — Renovar ou encerrar sessão

### Refresh

1. Cliente envia refresh token.
2. Sistema calcula hash, localiza token e valida expiração/estado.
3. Se já usado, revoga família e retorna 401 `REFRESH_TOKEN_REUSED`.
4. Caso válido, marca token usado e cria sucessor na mesma transação.
5. Retorna novo par.

### Logout

1. Cliente envia refresh atual autenticado.
2. Sistema revoga token/família conforme contrato.
3. Repetição retorna 204 sem efeito adicional.

## UC-04 — Criar personagem

**Ator:** Jogador.  
**Entrada:** `name`, `classCode`.  
**Pré-condições:** conta ativa; classe publicada; menos de três personagens ativos.  
**Pós-condição:** personagem nível 1 no local inicial, kit e habilidades iniciais concedidos atomicamente.

1. Obtém accountId do token.
2. Valida nome e classe.
3. Bloqueia/serializa a decisão de limite de forma definida pela implementação.
4. Cria personagem e stats.
5. Concede kit inicial respeitando inventário.
6. Posiciona no local inicial.
7. Persiste tudo na mesma transação e responde 201.

Falhas: limite, nome usado, classe indisponível ou conflito concorrente; nenhuma criação parcial.

## UC-05 — Consultar ou arquivar personagem

Listagem consulta por proprietário autenticado e paginação. Detalhe busca por `id + owner`; inexistente ou alheio retorna 404 idêntico. Arquivamento valida ausência de batalha e comando pendente, muda estado para `ARCHIVED` e preserva histórico. Não existe exclusão física pela API.

## UC-06 — Equipar ou desequipar

**Entrada para equipar:** `characterId`, `slot`, `inventoryEntryId`, `expectedVersion`.

1. Busca personagem e entrada pelo proprietário.
2. Valida estados, tipo, slot e versão.
3. Move item anterior para `OWNED` quando houver.
4. Marca novo item `EQUIPPED` e ocupa o slot.
5. Recalcula atributos derivados.
6. Persiste uma única transação e retorna estado atualizado.

Conflito, item alheio ou slot incompatível não produzem alteração parcial. Desequipar executa o fluxo inverso.

## UC-07 — Consumir item

1. Valida propriedade, quantidade, contexto e versão do item.
2. Calcula o efeito sem alterar estado.
3. Aplica efeito e reduz quantidade na mesma transação.
4. Remove a pilha ao chegar a zero.
5. Registra evento e devolve estado atualizado.

Se o alvo já estiver no máximo e o item proibir desperdício, retorna `ITEM_NOT_USABLE` sem consumo.

## UC-08 — Aceitar missão

1. Lista somente versões publicadas e visíveis.
2. Valida nível, classe, local, cadeia e instância existente.
3. Copia ID/versão e estado inicial dos objetivos.
4. Cria instância `ACTIVE` e primeiro nó narrativo.
5. Retorna objetivos e próximo passo.

Arquivamento posterior da definição não muda a instância.

## UC-09 — Avançar narrativa

**Entrada:** `questInstanceId`, `choiceCode`, `Idempotency-Key`.

1. Busca instância própria e ativa.
2. Valida nó atual, opção e condições.
3. Confere idempotência.
4. Persiste escolha imutável.
5. Aplica flags, itens, ouro, objetivos e próximo nó atomicamente.
6. Avalia conclusão/falha e retorna estado.

Mesma chave e corpo retornam o resultado anterior; outra escolha no mesmo nó retorna conflito.

## UC-10 — Viajar

**Entrada:** `characterId`, `destinationCode`, `Idempotency-Key`, `expectedVersion`.

1. Busca personagem próprio e posição.
2. Impede viagem em batalha/estado inválido.
3. Localiza conexão ativa origem→destino e valida restrições.
4. Valida ouro e versão.
5. Debita custo, atualiza posição e registra viagem.
6. Filtra e sorteia encontro com `RandomSource`.
7. Retorna destino e, quando houver, dados necessários para iniciar encontro.

Não existe conexão implícita inversa. Falha em qualquer passo mantém posição e ouro.

## UC-11 — Iniciar batalha

**Entrada:** personagem e referência de encontro/inimigo elegível.

1. Valida proprietário, estado, posição e ausência de batalha ativa.
2. Valida inimigo publicado ou encontro emitido pela viagem.
3. Cria snapshots de personagem, inimigo, habilidades e regras relevantes.
4. Calcula primeiro turno por velocidade.
5. Persiste batalha `IN_PROGRESS`, versão 0 e evento inicial.
6. Retorna estado completo consumível pelo cliente.

## UC-12 — Executar ação de batalha

**Entrada:** ação, alvo/código opcional, `expectedVersion` e `Idempotency-Key`.

1. Busca batalha própria em andamento.
2. Resolve idempotência; repetição igual encerra com resposta anterior.
3. Confere versão e turno.
4. Valida ação sem alterar estado.
5. Calcula resultado e aplica evento do jogador.
6. Verifica estado terminal.
7. Se continuar, executa política do inimigo e verifica novamente.
8. Atualiza cooldowns, efeitos, turno e versão.
9. Persiste eventos e estado em uma transação.
10. Se terminal, chama contabilização idempotente do resultado.

Falhas de validação não consomem turno ou recurso. Conflito concorrente retorna 409 com a versão atual permitida pelo contrato.

## UC-13 — Contabilizar resultado

Disparado quando batalha entra em estado terminal.

1. Confere `resultAccountedAt`; se preenchido, encerra sem efeito.
2. Para vitória, calcula XP e loot pelo snapshot.
3. Aplica progressão e inventário.
4. Publica eventos de missão usando IDs idempotentes.
5. Atualiza projeção de ranking.
6. Marca resultado contabilizado.
7. Confirma tudo na mesma transação ou estratégia outbox documentada; v1.0 usa mesma transação.

Fuga e cancelamento não concedem vitória, XP ou loot.

## UC-14 — Resgatar recompensa de missão

1. Busca instância própria `COMPLETED`.
2. Resolve idempotência e verifica ausência de `rewardGrantedAt`.
3. Valida capacidade para recompensas de item; política v1.0 rejeita resgate inteiro se não couber.
4. Aplica XP, ouro, itens, habilidades/flags e status `REWARDED`.
5. Persiste uma transação e retorna resumo.

Repetição devolve o resumo original; chave diferente após recompensa não concede novamente.

## UC-15 — Comprar item

1. Valida personagem próprio e comerciante no mesmo local.
2. Valida item, quantidade, preço vigente, ouro, estoque e inventário.
3. Resolve idempotência.
4. Usa versão/lock documentado no estoque.
5. Debita ouro, reduz estoque, adiciona item e grava ledger.
6. Confirma tudo e retorna saldos.

Sob duas compras do último item, somente uma confirma. A outra recebe 409 sem débito.

## UC-16 — Vender item

1. Valida personagem, comerciante, posse, quantidade e item vendável/não equipado.
2. Calcula preço de compra pelo servidor.
3. Resolve idempotência e versões.
4. Remove quantidade, credita ouro, adiciona estoque e registra ledger atomicamente.
5. Retorna saldos e transação.

## UC-17 — Consultar ranking

Recebe `page`, `size` e `classCode` opcional. Normaliza limites, aplica ordenação fixa e devolve metadados da página. A consulta usa somente projeção e campos públicos. Página além do fim retorna conteúdo vazio com 200.

## UC-18 — Publicar conteúdo

**Ator:** Admin.  
**Entrada:** tipo, código, versão rascunho, `Idempotency-Key`.

1. Autoriza `ADMIN`.
2. Carrega rascunho e grafo de referências.
3. Executa validações estruturais e semânticas completas.
4. Se houver erro, retorna todos os achados conhecidos com caminhos; nada é publicado.
5. Confere idempotência e versão.
6. Marca a versão como publicada e atual, mantendo a anterior histórica.
7. Registra auditoria.
8. Retorna conteúdo imutável publicado.

## UC-19 — Bloquear conta

1. Admin informa conta e motivo.
2. Sistema impede autobloqueio do último administrador ativo.
3. Muda conta para `BLOCKED`, revoga famílias de sessão e registra auditoria.
4. Access tokens existentes passam a falhar por verificação de estado na política definida.
5. Repetição sobre conta bloqueada é idempotente quando o motivo não muda.

## Checklist de implementação por caso

- [ ] comando/consulta e DTO de entrada definidos;
- [ ] papel e ownership definidos;
- [ ] regras citadas no código/teste;
- [ ] portas e limite transacional definidos;
- [ ] idempotência/concorrência tratadas quando marcadas;
- [ ] erros mapeados para Problem Details;
- [ ] cenário feliz, alternativo e limite testados;
- [ ] OpenAPI e Bruno atualizados;
- [ ] evidência ligada à issue e PR.
