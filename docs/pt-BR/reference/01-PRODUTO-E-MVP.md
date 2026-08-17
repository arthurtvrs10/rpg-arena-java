# Produto e MVP

## Visão

Para pessoas que querem uma experiência curta de RPG baseada em decisões, o RPG Arena oferece progressão, missões e batalhas por turnos através de uma API confiável. Diferente de um CRUD de catálogo, o produto expõe regras de estado, propriedade, concorrência e recompensa que precisam permanecer corretas mesmo sob repetição ou falha.

## Product Goal

Até 12/09/2026, disponibilizar uma versão executável na qual um jogador percorra o ciclo conta → personagem → equipamento → missão → batalha → ranking, com segurança por proprietário, consistência de dados, testes reproduzíveis e documentação suficiente para outra pessoa executar.

## Hipóteses

| Código | Hipótese | Como validar no mês |
|---|---|---|
| H1 | O ciclo principal cabe em quatro sprints | Incremento utilizável ao final de cada sábado |
| H2 | O domínio evidencia mais competência que CRUD simples | Demo apresenta estados, transação e concorrência |
| H3 | API-first é suficiente para o portfólio | Fluxo completo executável no Bruno |
| H4 | Monólito modular reduz custo sem esconder limites | Módulos possuem dependências controladas |
| H5 | Duas horas diárias sustentam o núcleo | Tarefas Must cabem no timebox e extensões são opcionais |

## Personas

### Júlia, jogadora

- quer começar rapidamente;
- espera que seus itens e personagens estejam protegidos;
- não entende detalhes internos da API;
- precisa de mensagens de erro acionáveis;
- aceita combate por turnos, mas não aceita perder progresso por clique repetido.

### Caio, administrador

- cadastra missões, itens e habilidades;
- precisa de validações para não criar catálogo inconsistente;
- não deve visualizar senha ou token;
- precisa distinguir erro do cliente de falha operacional.

### Renata, avaliadora técnica

- clona o repositório;
- segue o README;
- executa testes e coleção;
- procura regras além de CRUD;
- pergunta por que a arquitetura e os mecanismos de consistência foram escolhidos.

## Jornada principal

1. Visitante cria conta.
2. Conta autentica e recebe token.
3. Jogador cria personagem de uma classe.
4. Sistema entrega equipamento inicial.
5. Jogador equipa item válido.
6. Jogador inicia missão disponível.
7. Sistema valida conclusão e aplica recompensa.
8. Jogador inicia batalha PvE.
9. Jogador e inimigo alternam ações.
10. Sistema encerra batalha e atualiza resultado.
11. Jogador consulta ranking.

## Recorte Must / Should / Could / Won’t

### Must

- autenticação e papéis;
- propriedade dos recursos;
- personagem e progressão;
- inventário e equipamento;
- missão com recompensa única;
- batalha PvE por turnos;
- ranking paginado;
- migrations, testes, Bruno, Docker, CI e documentação.

### Should

- catálogo administrável;
- logs correlacionados;
- histórico resumido de ações;
- filtro de ranking por classe;
- métricas básicas do Actuator.

### Could

- replay textual;
- efeitos de status simples;
- renovação de token;
- cache de ranking somente após medição;
- publicação de imagem do container.

### Won’t no mês

- frontend;
- multiplayer em tempo real;
- microserviços;
- mensageria;
- pagamentos;
- Kubernetes;
- economia e marketplace.

## Fatiamento vertical

Cada história deve atravessar contrato, aplicação, regra, persistência e teste apenas na profundidade necessária. Evite construir “todas as entidades” antes de obter um fluxo.

Exemplo de fatia correta:

- criar personagem com limite, propriedade e resposta;
- não “criar módulo inteiro de personagens”.

Exemplo de fatia incorreta:

- criar todas as tabelas do jogo sem nenhum caso de uso executável.

## Critérios de valor

Uma funcionalidade agrega valor ao MVP quando:

- desbloqueia parte da jornada;
- evidencia decisão técnica relevante;
- pode ser demonstrada isoladamente;
- possui risco controlado por teste;
- não introduz infraestrutura sem requisito.

## Perguntas que o produto deve responder

- O que ocorre se a requisição de recompensa for repetida?
- Quem decide se o jogador é proprietário: URL ou identidade autenticada?
- O que ocorre quando duas ações chegam para o mesmo turno?
- Como uma migration nova funciona em banco vazio e em banco existente?
- Como um avaliador reproduz o fluxo sem conhecer o código?
- Qual funcionalidade seria removida primeiro se o prazo encolhesse?

## Decisão de prazo

Se houver atraso, preserve primeiro: autenticação, propriedade, personagem, missão/recompensa, batalha mínima, testes críticos e execução. Remova nesta ordem: filtros avançados, administração via API, histórico detalhado, métricas extras e efeitos especiais.
