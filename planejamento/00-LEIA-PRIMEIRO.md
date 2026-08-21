# LEIA PRIMEIRO - RPG ARENA

> Este planejamento agora faz parte do repositório completo. Antes de executar qualquer semana, consulte `../docs/requisitos/00-INDICE-E-DECISOES-FECHADAS.md`. A análise em `docs/requisitos/` é a fonte oficial de comportamento; este diretório define ordem, prazo e evidências.

## Resultado

Em 24 semanas, entregar o backend open source do **RPG Arena**, publicar a versão 1.0.0 e lançar uma minissérie técnica com 12 episódios e 24 Shorts.

## Período e carga

- Início: 24/08/2026
- Encerramento: 07/02/2027
- Carga: 18-22 horas por semana
- Total: 24 semanas, 144 tarefas, 12 episódios e 24 Shorts

## Ordem de uso

1. Leia `01-ESCOPO-PRODUTO.md`.
2. Leia `02-ARQUITETURA-ESTRUTURA.md`.
3. Abra `BACKLOG-MESTRE-6-MESES.xlsx` e atualize somente o Status.
4. Execute o arquivo da semana em `tarefas/`.
5. Use `04-MINISSERIE-YOUTUBE.md` para gravar durante o desenvolvimento.
6. Faça um PR por tarefa ou grupo pequeno e só marque como concluído quando o critério de aceite estiver comprovado.

## Regra principal

Não adicionar tecnologia porque apareceu em uma vaga. O projeto permanece monólito modular até a versão 1.0. Microserviços, Kafka, Kubernetes, interface gráfica e multiplayer ficam fora do escopo.

## Entregas principais

- v0.1.0: personagem e combate.
- v0.2.0: persistência, inventário, progressão e missões.
- v0.3.0: API REST segura.
- v0.4.0: mundo, economia e conteúdo administrativo.
- v1.0.0-rc.1: qualidade, Docker e operação.
- v1.0.0: deploy, open source, portfólio e temporada finalizada.
