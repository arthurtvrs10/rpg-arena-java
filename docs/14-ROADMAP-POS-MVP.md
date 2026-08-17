# Roadmap pós-MVP

Este roadmap existe para proteger o mês. Ideias boas vão para cá em vez de entrar no sprint atual.

## 1.1 — Robustez

- refresh token e política de revogação;
- auditoria de ações administrativas;
- replay textual de batalha;
- reconstrução de ranking;
- limites de abuso medidos;
- testes de carga do fluxo crítico;
- backup e restauração testados.

## 1.2 — Eventos confiáveis

- eventos de domínio;
- outbox transacional;
- consumidor idempotente;
- ranking e notificações desacopladas;
- métricas de fila;
- estratégia de reprocessamento.

Só implementar após dominar transação local e identificar consumidor real.

## 1.3 — Experiência

- frontend simples;
- documentação pública aprimorada;
- histórico do personagem;
- efeitos de status;
- novas classes e habilidades;
- internacionalização de mensagens.

## 2.0 — PvP assíncrono

- matchmaking;
- turnos com prazo;
- abandono;
- reconexão;
- prevenção de trapaça;
- controle de concorrência ampliado;
- privacidade do oponente.

## Pesquisa arquitetural

- medir gargalos antes de cache;
- comparar projeção síncrona e assíncrona;
- avaliar particionamento somente com volume;
- identificar limites organizacionais antes de separar serviço;
- calcular custo operacional de cada componente.

## Gatilhos para tecnologia

| Tecnologia | Só considerar quando |
|---|---|
| Redis | leitura medida é gargalo e estratégia de invalidação está definida |
| Mensageria | existe trabalho assíncrono, tolerância a atraso e reprocessamento |
| Microsserviços | limites e equipes independentes justificam deploy separado |
| Kubernetes | número de serviços e operação tornam orquestração necessária |
| WebSocket | produto exige atualização bidirecional quase em tempo real |

## Regra

Roadmap não é promessa. Cada item precisa voltar à descoberta, ter usuário, valor, risco, critério e métrica antes de virar sprint.
