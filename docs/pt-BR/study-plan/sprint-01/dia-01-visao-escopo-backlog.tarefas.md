# Dia 1 — Visão, escopo e backlog

**Data:** 17/08/2026  
**Sprint:** 1 — Produto, domínio e base executável  
**Tempo núcleo:** 2h  
**Extensão:** 60 min opcional  
**Resultado:** um produto recortado, ordenado e verificável antes do código.

## Antes de começar

- [ ] Leia 00-COMECE-AQUI, plano mestre e escopo.
- [ ] Crie o repositório rpg-turn-based-backend.
- [ ] Ative Issues e Projects no GitHub, se disponíveis.
- [ ] Copie README-GITHUB.md como rascunho de README.md.
- [ ] Crie um diário usando o template.

## O que você precisa compreender

- Product Goal descreve o estado futuro desejado, não uma lista de tecnologias.
- MVP é a menor versão que completa uma jornada, não um conjunto de telas incompletas.
- Backlog é ordenado; prioridade igual para tudo significa ausência de decisão.
- Critério de aceite descreve comportamento observável.
- Fora de escopo protege prazo e qualidade.
- Valor, risco e dependência influenciam a ordem.

## Fontes oficiais

1. Scrum Guide 2020 — Product Goal, Product Backlog e Sprint Goal:  
   https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-US.pdf
2. GitHub Issues:  
   https://docs.github.com/issues/tracking-your-work-with-issues/about-issues
3. GitHub Projects:  
   https://docs.github.com/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects

Leia somente as seções ligadas às saídas do dia.

## Exemplo neutro — reserva de quadra

Objetivo ruim: “usar Spring, JPA e JWT”.

Objetivo melhor: “permitir que um associado reserve uma quadra disponível sem dupla reserva e consulte suas reservas”.

Fatia MVP: autenticar → consultar horário → reservar → impedir conflito → cancelar. Chat, pagamento e ranking ficam fora.

Princípio a transferir: tecnologia apoia o comportamento; não é o resultado do produto.

## Tarefa prática

### Bloco 1 — Recuperação e leitura, 20 min

Sem consultar, escreva:

- o que diferencia o RPG de um CRUD;
- quem usa;
- qual é o ciclo principal;
- quais cinco riscos podem invalidar a entrega.

Depois compare com o escopo.

### Bloco 2 — Product brief, 25 min

No repositório, crie docs/PRODUCT-SCOPE.md contendo:

- visão em uma frase;
- problema;
- Product Goal com data;
- jogador, administrador e avaliador;
- jornada principal;
- Must, Should, Could e Won’t;
- métricas e critério de release.

Adapte o documento fornecido; remova qualquer promessa que não pretende implementar.

### Bloco 3 — Backlog, 35 min

Crie issues para as histórias Must. Para cada uma:

- ID;
- usuário, capacidade e benefício;
- regras relacionadas;
- dois critérios felizes/limites;
- dois critérios de falha;
- risco;
- dependência;
- tamanho relativo 3, 5 ou 8.

Ordene primeiro o risco que bloqueia o ciclo, não a parte mais divertida.

### Bloco 4 — Planejamento da Sprint 1, 20 min

Defina o Sprint Goal em uma frase. Selecione apenas os itens dos dias 1 a 6. Crie quadro com Backlog, Ready, In Progress, Review, Validate e Done. WIP de In Progress igual a um.

### Bloco 5 — Verificação e evidência, 20 min

Faça um teste de coerência:

- toda história Must liga a uma etapa da jornada?
- todo endpoint previsto serve uma história?
- cada regra crítica tem ao menos um critério?
- algo fora de escopo entrou disfarçado?

Atualize README com estado “em desenvolvimento”, crie commit e diário.

## Critérios de aceite

- [ ] Product Goal contém usuário, resultado e data.
- [ ] Jornada principal é executável do início ao fim.
- [ ] Must cabe no mês após remover Should/Could.
- [ ] Há pelo menos 12 histórias ordenadas.
- [ ] Cada história possui comportamento e falha.
- [ ] Microsserviços, frontend e tempo real estão fora.
- [ ] Sprint Goal não é “estudar tecnologias”.
- [ ] Quadro possui WIP 1.

## Testes obrigatórios

Faça três simulações de mudança:

1. Prazo perde cinco dias: indique exatamente o que sai.
2. Deploy fica indisponível: defina demonstração alternativa local.
3. Habilidade com cooldown atrasa: mostre que ataque básico ainda completa batalha.

Se o ciclo quebrar, o backlog está mal ordenado.

## Evidências

- link do repositório;
- docs/PRODUCT-SCOPE.md;
- captura/lista do backlog ordenado;
- Sprint Goal;
- commit sugerido: docs(product): define MVP goal and ordered backlog.

## Perguntas de recuperação

Responda amanhã sem notas:

1. Qual é o Product Goal?
2. Qual diferença entre Must e Should?
3. Qual é o primeiro comportamento que prova valor?
4. Por que “implementar JWT” não é Product Goal?
5. Que item você corta primeiro e por quê?

## Erros comuns

- transformar o backlog em grade de curso;
- estimar em horas com falsa precisão;
- criar épicos sem critérios;
- colocar tudo como Must;
- confundir “API completa” com resultado;
- adicionar tecnologia para parecer sênior.

## Extensão profissional opcional

Peça a uma pessoa para ler apenas o escopo e descrever o produto. Registre dúvidas dela; isso testa clareza sem discutir código.

## Conteúdo do dia

Grave até dois minutos: “Como recortei um RPG para conseguir entregar em 30 dias”.

## Correção e conferência — só depois da tentativa

Seu Product Goal deve se parecer com um resultado: “Até 12/09, permitir o ciclo conta → personagem → missão → batalha → ranking com segurança, consistência e execução reproduzível”.

O backlog correto começa por base executável e riscos do ciclo. Se sua lista começa com “criar 30 itens, 20 monstros e 10 classes”, ela está orientada a conteúdo, não ao risco técnico. Deve ser possível remover habilidades avançadas e ainda concluir uma batalha com ataque básico.
