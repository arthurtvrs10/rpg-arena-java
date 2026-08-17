# Portfólio, comunicação e candidaturas

## Princípio

Não espere o projeto ficar perfeito. Candidate-se enquanto constrói, use perguntas e rejeições como dados e melhore o material semanalmente.

## Meta de candidaturas

| Semana | Quantidade mínima | Material disponível |
|---|---:|---|
| 1 | 2 | visão, arquitetura e regra pura testada |
| 2 | 3 | autenticação, propriedade e inventário |
| 3 | 4 | transação, idempotência e concorrência |
| 4 | 5 | release, CI, deploy e demo |

Total mínimo: 14 candidaturas personalizadas. Qualidade importa: leia a vaga, ajuste resumo e registre retorno.

## Planilha ou registro

- empresa;
- vaga;
- link;
- data;
- requisitos aderentes;
- lacuna real;
- versão do currículo;
- contato;
- etapa;
- retorno;
- pergunta técnica recebida;
- ação de melhoria.

## Pitch de 60 segundos

Estrutura:

1. quem você é e foco;
2. problema do projeto;
3. três decisões relevantes;
4. como você prova qualidade;
5. o que procura.

Exemplo-base para adaptar:

“Sou desenvolvedor backend Java em transição para a primeira oportunidade profissional. No RPG Arena construí uma API Spring Boot com PostgreSQL. O destaque não é apenas o CRUD: modelei máquinas de estado, proteção por proprietário, recompensa idempotente e concorrência de turnos. Valido regras com JUnit, banco real com Testcontainers e fluxos no Bruno, e entrego com Docker e CI. Procuro uma equipe em que eu possa contribuir no backend e continuar evoluindo com review.”

Não memorize palavra por palavra. Grave até soar natural e fiel ao que foi concluído.

## Demo de oito minutos

1. 0:00–0:45 — problema e escopo;
2. 0:45–1:30 — arquitetura e pastas;
3. 1:30–3:30 — jornada feliz;
4. 3:30–4:30 — acesso cruzado rejeitado;
5. 4:30–5:30 — repetição idempotente;
6. 5:30–6:30 — concorrência/teste;
7. 6:30–7:15 — CI, Docker e documentação;
8. 7:15–8:00 — trade-off e próximo passo.

## Perguntas técnicas para praticar

### Java e domínio

- Por que regra de combate não depende do Spring?
- Como garante estado válido sem setters livres?
- Onde usou enum, value object e composição?
- Como testou múltiplos níveis?

### Spring e HTTP

- Qual responsabilidade do Controller?
- Onde começa e termina a transação?
- Por que não retorna entidade JPA?
- Como escolheu 400, 401, 403, 404 e 409?

### Banco

- O que uma migration resolve?
- Por que restrição única ainda é necessária?
- Como Read Committed afeta “ler e gravar”?
- Quando optimistic locking falha e como tratar?

### Segurança

- Como evita BOLA?
- Por que JWT não resolve autorização?
- Que dados nunca entram no token ou log?
- Como testou acesso de A contra B?

### Testes e entrega

- O que é unitário e o que exige container?
- Como seu teste de concorrência evita falso positivo?
- O que o Bruno prova que JUnit não prova?
- Como outra pessoa executa o projeto?

## Conteúdo semanal

- Sprint 1: “De CRUD para domínio: como modelei progressão de personagem”.
- Sprint 2: “JWT não basta: como protegi recursos por proprietário”.
- Sprint 3: “Duas ações no mesmo turno: concorrência e idempotência”.
- Sprint 4: “Da regra ao deploy: como entreguei uma API Java testável”.

Mostre aprendizado e evidência; não revele segredo, token ou dados pessoais.

## Revisão do GitHub

- README começa pelo valor;
- projeto fixado no perfil;
- descrição curta e tópicos coerentes;
- commits legíveis;
- issues e PRs mostram processo;
- CI visível;
- release e changelog;
- licença escolhida;
- nenhum segredo ou arquivo de IDE;
- instruções foram testadas em clone limpo.

## Feedback sem autoengano

Depois de entrevista:

1. anote perguntas imediatamente;
2. marque “soube”, “parcial” ou “não soube”;
3. escreva a resposta com suas palavras;
4. aplique uma melhoria concreta;
5. continue candidatando.

Não adicione uma tecnologia só porque apareceu uma vez. Procure padrões em várias vagas e mantenha profundidade no núcleo.
