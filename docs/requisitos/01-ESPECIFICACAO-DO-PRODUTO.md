# Especificação do produto — RPG Arena API

## 1. Visão

Para estudantes e avaliadores técnicos que precisam enxergar engenharia de software além de CRUD, o RPG Arena é uma API open source de RPG por turnos que transforma regras de jogo em comportamentos seguros, persistentes e testáveis. O produto demonstra domínio rico, transações, concorrência, autenticação, autorização, observabilidade e entrega profissional em um cenário compreensível.

## 2. Problema

Projetos de portfólio frequentemente exibem apenas tabelas e endpoints sem regras difíceis. Eles não provam como o desenvolvedor trata estados, acesso horizontal, repetição de requisições, atualização concorrente, consistência de dados ou evolução de arquitetura. O RPG Arena usa uma jornada de jogo para tornar essas competências observáveis por código, testes, API, documentação e vídeo.

## 3. Objetivos do produto

1. Entregar uma jornada jogável completa por API.
2. Manter o progresso consistente sob falhas, repetição e concorrência.
3. Impedir que uma conta acesse recursos privados de outra.
4. Permitir publicação administrativa de conteúdo versionado.
5. Ser executável por outra pessoa sem ajuda privada.
6. Produzir evidências técnicas para GitHub, YouTube e processos seletivos.

## 4. Atores e interesses

### Visitante

Consulta informações públicas, cria conta, autentica e consulta ranking. Não acessa progresso privado.

### Jogador (`PLAYER`)

Mantém o próprio perfil, personagens, inventários, missões, batalhas, posição e transações. Nunca escolhe o proprietário de um recurso por payload.

### Administrador de conteúdo (`ADMIN`)

Cria, valida, publica e arquiva classes, habilidades, itens, inimigos, locais, comerciantes e missões. Não assume silenciosamente a identidade de jogador.

### Operador técnico

Implanta, monitora, restaura e investiga a aplicação. Atua pela plataforma e runbooks, não por um papel de gameplay.

### Avaliador ou contribuidor

Clona o projeto, executa testes, usa a coleção Bruno, lê decisões e propõe mudanças pelo GitHub. Não é um ator autenticado do produto.

## 5. Jornada principal de demonstração

1. Visitante registra conta e autentica.
2. Jogador cria `Arin`, classe `WARRIOR`, no nível 1.
3. Sistema concede equipamento inicial e posiciona o personagem em `VILA_DE_ASTER`.
4. Jogador consulta locais vizinhos e aceita `ECOS_DA_FLORESTA`.
5. Jogador viaja para `FLORESTA_SUSSURRANTE` e gera um encontro reproduzível.
6. Jogador inicia batalha contra `LOBO_CINZENTO`.
7. Jogador ataca, defende, usa habilidade e encerra a batalha.
8. Sistema registra loot, XP, progresso de missão e ranking sem duplicar efeitos.
9. Jogador volta à vila, vende loot e compra uma poção.
10. Jogador toma uma decisão narrativa, conclui a missão e resgata a recompensa uma única vez.
11. Jogador consulta o ranking.
12. Um segundo usuário tenta usar os IDs de Arin e recebe 404 sem dados vazados.

## 6. Escopo funcional da versão 1.0

### Identidade e acesso

Cadastro, login, refresh rotativo, logout, perfil próprio, bloqueio administrativo, papéis e auditoria de eventos de segurança.

### Personagem e progressão

Criação, listagem, detalhe, arquivamento, classe, atributos, vida, mana, experiência, níveis, habilidades desbloqueadas e posição.

### Inventário e equipamento

Pilhas, capacidade, equipamento por slot, consumíveis, loot e recalculo de atributos derivados.

### Combate

Batalha PvE por turnos, snapshot dos participantes, ataque, defesa, habilidade, item, efeitos de status, fuga, histórico, idempotência e concorrência.

### Missões e narrativa

Catálogo publicado, pré-requisitos, objetivos, progresso por eventos, escolhas, consequências, abandono, falha, conclusão e recompensa única.

### Mundo e exploração

Regiões, locais, conexões, custo de viagem, posição persistente e encontros configurados.

### Economia

Moeda, comerciante, estoque, compra, venda, reposição administrativa e livro de transações.

### Conteúdo administrativo

Criação de rascunho, validação, publicação, arquivamento, versionamento e auditoria dos catálogos.

### Ranking e operação

Ranking público paginado, OpenAPI, Bruno, healthchecks, logs correlacionados, métricas, Docker, CI e deploy.

## 7. Fora do escopo

- frontend completo, jogo gráfico ou game engine;
- aplicativo mobile;
- PvP, multiplayer em tempo real, chat, guildas e amigos;
- pagamentos, moeda real, marketplace ou monetização;
- mapas procedurais e geração de conteúdo por IA;
- e-mail, recuperação de senha e autenticação social;
- microserviços, Kafka, Kubernetes e service mesh;
- alta disponibilidade multi-região;
- moderação de comunidade dentro do jogo;
- compatibilidade retroativa com dados anteriores à primeira release pública.

## 8. Épicos e resultados

| Épico | Resultado demonstrável | Release |
|---|---|---|
| EP-01 Fundação | build, CI, módulos e ADRs | v0.1.0 |
| EP-02 Personagem | personagem válido e progressão pura | v0.1.0 |
| EP-03 Combate | batalha completa em memória | v0.1.0 |
| EP-04 Persistência | schema por migrations e repositories | v0.2.0 |
| EP-05 Inventário | equipar/consumir com transação | v0.2.0 |
| EP-06 Missões | progresso e recompensa única | v0.2.0 |
| EP-07 API | contratos previsíveis e coleção Bruno | v0.3.0 |
| EP-08 Segurança | autenticação, refresh, RBAC e ownership | v0.3.0 |
| EP-09 Mundo | mapa, viagem e encontros | v0.4.0 |
| EP-10 Economia | compra/venda concorrente | v0.4.0 |
| EP-11 Conteúdo | narrativa e publicação versionada | v0.4.0 |
| EP-12 Qualidade | testes, Docker, observabilidade e performance | v1.0.0-rc.1 |
| EP-13 Publicação | deploy, governança e release pública | v1.0.0 |

## 9. Critérios de sucesso

- Uma pessoa externa executa o ambiente seguindo apenas o README.
- A coleção Bruno reproduz a jornada principal sem editar URLs manualmente.
- Todos os requisitos Must possuem teste e evidência.
- Nenhum teste de ownership permite acesso cruzado.
- Repetir ação, recompensa ou compra com a mesma chave não duplica efeito.
- Concorrência sobre o mesmo turno ou último estoque produz um vencedor consistente.
- Banco vazio chega ao estado atual somente por migrations.
- API publicada responde por HTTPS e possui smoke test.
- Nenhum segredo aparece no Git, log ou resposta.
- O repositório explica decisões, limitações e riscos conhecidos.
- As 12 publicações principais demonstram problema, decisão, implementação, teste e resultado.

## 10. Releases e gates

### v0.1.0 — núcleo jogável

Personagem e batalha determinística funcionam em Java puro. Gate: suíte unitária reproduz uma batalha completa.

### v0.2.0 — jornada persistente

PostgreSQL, inventário, progressão e missão persistem. Gate: reinício não perde progresso; rollback e idempotência são testados.

### v0.3.0 — API segura

REST, JWT, refresh, RBAC e ownership. Gate: Bruno executa a jornada e a suíte rejeita acesso cruzado.

### v0.4.0 — mundo e conteúdo

Viagem, encontros, economia, narrativa e administração. Gate: jogador percorre o fluxo completo usando conteúdo publicado.

### v1.0.0-rc.1 — candidato operável

Testes, Docker, OpenAPI, logs, métricas, performance e revisão de segurança. Gate: regressão, quality gates e setup limpo aprovados.

### v1.0.0 — release pública

Deploy, runbooks, governança open source, case study e temporada concluída. Gate: smoke em produção e nenhum blocker aberto.

## 11. Política de prioridade

- **Must:** necessário para jornada, integridade, segurança ou operação mínima.
- **Should:** aumenta qualidade e demonstração, mas pode ser simplificado sem quebrar a jornada.
- **Could:** extensão somente após todos os Must.
- **Won't 1.0:** explicitamente adiado.

Se o prazo cair, reduza filtros, efeitos, endpoints administrativos e detalhes de histórico. Não remova ownership, transação de recompensa, idempotência, teste crítico, migrations ou execução reproduzível.
