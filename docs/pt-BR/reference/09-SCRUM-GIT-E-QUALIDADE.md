# Scrum, Kanban, Git e qualidade

## Modelo de trabalho

Você acumula as funções de Product Owner, analista, Scrum Master e desenvolvedor. Para evitar conflito:

- como Product Owner, ordena por valor e corta escopo;
- como analista, torna regras e critérios verificáveis;
- como Scrum Master, protege o timebox e remove impedimentos;
- como desenvolvedor, implementa e prova qualidade;
- não altere critérios silenciosamente para considerar algo pronto.

## Sprint de uma semana

### Planning — segunda, 20 minutos

- reler Product Goal;
- definir Sprint Goal em uma frase;
- escolher apenas tarefas Must que cabem;
- confirmar critérios e dependências;
- criar branch da primeira história.

### Daily — cada dia, 5 minutos

Registrar:

1. qual resultado ficou pronto;
2. qual é o próximo menor passo;
3. qual impedimento exige ação;
4. se o Sprint Goal corre risco.

### Refinamento — quarta, 15 minutos

Preparar dois próximos itens; não implementar.

### Review — sábado, 25 minutos

Demonstrar comportamento executável a partir do ponto de vista do usuário. Não mostrar apenas arquivos.

### Retrospectiva — sábado, 20 minutos

- manter uma prática;
- parar uma prática;
- começar uma prática;
- escolher uma única ação com dono e prazo.

## Quadro e WIP

Colunas:

- Backlog;
- Ready;
- In Progress;
- Review;
- Validate;
- Done.

Limites:

- In Progress: 1;
- Review: 1;
- Validate: 1.

Bloqueado não é nova coluna conveniente; marque causa, horário e próxima ação.

## Branches

Padrões:

- feat/BA-02-basic-attack;
- fix/AU-03-owner-check;
- test/MI-03-idempotency;
- docs/ADR-003-concurrency;
- chore/DE-02-ci.

Branches curtas, ligadas a item de backlog. Não acumule a sprint inteira em uma branch.

## Commits

Formato:

~~~text
tipo(escopo): intenção no imperativo
~~~

Exemplos:

- feat(battle): reject actions outside current turn
- test(mission): prove reward is granted once
- fix(security): scope character lookup by authenticated owner
- docs(adr): record optimistic locking decision

Um commit deve ser compreensível isoladamente e manter o build utilizável quando possível. Não use “ajustes”, “final” ou “coisas”.

## Pull request

Todo PR informa:

- problema e história;
- solução e limite;
- regras afetadas;
- endpoints/migrations;
- como testar;
- riscos e rollback;
- evidências;
- checklist de segurança;
- decisão que merece comentário.

Faça revisão em três passagens:

1. comportamento: atende critérios e erros?
2. risco: segurança, transação, concorrência e dados?
3. manutenção: nomes, dependências, duplicação e clareza?

## Política de merge

Merge somente quando:

- CI verde;
- comentários resolvidos;
- migration revisada;
- testes críticos presentes;
- README/Bruno atualizados;
- sem segredo;
- Definition of Done cumprida.

Mesmo trabalhando sozinho, deixe o PR aberto por pelo menos uma revisão deliberada. Leia o diff no GitHub como se fosse código de outra pessoa.

## Métricas úteis

- histórias Done por sprint;
- tempo do início ao Done;
- defeitos encontrados depois do merge;
- testes intermitentes;
- itens bloqueados e causa;
- histórias reabertas;
- candidaturas e feedback.

Não use linhas de código ou número de commits como produtividade.

## Controle de qualidade

### Antes de implementar

- regra numerada;
- exemplo e contraexemplo;
- critérios observáveis;
- risco principal;
- estratégia de teste.

### Antes do commit

- formatter;
- teste focal;
- nenhum segredo;
- diff revisado;
- nome comunica intenção.

### Antes do PR

- verify completo;
- Bruno quando houver API;
- migration do zero;
- logs e erros revisados;
- documentação.

## Tratamento de impedimento

Modelo de registro:

- Sintoma:
- Comando/requisição:
- Resultado esperado:
- Resultado atual:
- Primeira ocorrência:
- Hipóteses:
- Experimentos realizados:
- Evidência:
- Próxima ação de até 20 minutos:

Um impedimento documentado vira conhecimento; uma tarde alternando tentativas aleatórias vira retrabalho.
