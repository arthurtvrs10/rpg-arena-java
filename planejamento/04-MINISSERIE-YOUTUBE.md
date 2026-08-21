# Minissérie YouTube - RPG Arena

## Formato

- 12 episódios principais, um a cada duas semanas, com 12-18 minutos.
- 24 Shorts, um por semana, com 30-60 segundos.
- Uma demonstração final de 6-10 minutos separada do episódio 12.
- Publicação principal no domingo de cada semana par.
- O vídeo mostra problema, decisão, implementação, teste e resultado; não vira leitura de código.

## Identidade visual

- Fundo: ink #171126 e off-white #F7F3EA.
- Destaque: violeta #7C3AED e dourado #D4A017.
- Thumbnail: máximo de 4 palavras, um diagrama/objeto e contraste alto.
- Fonte visual: condensada para títulos e monoespaçada para código.

## Episódios

| Ep. | Semanas | Título | Hook | Demo | Thumbnail |
|---:|:---:|---|---|---|---|
| 01 | 1-2 | Construindo um RPG backend profissional: escopo e arquitetura | O maior erro não é escolher a tecnologia errada; é começar a codar sem saber o que precisa terminar. | Repositório, diagrama modular, aplicação iniciando e check verde. | RPG BACKEND DO ZERO |
| 02 | 3-4 | Personagem e combate: domínio rico em Java | Se toda regra está no service, suas entidades são apenas tabelas com getters. | Batalha completa executada por teste com seed fixa. | ADEUS, DOMÍNIO ANÊMICO |
| 03 | 5-6 | PostgreSQL, Flyway e inventário transacional | Um item duplicado por concorrência destrói a confiança no jogo. | Migration do zero, rollback e duas atualizações concorrentes. | SEM DUPLICAR ITENS |
| 04 | 7-8 | XP, habilidades e missões com eventos de domínio | Conectar tudo com chamadas diretas funciona até a primeira mudança. | Batalha gera XP, desbloqueia habilidade e conclui missão. | O RPG COMEÇOU A EVOLUIR |
| 05 | 9-10 | Transformando o RPG em uma API REST previsível | Uma API que funciona só no seu Postman não é uma API pronta. | CRUD de personagem e inventário com conflito de versão. | API QUE OUTROS CONSEGUEM USAR |
| 06 | 11-12 | JWT, ownership e batalha segura por HTTP | Ter JWT não impede um jogador de tentar acessar o personagem do outro. | Ataque com owner funciona; troca de ID retorna acesso negado. | JWT NÃO É AUTORIZAÇÃO |
| 07 | 13-14 | Mundo, viagens, NPCs e economia consistente | A economia quebra quando duas pessoas compram o último item. | Viagem gera encontro e compra concorrente permite só um vencedor. | QUEM COMPRA O ÚLTIMO ITEM? |
| 08 | 15-16 | Missões ramificadas e conteúdo administrável | Hardcode de diálogo transforma cada nova missão em deploy. | Admin publica missão; jogador escolhe e recebe consequência. | MISSÕES SEM HARDCODE |
| 09 | 17-18 | Testes reais e Docker: tornando o projeto reproduzível | Cobertura alta não salva teste que nunca encontra um bug. | Clone limpo, Testcontainers, JaCoCo e Docker Compose. | FUNCIONA EM OUTRA MÁQUINA? |
| 10 | 19-20 | Documentação, logs, métricas, performance e segurança | Se você não consegue observar a falha, você não consegue operar o sistema. | CorrelationId, métrica, N+1 corrigido e quality gate. | DE API FUNCIONAL A OPERÁVEL |
| 11 | 21-22 | Deploy e open source com fluxo profissional | Publicar não é apertar deploy; é saber voltar quando der errado. | Deploy, smoke, rollback e PR externo simulado. | COLOQUEI O RPG ONLINE |
| 12 | 23-24 | Release 1.0: seis meses construindo um RPG backend | O resultado não é uma lista de tecnologias; é um sistema que eu consigo explicar e entregar. | Jornada completa em produção, testes, GitHub e release. | 6 MESES. 1 RPG. TUDO O QUE APRENDI |

## Shorts semanais

| Semana | Short | Tema |
|---:|---:|---|
| 1 | 01 | Por que o RPG começa pelo escopo, não pelo código |
| 2 | 02 | Monólito modular vs pastas controller/service/repository |
| 3 | 03 | Value Object não é frescura |
| 4 | 04 | Como testar sorte sem teste instável |
| 5 | 05 | Migration não é um SQL solto |
| 6 | 06 | Rollback de inventário em 30 segundos |
| 7 | 07 | Como permitir vários level ups de uma vez |
| 8 | 08 | Missão idempotente: recompensa apenas uma vez |
| 9 | 09 | DTO não é entidade JPA |
| 10 | 10 | Problem Details deixa a API previsível |
| 11 | 11 | Access token vs refresh token |
| 12 | 12 | JWT não resolve ownership |
| 13 | 13 | Mapa de RPG como grafo |
| 14 | 14 | Duas compras, um único item |
| 15 | 15 | Máquina de estados para missões |
| 16 | 16 | ArchUnit protegendo a arquitetura |
| 17 | 17 | Cobertura alta pode mentir |
| 18 | 18 | PostgreSQL real nos testes com Testcontainers |
| 19 | 19 | Bruno Runner validando a jornada inteira |
| 20 | 20 | N+1 visto no log e corrigido |
| 21 | 21 | Docker multi-stage reduzindo a imagem |
| 22 | 22 | Um PR profissional do início ao fim |
| 23 | 23 | O bug que virou teste de regressão |
| 24 | 24 | O que mudou depois de seis meses construindo |

## Estrutura obrigatória de cada episódio

1. **0:00-0:20 - Hook:** consequência ou problema concreto.
2. **0:20-0:50 - Promessa:** o que será construído e comprovado.
3. **0:50-2:00 - Contexto:** estado anterior e regra do produto.
4. **2:00-5:00 - Decisão:** alternativas e trade-off.
5. **5:00-11:00 - Construção:** somente trechos que mudam entendimento.
6. **11:00-14:00 - Teste e demo:** prova executável.
7. **14:00-16:00 - Erro e aprendizado:** o que falhou e por quê.
8. **Final - CTA:** release, issue, documentação ou próximo episódio.

## Checklist de gravação

- [ ] Limpar desktop, notificações e segredos.
- [ ] Aumentar fonte do editor e terminal.
- [ ] Gravar 1080p/60 ou 1440p/30.
- [ ] Capturar diagrama, código, teste, Bruno, banco e GitHub separadamente.
- [ ] Fazer commit antes e depois de cada trecho demonstrado.
- [ ] Não exibir token, senha, e-mail privado ou URL administrativa.
- [ ] Gravar demo final primeiro; depois narrar o caminho.
- [ ] Adicionar capítulos, links, tags e comentário fixado.
- [ ] Medir CTR, retenção aos 30s, duração média, cliques no GitHub e comentários em 48h/7d.

## Estrutura de arquivos de conteúdo

`youtube/ep-XX/{roteiro.md,thumbnail,raw,audio,project,export}`

## Regra editorial

Cada episódio precisa responder: qual problema existia, qual decisão foi tomada, como foi testada, qual foi o resultado e o que faria diferente.
