# Método de execução

## Carga semanal - 18 a 22 horas

| Dia | Trabalho | Resultado |
|---|---|---|
| Segunda | Leitura dirigida + tarefa 1 | decisão/documento ou regra pronta |
| Terça | Tarefa 2 | implementação principal |
| Quarta | Tarefa 3 + Short | segunda parte e conteúdo curto |
| Quinta | Tarefa 4 | integração/persistência/API |
| Sexta | Tarefa 5 | testes, refatoração e PR |
| Sábado | Buffer de até 2h | corrigir bloqueio, não adicionar escopo |
| Domingo | Tarefa 6 | Short ou episódio e retrospectiva |

## Ciclo de aprendizagem

1. Leia apenas a seção oficial necessária para a tarefa.
2. Escreva a regra em português e um exemplo antes do código.
3. Implemente o menor caminho completo.
4. Teste caminho feliz, erro e limite.
5. Refatore nomes e responsabilidades.
6. Explique em voz alta sem consultar o código.
7. Registre decisão, evidência e dúvida resolvida no PR.

## Hierarquia de consulta sem IA

1. Documentação oficial.
2. Testes e exemplos oficiais do projeto/biblioteca.
3. Código-fonte e Javadoc.
4. Issue oficial ou discussão do mantenedor.
5. Livro/artigo técnico reconhecido.
6. Stack Overflow apenas para pistas; valide na fonte oficial.

## Definition of Ready

- Problema e valor descritos.
- Critério de aceite mensurável.
- Dependências identificadas.
- Referência oficial definida.
- Tamanho cabe em até dois dias.

## Definition of Done

- Código compila e segue arquitetura.
- Testes relevantes passam.
- Banco/migration validado quando aplicável.
- Bruno/OpenAPI atualizado quando aplicável.
- Documentação e ADR atualizados.
- Nenhum segredo no diff.
- PR revisado, CI verde e evidência anexada.
- Material de gravação capturado.

## Git profissional

- Uma issue por entrega.
- Branch: `feat/123-combat-turn`, `fix/456-refresh-reuse`, `docs/789-architecture`.
- Commit: Conventional Commits.
- PR pequeno, ligado à issue, com teste e evidência.
- Squash merge na main protegida.
- Tag SemVer a cada marco.

## Regra contra atraso

Se uma semana atrasar: corte item opcional, preserve o fluxo vertical e mova somente tarefas explicitamente não críticas. Não avance com dívida que invalida segurança, transação ou teste do marco.
