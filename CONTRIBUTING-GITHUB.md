# Contribuindo

## Fluxo

1. escolha uma issue Ready;
2. crie branch curta com ID;
3. implemente uma fatia;
4. execute testes;
5. atualize contrato e documentos;
6. abra pull request;
7. revise o diff;
8. faça merge somente com CI verde.

## Qualidade

Toda mudança de comportamento precisa de teste. Endpoint de recurso privado precisa de cenário com outro jogador. Mudança de banco precisa de migration nova. Nenhum segredo pode entrar no repositório.

## Commits

Use tipo e escopo, por exemplo:

~~~text
feat(battle): reject duplicate action request
~~~

## Pull requests

Pequenos, explicáveis e ligados a uma história. Inclua riscos, evidências e instrução de teste.
