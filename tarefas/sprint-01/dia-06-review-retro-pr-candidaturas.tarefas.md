# Dia 6 — Review, retrospectiva, PR e candidaturas

**Data:** 22/08/2026  
**Sprint:** 1  
**Tempo núcleo:** 2h30  
**Extensão:** 60 min  
**Resultado:** primeiro incremento revisado, demonstrado e transformado em evidência profissional.

## Antes de começar

- [ ] Pare de iniciar funcionalidade nova.
- [ ] Confirme Sprint Goal.
- [ ] Reúna commits, testes, docs e impedimentos.
- [ ] Copie o template de review/retro.

## O que você precisa compreender

- Review inspeciona produto; retrospectiva inspeciona processo.
- PR é comunicação assíncrona e controle de mudança.
- Demo começa pelo comportamento, não pela árvore de classes.
- “Quase pronto” retorna ao backlog; não entra em Done.
- Candidatura é ciclo de feedback, não prêmio pelo projeto perfeito.

## Fontes

- Scrum Guide: https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-US.pdf
- GitHub pull requests: https://docs.github.com/pull-requests
- Git review: https://git-scm.com/docs
- Template local: ../../templates/REVIEW-RETRO-TEMPLATE.md

## Exemplo neutro — release de reservas

Uma review não mostra “criei três services”. Demonstra reserva disponível, tentativa duplicada rejeitada e banco reproduzível. A retro não diz “foi bom”; escolhe uma ação como “limitar leitura a 20 minutos antes do experimento”.

## Tarefa prática

### 1. Auditoria da Definition of Done, 20 min

Para cada item:

- comportamento;
- testes;
- documentação;
- segurança aplicável;
- migration;
- commit;
- explicação.

Mova incompletos para backlog com descrição objetiva.

### 2. PR, 30 min

Abra PR da Sprint 1 ou PRs menores já existentes. Preencha:

- problema;
- escopo e fora;
- regras;
- decisões;
- como testar;
- evidências;
- riscos;
- rollback.

Revise o diff em três passagens: comportamento, risco, manutenção. Faça comentários em seu próprio PR antes de alterar.

### 3. Verificação limpa, 25 min

Em banco descartável:

- suba PostgreSQL;
- aplique migrations;
- execute build/test;
- verifique health;
- rode regra de progressão;
- confira git status.

### 4. Demo, 20 min

Grave ou apresente:

1. Product Goal e fora de escopo;
2. estrutura modular;
3. banco do zero;
4. regra de XP com teste de múltiplos níveis;
5. ADR e próximo risco.

Máximo cinco minutos.

### 5. Retrospectiva, 20 min

Registre:

- um manter;
- um parar;
- um começar;
- dados da sprint;
- uma ação da Sprint 2.

Analise tempo bloqueado e histórias reabertas.

### 6. Portfólio e candidaturas, 25 min

- publique um post/vídeo técnico honesto;
- atualize descrição do GitHub;
- selecione duas vagas Java backend compatíveis;
- personalize resumo usando evidência real;
- candidate-se e registre.

Não diga que autenticação ou deploy já existem se ainda não existem.

### 7. Fechamento, 10 min

Faça merge somente se CI/testes e DoD estiverem verdes. Crie tag 0.1.0 opcional.

## Critérios de aceite

- [ ] Sprint Goal foi avaliado por evidência.
- [ ] PR descreve risco e teste.
- [ ] banco vazio funciona.
- [ ] demo tem comportamento executável.
- [ ] retro tem uma ação mensurável.
- [ ] backlog foi reordenado.
- [ ] duas candidaturas foram registradas.
- [ ] comunicação não exagera o que existe.

## Testes obrigatórios

- clone/ambiente limpo ou simulação equivalente;
- Maven verify;
- migrations do zero;
- revisão de segredos;
- links do README;
- diff completo.

## Evidências

- PR;
- saída da suíte;
- review/retro;
- vídeo/post;
- duas candidaturas sem dados sensíveis;
- commit final: docs(sprint): close sprint one with review evidence.

## Perguntas de recuperação

1. Qual a diferença entre review e retro?
2. O que impediu mais progresso?
3. Que decisão você consegue defender?
4. Qual risco central da Sprint 2?
5. O que você remove se atrasar?

## Erros comuns

- usar sábado para começar nova feature;
- merge com teste quebrado;
- demo de slides sem execução;
- retro com cinco ações;
- candidatura genérica em massa;
- declarar nível profissional sem evidência.

## Extensão opcional

Peça review do PR a uma comunidade ou colega. Faça pergunta específica: “A fronteira de domínio e a regra de progressão estão compreensíveis?”.

## Correção e conferência — só depois da tentativa

Sprint 1 está bem-sucedida se outra pessoa entende o produto, sobe base e vê uma regra não trivial testada. Autenticação ainda não é exigida. Se o banco só funciona com passos ocultos, se o domínio depende do Spring ou se não há teste de múltiplos níveis, o incremento não cumpre a porta de qualidade.
