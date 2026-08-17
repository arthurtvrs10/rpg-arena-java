# RPG Arena — imersão backend de 30 dias

Este é um plano de execução, não uma lista de assuntos. Durante quatro sprints você construirá uma API de RPG de turnos com Java 21, Spring Boot, PostgreSQL, Flyway, Spring Security, testes, Bruno, Docker e integração contínua.

O plano começa no seu nível atual. Ele pressupõe que você já consegue criar um projeto Spring Boot, entende Controller, Service, Repository, DTO, JPA, injeção de dependência, Maven, PostgreSQL básico, Docker Compose e requisições no Bruno. Não há uma semana de variáveis, laços, classes ou CRUD introdutório.

## Expectativa honesta

Não é possível adquirir oito anos reais de experiência em um mês. Experiência inclui incidentes, manutenção, colaboração e decisões repetidas em contextos diferentes. O que este plano faz é concentrar, em 30 dias, práticas que normalmente demoram anos para aparecer em estudos soltos:

- descoberta e recorte de produto;
- modelagem de regras de negócio;
- decisões arquiteturais registradas;
- contratos HTTP e segurança por propriedade;
- transações, concorrência e idempotência;
- testes em vários níveis;
- revisão por critérios, não por “funcionou na minha máquina”;
- entrega, documentação e comunicação técnica.

## Calendário

- Início: 17/08/2026.
- Encerramento: 13/09/2026.
- Trabalho principal: segunda a sábado.
- Domingo: descanso; no máximo 30 minutos para organizar a semana seguinte.
- Núcleo diário: 2 horas.
- Extensão profissional opcional: 60 a 90 minutos.
- Total: 24 dias de execução em quatro sprints de uma semana.

## Como usar a pasta

1. Leia hoje o plano mestre, o escopo, as regras e a arquitetura.
2. Abra apenas o arquivo do dia atual na pasta tarefas.
3. Trabalhe em uma única história por vez.
4. Consulte primeiro as fontes indicadas no arquivo do dia.
5. Não abra a seção “Correção e conferência” antes de produzir sua própria tentativa.
6. Termine cada dia com teste, evidência, diário e commit.
7. Aos sábados, faça review, retrospectiva, vídeo curto e candidatura.

## Ritual diário de duas horas

| Bloco | Tempo | Ação |
|---|---:|---|
| Recuperação | 10 min | Responder sem consultar as perguntas de ontem |
| Leitura dirigida | 20 min | Ler apenas as seções oficiais indicadas |
| Modelagem | 15 min | Escrever regra, contrato ou diagrama antes do código |
| Implementação | 55 min | Executar a menor fatia vertical da tarefa |
| Verificação | 15 min | Rodar testes e cenário Bruno |
| Evidência | 5 min | Atualizar diário e criar commit |

A extensão profissional é usada para testes adicionais, documentação, refatoração ou candidatura. Nunca use a extensão para começar outra história sem concluir a atual.

## Regra de consulta sem IA

Quando travar:

1. escreva em uma frase o comportamento esperado;
2. copie a mensagem de erro exata;
3. identifique a camada: domínio, HTTP, segurança, persistência, banco ou ambiente;
4. consulte a documentação oficial indicada;
5. procure pelo conceito e pela mensagem, não por “projeto completo pronto”;
6. reduza para um teste mínimo;
7. registre a causa e a correção no diário.

Se após 25 minutos você ainda não tiver uma hipótese testável, marque a tarefa como impedida, documente o que tentou e passe para o item de diagnóstico do próprio arquivo. Não copie uma solução que você não consegue explicar.

## Resultado obrigatório no encerramento

Você deverá conseguir demonstrar:

- aplicação backend funcional em Java 21 e Spring Boot;
- regras de personagem, inventário, missão e batalha modeladas por objetos;
- PostgreSQL versionado por migrations, com transações e controle de concorrência;
- API REST autenticada, autorizada e isolada por jogador;
- testes unitários, integração com banco real e coleção Bruno;
- branches curtas, pull requests, commits semânticos e histórico legível;
- execução completa com Docker Compose;
- CI no GitHub Actions;
- README, escopo, OpenAPI, decisões e demonstração pública;
- explicação dos principais trade-offs;
- candidaturas realizadas e feedback registrado.

## Ordem de leitura

1. [Plano mestre](PLANO-MESTRE-30-DIAS.md)
2. [Escopo do produto](PRODUCT-SCOPE.md)
3. [Produto e MVP](reference/01-PRODUTO-E-MVP.md)
4. [Regras de negócio](reference/03-REGRAS-DE-NEGOCIO.md)
5. [Arquitetura e pastas](reference/04-ARQUITETURA-E-PASTAS.md)
6. [Metodologia](reference/10-METODOLOGIA-DE-APRENDIZAGEM.md)
7. [Sprint 1 — Dia 1](study-plan/sprint-01/dia-01-visao-escopo-backlog.tarefas.md)

## Regra final

O projeto vale pelo que você consegue explicar, testar e entregar. Uma funcionalidade pequena concluída com regra clara, teste, documentação e commit vale mais do que cinco tecnologias parcialmente instaladas.
