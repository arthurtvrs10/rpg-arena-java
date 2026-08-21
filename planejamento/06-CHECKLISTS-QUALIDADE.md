# Checklists de qualidade e entrega

## Pull request

- [ ] Issue e critério de aceite vinculados.
- [ ] Mudança pequena e nomeada.
- [ ] Teste de regra/erro/limite.
- [ ] Sem entidade JPA no contrato HTTP.
- [ ] Sem segredo, token ou dado pessoal.
- [ ] Migration nova; nenhuma migration aplicada foi editada.
- [ ] Bruno/OpenAPI/docs atualizados.
- [ ] CI verde e evidência anexada.

## Banco e transações

- [ ] PK, FK, unique, check e índices revisados.
- [ ] Transação começa na camada de aplicação.
- [ ] Falha no meio não deixa estado parcial.
- [ ] Concorrência testada quando há estoque, recompensa ou turno.
- [ ] Query crítica analisada com EXPLAIN.
- [ ] Migration testada em banco vazio.

## Segurança

- [ ] Deny by default.
- [ ] Ownership validado no caso de uso.
- [ ] Senha codificada e nunca logada.
- [ ] Access curto; refresh rotativo e revogável.
- [ ] Validação de entrada e tamanho.
- [ ] CORS, headers, rate limit e erros revisados.
- [ ] Dependências e segredos verificados.

## API

- [ ] Status HTTP correto.
- [ ] DTO separado do domínio/JPA.
- [ ] Problem Details consistente.
- [ ] Paginação possui limite.
- [ ] Idempotência em comandos repetíveis.
- [ ] OpenAPI e Bruno atualizados.

## Docker e deploy

- [ ] Imagem multi-stage e usuário não root.
- [ ] .dockerignore e sem segredo na imagem.
- [ ] Health, readiness e liveness.
- [ ] Variáveis obrigatórias validadas.
- [ ] Backup, migration e rollback ensaiados.
- [ ] Smoke test pós-deploy.

## Episódio

- [ ] Hook concreto nos primeiros 20 segundos.
- [ ] Problema e decisão explicados.
- [ ] Demo gravada sem segredo.
- [ ] Teste comprovando a regra.
- [ ] Erro/aprendizado incluído.
- [ ] Thumbnail legível em tamanho pequeno.
- [ ] Capítulos, links, playlist e comentário fixado.

## Release

- [ ] Milestone sem blocker.
- [ ] Regressão, smoke e segurança passam.
- [ ] Changelog reconciliado com PRs.
- [ ] Tag SemVer aponta para commit implantado.
- [ ] OpenAPI, Bruno e README correspondem à versão.
- [ ] Rollback disponível.
- [ ] Demo e release notes publicadas.
