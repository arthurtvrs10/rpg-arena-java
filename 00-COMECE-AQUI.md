# RPG Arena — comece aqui

Este é o pacote único do projeto: código inicial, análise de requisitos, arquitetura, contrato de API, planejamento de seis meses, tarefas semanais, backlog, materiais de GitHub e minissérie do YouTube.

## Estado real

- O repositório contém uma aplicação Spring Boot inicial.
- Nenhuma funcionalidade de jogo está marcada como implementada.
- A especificação da versão 1.0 está fechada e pronta para orientar o desenvolvimento.
- O trabalho começa pela Semana 01 e termina com a release `v1.0.0` na Semana 24.

## Ordem obrigatória

1. Leia `docs/requisitos/00-INDICE-E-DECISOES-FECHADAS.md`.
2. Leia `docs/requisitos/01-ESPECIFICACAO-DO-PRODUTO.md`.
3. Consulte `docs/requisitos/02-CATALOGO-REQUISITOS.md` e `03-REGRAS-DE-NEGOCIO.md` durante a implementação.
4. Abra `docs/api/openapi.yaml` antes de criar controllers ou DTOs.
5. Abra `planejamento/BACKLOG-MESTRE-6-MESES.xlsx` e altere somente as colunas de acompanhamento.
6. Execute `planejamento/tarefas/semana-01.tarefas`.
7. Ao iniciar uma história, use o caso de uso, a regra e o critério BDD ligados a ela.
8. Só marque uma tarefa como concluída quando a evidência exigida estiver no repositório.

## Fonte de verdade

Em caso de conflito, siga esta ordem:

1. `docs/requisitos/` — comportamento e regras da versão 1.0;
2. `docs/api/openapi.yaml` — contrato HTTP;
3. `docs/dados/` — persistência e restrições;
4. `docs/decisoes/` — decisões arquiteturais;
5. `planejamento/` — sequência, prazo e conteúdo;
6. `docs/pt-BR/` — material anterior de estudo, mantido como referência.

## Regra de execução

Não implemente uma entidade inteira por antecipação. Entregue fatias verticais: contrato, caso de uso, regra, persistência e teste para um comportamento demonstrável.

## Primeira ação

Crie a issue `RPG-M1-W01-01`, abra a branch `docs/visao-produto`, execute o arquivo da Semana 01 e registre as decisões nos documentos já preparados. A análise não precisa ser refeita; altere-a somente por decisão explícita registrada em ADR ou log de mudança de requisito.
