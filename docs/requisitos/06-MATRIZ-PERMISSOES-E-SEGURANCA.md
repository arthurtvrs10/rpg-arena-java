# Matriz de permissões e segurança

## Princípios

1. Autenticação prova identidade; autorização decide papel e propriedade.
2. Todo dado do cliente é não confiável, inclusive IDs, versões, preço, dano e papel.
3. Recursos privados são buscados por `resourceId + authenticatedAccountId` ou verificados no caso de uso.
4. `ADMIN` gerencia conteúdo; não recebe acesso automático ao progresso privado.
5. O sistema retorna 404 para recurso privado inexistente ou de outro proprietário.

## Matriz de acesso

| Capacidade | Público | PLAYER | ADMIN | Ownership/condição |
|---|:---:|:---:|:---:|---|
| Registrar e autenticar | Sim | Sim | Sim | nenhuma |
| Refresh/logout | Não | Sim | Sim | sessão própria |
| Consultar/editar perfil | Não | Sim | Sim | próprio |
| Criar/listar personagem | Não | Sim | Não por padrão | conta própria |
| Detalhar/arquivar personagem | Não | Sim | Não por padrão | personagem próprio |
| Inventário/equipamento | Não | Sim | Não | personagem e item próprios |
| Missões e narrativa | Não | Sim | Não | instância própria |
| Viagem e mundo público | Não | Sim | Não | personagem próprio; conteúdo publicado |
| Batalha e ações | Não | Sim | Não | batalha/personagem próprios |
| Comércio | Não | Sim | Não | personagem próprio e mesmo local |
| Ranking | Sim | Sim | Sim | somente campos públicos |
| Conteúdo em rascunho | Não | Não | Sim | papel ADMIN |
| Publicar/arquivar conteúdo | Não | Não | Sim | papel ADMIN e auditoria |
| Bloquear conta | Não | Não | Sim | não bloquear último admin ativo |
| Health liveness | Sim | Sim | Sim | sem detalhes sensíveis |
| Health readiness/métricas | Configurável | Não | Não | rede/plataforma autorizada |

## Matriz allow/deny obrigatória

Cada linha vira teste automatizado.

| ID | Cenário | Resultado |
|---|---|---|
| SEC-T01 | sem token em endpoint privado | 401 |
| SEC-T02 | token expirado, adulterado ou issuer inválido | 401 |
| SEC-T03 | conta bloqueada com token previamente válido | 401/403 conforme filtro documentado; v1.0 usa 403 `ACCOUNT_INACTIVE` |
| SEC-T04 | PLAYER chama rota `/admin/**` | 403 |
| SEC-T05 | PLAYER A consulta personagem de B | 404 |
| SEC-T06 | PLAYER A equipa item de B | 404 |
| SEC-T07 | PLAYER A consulta ou age em batalha de B | 404 |
| SEC-T08 | PLAYER A avança missão de B | 404 |
| SEC-T09 | payload tenta definir `role`, `ownerId`, `level`, `gold`, `damage` ou `price` | 400 |
| SEC-T10 | ranking contém e-mail/accountId | teste falha |
| SEC-T11 | erro 500 contém SQL, stack ou classe interna | teste falha |
| SEC-T12 | log contém Authorization, senha, hash ou refresh token | teste falha |

## Modelo de ameaças

| Ameaça | Exemplo | Controle | Evidência |
|---|---|---|---|
| BOLA/IDOR | trocar `characterId` | identidade do token + busca por owner + 404 | SEC-T05–T08 |
| Autenticação quebrada | token forjado/expirado | algoritmo fixo, issuer, expiração e status da conta | SEC-T01–T03 |
| Reutilização de sessão | refresh roubado usado duas vezes | rotação, hash e revogação de família | testes US-AUT-02 |
| Mass assignment | enviar papel, XP ou preço | DTO allowlist e falha para campos desconhecidos | SEC-T09 |
| Função admin exposta | PLAYER publica item | RBAC por rota e método | SEC-T04 |
| Concorrência | dois ataques/duas compras | versão, unique constraint e transação | BDD CBT/ECO |
| Replay | repetir compra/recompensa | Idempotency-Key, hash do corpo e resultado persistido | testes de repetição |
| Injeção | filtros/ordenação livres | parâmetros tipados, consultas parametrizadas, sort allowlist | testes API |
| Exposição de dados | ranking inclui e-mail | DTO público específico | SEC-T10 |
| Misconfiguration | actuator/stack aberto | exposição mínima por perfil e erro seguro | SEC-T11 |
| Logs sensíveis | token no logger | filtro de redação e revisão automatizada | SEC-T12 |
| Dependência vulnerável | biblioteca/imagem antiga | atualização deliberada, Dependabot e scanner | pipeline de release |
| Abuso de recursos | page size enorme/spam de login | limites, timeout e rate limit quando implementado | testes de limite |

## JWT e sessão

- Algoritmo permitido é configurado explicitamente; não aceitar `none` ou algoritmo vindo do token.
- Subject é `accountId` UUID; não usar e-mail como identidade estável.
- Claims mínimas: `sub`, `role`, `iss`, `iat`, `exp`, `jti`.
- Access: 15 minutos. Refresh: 7 dias.
- Refresh é valor aleatório opaco, não JWT obrigatório; somente hash é persistido.
- Logout e bloqueio revogam refresh/família.
- O segredo/chave vem de variável de ambiente e possui validação de tamanho no startup.
- Relógio é injetável nos testes.

## Cabeçalhos e transporte

- Produção somente HTTPS.
- `Authorization: Bearer <token>` em rotas privadas.
- `Idempotency-Key: <UUID>` nos comandos críticos.
- `X-Correlation-ID` pode ser aceito se válido; o servidor gera um quando ausente e sempre o devolve.
- CORS deve listar origens explícitas quando existir cliente web; não usar `*` com credenciais.
- Respostas sensíveis usam `Cache-Control: no-store`.

## Dados e privacidade

Dados pessoais mínimos: e-mail e nome público. Não armazenar data de nascimento, telefone ou endereço. Ranking usa somente nome do personagem e estatísticas do jogo. Auditoria registra IDs técnicos e operação, não payload completo. Retenção inicial: auditoria 90 dias no ambiente publicado; logs operacionais 30 dias; refresh expirado pode ser removido após janela de detecção definida.

## Checklist antes de cada release

- [ ] nenhum segredo em arquivos, histórico ou imagem;
- [ ] matriz allow/deny verde;
- [ ] dependências e container revisados;
- [ ] endpoints Actuator mínimos;
- [ ] erros não expõem detalhes internos;
- [ ] paginação e corpo possuem limites;
- [ ] idempotência e concorrência têm teste;
- [ ] backup e rollback foram ensaiados para v1.0;
- [ ] riscos residuais constam em issue e release notes.
