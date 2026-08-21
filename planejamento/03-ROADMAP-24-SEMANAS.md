# Roadmap de 24 semanas

## Visão mensal

| Mês | Semanas | Fase | Objetivo | Marco | Prova |
|---:|:---:|---|---|---|---|
| 1 | 1-4 | Núcleo jogável | Fechar escopo, arquitetura, personagem e combate determinístico. | v0.1.0 - batalha jogável sem banco | Testes demonstram criação de personagem e batalha completa. |
| 2 | 5-8 | Persistência e progressão | Persistir dados e entregar inventário, equipamentos, XP, habilidades e missões. | v0.2.0 - jornada persistente | Banco nasce por migrations e a jornada sobrevive a reinício. |
| 3 | 9-12 | API e segurança | Expor o jogo por REST com autenticação, autorização e ownership. | v0.3.0 - API segura | Bruno executa cadastro, login, personagem, batalha e missão. |
| 4 | 13-16 | Mundo e conteúdo | Adicionar exploração, encontros, NPCs, economia e missões ramificadas. | v0.4.0 - sistemas de mundo | Fluxo ponta a ponta inclui viagem, compra e escolha narrativa. |
| 5 | 17-20 | Qualidade e operação | Elevar testes, Docker, documentação, observabilidade, desempenho e segurança. | v1.0.0-rc.1 - candidato a release | CI, Docker, OpenAPI, métricas e quality gates funcionam. |
| 6 | 21-24 | Publicação e portfólio | Publicar, estabilizar, abrir colaboração e transformar o projeto em prova profissional. | v1.0.0 - release pública | Projeto online, documentado, demonstrável e usado em candidaturas. |

## Semanas

### Semana 01 - Produto, escopo e repositório

- **Período:** 24/08/2026 a 30/08/2026
- **Objetivo:** Transformar a ideia em um produto executável e público.
- **Entrega:** Repositório preparado, backlog priorizado e escopo fechado.
- **Conteúdo:** Episódio 01 / Short 01

- [ ] **RPG-M1-W01-01 - Definir visão e público:** A visão responde para quem, por quê, o que será entregue e como medir sucesso.
- [ ] **RPG-M1-W01-02 - Fechar MVP e não objetivos:** Todo item do MVP cabe em um dos seis marcos e o fora de escopo está explícito.
- [ ] **RPG-M1-W01-03 - Descrever jornadas e glossário:** Cada jornada tem fluxo principal, falhas, pré-condições e resultado.
- [ ] **RPG-M1-W01-04 - Criar repositório e metadados:** Repositório público apresenta descrição, licença, topics e regras de merge.
- [ ] **RPG-M1-W01-05 - Criar backlog, DoR e DoD:** Todas as issues do mês 1 têm aceite, prioridade, tamanho e evidência.
- [ ] **RPG-M1-W01-06 - Preparar identidade e trailer da série:** Trailer explica o desafio de seis meses e aponta para o repositório.

### Semana 02 - Arquitetura e ambiente profissional

- **Período:** 31/08/2026 a 06/09/2026
- **Objetivo:** Criar uma base técnica que suporte seis meses sem virar um projeto bagunçado.
- **Entrega:** Aplicação inicia, CI passa e arquitetura está registrada.
- **Conteúdo:** Episódio 01 / Short 02

- [ ] **RPG-M1-W02-01 - Definir monólito modular:** O diagrama mostra módulos e nenhuma regra depende de controller ou JPA.
- [ ] **RPG-M1-W02-02 - Criar projeto Java 21 e Spring Boot:** ./mvnw clean verify executa e /actuator/health responde UP.
- [ ] **RPG-M1-W02-03 - Criar árvore de pacotes:** Pacotes seguem o desenho e não existe pacote global service/controller/repository.
- [ ] **RPG-M1-W02-04 - Registrar ADRs iniciais:** Cada ADR contém contexto, opções, decisão, consequências e status.
- [ ] **RPG-M1-W02-05 - Configurar qualidade inicial:** PR de teste falha com teste quebrado e passa após correção; ambiente possui plano A e B.
- [ ] **RPG-M1-W02-06 - Publicar episódio 1:** Vídeo publicado, capítulos adicionados e links do repositório e playlist conferidos.

### Semana 03 - Domínio de personagem

- **Período:** 07/09/2026 a 13/09/2026
- **Objetivo:** Modelar regras usando objetos ricos, invariantes e casos de uso.
- **Entrega:** Personagem consistente, independente de Spring e banco.
- **Conteúdo:** Episódio 02 / Short 03

- [ ] **RPG-M1-W03-01 - Criar Value Objects do personagem:** Valores inválidos não existem e igualdade segue valor, não referência.
- [ ] **RPG-M1-W03-02 - Modelar classes e atributos iniciais:** Adicionar nova classe exige uma extensão localizada e testes deixam regras legíveis.
- [ ] **RPG-M1-W03-03 - Implementar agregado Character:** Métodos impedem cura acima do máximo, dano negativo e ações quando derrotado.
- [ ] **RPG-M1-W03-04 - Criar factory, portas e casos de uso:** Casos de uso não importam web/JPA e retornam erro explícito.
- [ ] **RPG-M1-W03-05 - Cobrir invariantes do personagem:** Caminho feliz, erro e limite de cada regra crítica estão cobertos.
- [ ] **RPG-M1-W03-06 - Produzir Short 3 e capturar episódio 2:** Short publicado e pasta do episódio contém gravações nomeadas.

### Semana 04 - Motor de combate determinístico

- **Período:** 14/09/2026 a 20/09/2026
- **Objetivo:** Entregar a primeira versão jogável com regras testáveis.
- **Entrega:** Batalha completa e release v0.1.0.
- **Conteúdo:** Episódio 02 / Short 04

- [ ] **RPG-M1-W04-01 - Especificar regras de combate:** Fórmulas, arredondamentos e casos extremos não possuem ambiguidade.
- [ ] **RPG-M1-W04-02 - Criar políticas de dano e aleatoriedade:** Mesma semente produz o mesmo histórico e dano nunca fica abaixo do mínimo.
- [ ] **RPG-M1-W04-03 - Modelar Battle e Turn:** Só o participante correto age e batalha encerrada é imutável.
- [ ] **RPG-M1-W04-04 - Implementar ações e efeitos:** Cada ação valida custo/alvo e gera evento de batalha auditável.
- [ ] **RPG-M1-W04-05 - Fechar suíte e release v0.1:** Suite reproduz batalha completa e release v0.1.0 pode ser executada pelo README.
- [ ] **RPG-M1-W04-06 - Publicar episódio 2:** Vídeo publicado com capítulos, thumbnail e link para v0.1.0.

### Semana 05 - PostgreSQL, Flyway e repositories

- **Período:** 21/09/2026 a 27/09/2026
- **Objetivo:** Persistir o núcleo sem contaminar o domínio.
- **Entrega:** Banco criado por migrations e repositories testados.
- **Conteúdo:** Episódio 03 / Short 05

- [ ] **RPG-M2-W05-01 - Desenhar modelo relacional:** ERD corresponde aos agregados e cada constraint tem justificativa.
- [ ] **RPG-M2-W05-02 - Criar baseline Flyway:** Banco vazio chega ao schema atual apenas ao iniciar a aplicação.
- [ ] **RPG-M2-W05-03 - Mapear entidades JPA:** O pacote domain não importa jakarta.persistence e round-trip mantém dados.
- [ ] **RPG-M2-W05-04 - Implementar adapters de repositório:** Casos de uso trabalham somente com interfaces do domínio/aplicação.
- [ ] **RPG-M2-W05-05 - Testar com PostgreSQL real:** Testes não usam H2 e executam localmente e no CI.
- [ ] **RPG-M2-W05-06 - Produzir Short 5 e capturar episódio 3:** Short publicado e gravações de migration/repository separadas por cena.

### Semana 06 - Inventário, equipamento e transações

- **Período:** 28/09/2026 a 04/10/2026
- **Objetivo:** Garantir consistência ao manipular itens e atributos.
- **Entrega:** Inventário transacional com concorrência testada.
- **Conteúdo:** Episódio 03 / Short 06

- [ ] **RPG-M2-W06-01 - Modelar catálogo de itens:** Tipos inválidos não são instanciados e catálogo é separado da posse.
- [ ] **RPG-M2-W06-02 - Implementar slots e pilhas:** Excesso de capacidade e item inexistente retornam erro de domínio sem alterar estado.
- [ ] **RPG-M2-W06-03 - Implementar equipar e desequipar:** Equipamento muda apenas stats derivados e rollback lógico mantém consistência.
- [ ] **RPG-M2-W06-04 - Criar tabela de recompensas:** Distribuição é reproduzível e configuração inválida falha cedo.
- [ ] **RPG-M2-W06-05 - Persistir e testar concorrência:** Uma falha não deixa estado parcial e conflito vira resposta de negócio controlada.
- [ ] **RPG-M2-W06-06 - Publicar episódio 3:** Vídeo publicado com demo de rollback e link para PRs.

### Semana 07 - Progressão, níveis e habilidades

- **Período:** 05/10/2026 a 11/10/2026
- **Objetivo:** Criar evolução de personagem extensível e auditável.
- **Entrega:** XP, level up e habilidades persistentes.
- **Conteúdo:** Episódio 04 / Short 07

- [ ] **RPG-M2-W07-01 - Definir curva de experiência:** A curva é calculável, monotônica e possui tabela de referência.
- [ ] **RPG-M2-W07-02 - Implementar ganho de XP:** XP não se perde, limite máximo é respeitado e múltiplos níveis têm teste.
- [ ] **RPG-M2-W07-03 - Modelar habilidades:** Uso inelegível não gasta recurso e explica a regra violada.
- [ ] **RPG-M2-W07-04 - Publicar eventos de domínio:** Handlers podem falhar de forma observável sem corromper o agregado.
- [ ] **RPG-M2-W07-05 - Persistir e testar progressão:** Todos os limites documentados têm teste e persistência mantém estado.
- [ ] **RPG-M2-W07-06 - Produzir Short 7 e capturar episódio 4:** Short publicado e roteiro visual do episódio revisado.

### Semana 08 - Missões e jornada persistente

- **Período:** 12/10/2026 a 18/10/2026
- **Objetivo:** Conectar combate, loot e progressão sem acoplamento direto.
- **Entrega:** Missão completa e release v0.2.0.
- **Conteúdo:** Episódio 04 / Short 08

- [ ] **RPG-M2-W08-01 - Separar definição e instância:** Alterar catálogo não muda progresso antigo silenciosamente.
- [ ] **RPG-M2-W08-02 - Criar máquina de estados:** Não é possível concluir sem objetivos nem resgatar duas vezes.
- [ ] **RPG-M2-W08-03 - Atualizar progresso por eventos:** Evento repetido não duplica progresso e só missões elegíveis avançam.
- [ ] **RPG-M2-W08-04 - Entregar recompensa atomicamente:** Toda recompensa é aplicada uma vez ou nenhuma alteração persiste.
- [ ] **RPG-M2-W08-05 - Fechar jornada e v0.2.0:** Jornada sobrevive a reinício e um terceiro a reproduz pelo README.
- [ ] **RPG-M2-W08-06 - Publicar episódio 4:** Vídeo, capítulos, thumbnail e release v0.2.0 estão publicados.

### Semana 09 - Contrato REST, DTOs e Bruno

- **Período:** 19/10/2026 a 25/10/2026
- **Objetivo:** Criar uma API previsível antes de expor todos os recursos.
- **Entrega:** Padrão HTTP, erros, validação e coleção Bruno.
- **Conteúdo:** Episódio 05 / Short 09

- [ ] **RPG-M3-W09-01 - Definir convenções REST:** Documento possui exemplos de sucesso e erro para cada convenção.
- [ ] **RPG-M3-W09-02 - Criar DTOs e mapeadores:** Nenhum controller retorna entidade JPA ou senha/token indevido.
- [ ] **RPG-M3-W09-03 - Implementar validação em camadas:** Payload inválido retorna 400 com lista de violações estável.
- [ ] **RPG-M3-W09-04 - Criar Problem Details global:** 400, 401, 403, 404, 409 e 500 seguem o mesmo formato.
- [ ] **RPG-M3-W09-05 - Montar coleção e ambientes:** Collection Runner executa health e primeiro CRUD sem editar URL.
- [ ] **RPG-M3-W09-06 - Produzir Short 9 e capturar episódio 5:** Short publicado e requests principais gravados em 1080p.

### Semana 10 - APIs de personagem e inventário

- **Período:** 26/10/2026 a 01/11/2026
- **Objetivo:** Expor os primeiros recursos com consultas e concorrência controladas.
- **Entrega:** Personagem e inventário consumíveis por HTTP.
- **Conteúdo:** Episódio 05 / Short 10

- [ ] **RPG-M3-W10-01 - Criar endpoints de personagem:** Bruno cobre 201, 200, 400, 404 e 409.
- [ ] **RPG-M3-W10-02 - Criar endpoints de inventário:** Responses mostram atributos derivados e falhas não deixam estado parcial.
- [ ] **RPG-M3-W10-03 - Adicionar paginação e filtros:** Parâmetros inválidos retornam 400 e consultas não usam full scan desnecessário.
- [ ] **RPG-M3-W10-04 - Aplicar optimistic locking e idempotência:** Requisições simultâneas não silenciam perda de atualização nem duplicam efeitos.
- [ ] **RPG-M3-W10-05 - Integrar OpenAPI e testes HTTP:** OpenAPI corresponde à implementação e CI executa testes HTTP.
- [ ] **RPG-M3-W10-06 - Publicar episódio 5:** Vídeo publicado e coleção Bruno linkada no repositório.

### Semana 11 - Contas, JWT e sessões

- **Período:** 02/11/2026 a 08/11/2026
- **Objetivo:** Autenticar sem expor credenciais e preparar autorização real.
- **Entrega:** Cadastro, login, refresh e logout seguros.
- **Conteúdo:** Episódio 06 / Short 11

- [ ] **RPG-M3-W11-01 - Modelar Account e roles:** Email é único e conta bloqueada não autentica.
- [ ] **RPG-M3-W11-02 - Implementar cadastro:** Banco só armazena hash e logs/responses não contêm segredo.
- [ ] **RPG-M3-W11-03 - Implementar login JWT:** Tokens adulterados, expirados ou de issuer incorreto são rejeitados.
- [ ] **RPG-M3-W11-04 - Implementar refresh rotativo:** Refresh reutilizado revoga a família e logout encerra a sessão.
- [ ] **RPG-M3-W11-05 - Criar matriz de permissões:** Matriz cobre todos os recursos e tem testes allow/deny.
- [ ] **RPG-M3-W11-06 - Produzir Short 11 e capturar episódio 6:** Short publicado e cenas de segurança não exibem segredo real.

### Semana 12 - Ownership e gameplay seguro

- **Período:** 09/11/2026 a 15/11/2026
- **Objetivo:** Impedir acesso horizontal e expor batalha/missões com segurança.
- **Entrega:** API segura e release v0.3.0.
- **Conteúdo:** Episódio 06 / Short 12

- [ ] **RPG-M3-W12-01 - Aplicar ownership de personagem:** Trocar characterId nunca concede acesso a outro jogador.
- [ ] **RPG-M3-W12-02 - Expor batalha:** Ação fora de turno, duplicada ou de não proprietário é recusada.
- [ ] **RPG-M3-W12-03 - Expor missões:** Recompensa não duplica e missão alheia retorna 403/404 conforme política.
- [ ] **RPG-M3-W12-04 - Criar suíte de segurança:** Todos os cenários allow/deny rodam no CI.
- [ ] **RPG-M3-W12-05 - Fechar v0.3.0:** Pessoa externa joga por HTTP usando apenas documentação e coleção.
- [ ] **RPG-M3-W12-06 - Publicar episódio 6:** Vídeo publicado com aviso para nunca versionar segredos.

### Semana 13 - Mundo, locais e exploração

- **Período:** 16/11/2026 a 22/11/2026
- **Objetivo:** Transformar módulos isolados em uma jornada de mundo.
- **Entrega:** Mapa em grafo, viagem e encontros.
- **Conteúdo:** Episódio 07 / Short 13

- [ ] **RPG-M4-W13-01 - Modelar regiões e locais:** Grafo rejeita conexão inválida e localização inexistente.
- [ ] **RPG-M4-W13-02 - Implementar viagem:** Não existe teletransporte indevido e custo é aplicado uma vez.
- [ ] **RPG-M4-W13-03 - Criar encontros configuráveis:** RandomSource torna encontro reproduzível e só opções elegíveis entram no sorteio.
- [ ] **RPG-M4-W13-04 - Persistir mapa e posição:** Banco novo recebe mapa válido e posição sobrevive a reinício.
- [ ] **RPG-M4-W13-05 - Expor mapa e viagem:** Bruno demonstra exploração completa e bloqueios.
- [ ] **RPG-M4-W13-06 - Produzir Short 13 e capturar episódio 7:** Short publicado e diagrama do mapa exportado.

### Semana 14 - NPCs, loja e economia

- **Período:** 23/11/2026 a 29/11/2026
- **Objetivo:** Criar transações econômicas sem exploit ou inconsistência.
- **Entrega:** Compra e venda concorrentes e seguras.
- **Conteúdo:** Episódio 07 / Short 14

- [ ] **RPG-M4-W14-01 - Modelar Money e preços:** Não há double, valor negativo, overflow silencioso ou preço fora da política.
- [ ] **RPG-M4-W14-02 - Modelar NPC e Merchant:** Comerciante só atende personagem elegível no mesmo local.
- [ ] **RPG-M4-W14-03 - Implementar compra transacional:** Falha em qualquer etapa não consome moeda nem estoque.
- [ ] **RPG-M4-W14-04 - Implementar venda e reposição:** Venda repetida e estoque negativo são impossíveis sob concorrência.
- [ ] **RPG-M4-W14-05 - Testar economia concorrente:** Somente uma compra vence e todos os saldos fecham.
- [ ] **RPG-M4-W14-06 - Publicar episódio 7:** Vídeo publicado com diagrama da transação e demo.

### Semana 15 - Missões ramificadas e diálogo

- **Período:** 30/11/2026 a 06/12/2026
- **Objetivo:** Permitir conteúdo narrativo sem hardcode no fluxo principal.
- **Entrega:** Escolhas, consequências e conteúdo versionado.
- **Conteúdo:** Episódio 08 / Short 15

- [ ] **RPG-M4-W15-01 - Definir schema narrativo:** Conteúdo inválido falha na carga com mensagem e caminho do campo.
- [ ] **RPG-M4-W15-02 - Implementar pré-requisitos e cadeias:** Sistema explica por que uma missão está bloqueada sem if espalhado.
- [ ] **RPG-M4-W15-03 - Modelar nós e escolhas:** Escolha inexistente, bloqueada ou repetida não altera estado.
- [ ] **RPG-M4-W15-04 - Aplicar efeitos e versionamento:** Nova publicação não corrompe jornada em andamento.
- [ ] **RPG-M4-W15-05 - Expor narrativa e validar contratos:** Fluxo ramificado completo roda no Bruno e no CI.
- [ ] **RPG-M4-W15-06 - Produzir Short 15 e capturar episódio 8:** Short publicado e árvore narrativa exportada.

### Semana 16 - Administração e publicação de conteúdo

- **Período:** 07/12/2026 a 13/12/2026
- **Objetivo:** Gerenciar conteúdo sem editar o banco manualmente.
- **Entrega:** API administrativa e release v0.4.0.
- **Conteúdo:** Episódio 08 / Short 16

- [ ] **RPG-M4-W16-01 - Definir RBAC administrativo:** PLAYER não acessa endpoints admin e testes cobrem cada permissão.
- [ ] **RPG-M4-W16-02 - Criar CRUD de conteúdo:** Operações usam DTO, validação, paginação e auditoria.
- [ ] **RPG-M4-W16-03 - Criar rascunho e publish:** Somente versão válida fica ativa e instâncias antigas mantêm referência.
- [ ] **RPG-M4-W16-04 - Registrar ações administrativas:** É possível identificar quem alterou e publicou cada versão.
- [ ] **RPG-M4-W16-05 - Executar ArchUnit e fechar v0.4:** Build falha em violação arquitetural e v0.4.0 demonstra conteúdo administrável.
- [ ] **RPG-M4-W16-06 - Publicar episódio 8:** Vídeo publicado com fluxo draft -> publish -> jogo.

### Semana 17 - Estratégia de testes e cobertura útil

- **Período:** 14/12/2026 a 20/12/2026
- **Objetivo:** Criar uma rede de segurança baseada em riscos, não em números vazios.
- **Entrega:** Suíte organizada, rápida e auditável.
- **Conteúdo:** Episódio 09 / Short 17

- [ ] **RPG-M5-W17-01 - Escrever estratégia de testes:** Cada risco crítico possui tipo, camada, dado e objetivo de teste.
- [ ] **RPG-M5-W17-02 - Completar testes de domínio:** Cada regra crítica possui caminho feliz, erro e limite.
- [ ] **RPG-M5-W17-03 - Criar Test Data Builders:** Testes ficam independentes, legíveis e sem estado compartilhado.
- [ ] **RPG-M5-W17-04 - Padronizar Testcontainers:** Suíte roda local/CI sem banco instalado e sem ordem entre testes.
- [ ] **RPG-M5-W17-05 - Configurar JaCoCo:** Queda abaixo do limite bloqueia PR e exclusões estão justificadas.
- [ ] **RPG-M5-W17-06 - Produzir Short 17 e capturar episódio 9:** Short publicado e relatórios/execuções gravados.

### Semana 18 - Docker e execução reproduzível

- **Período:** 21/12/2026 a 27/12/2026
- **Objetivo:** Fazer qualquer pessoa executar o projeto com um comando.
- **Entrega:** Imagem, Compose, healthchecks e onboarding.
- **Conteúdo:** Episódio 09 / Short 18

- [ ] **RPG-M5-W18-01 - Criar Dockerfile multi-stage:** Imagem inicia, não contém fonte/segredo desnecessário e executa sem root.
- [ ] **RPG-M5-W18-02 - Criar Compose API + PostgreSQL:** docker compose up --build inicia ambiente do zero.
- [ ] **RPG-M5-W18-03 - Separar profiles e segredos:** Nenhum segredo real está no Git e produção falha cedo sem configuração.
- [ ] **RPG-M5-W18-04 - Adicionar readiness e liveness:** Compose e plataforma detectam indisponibilidade corretamente.
- [ ] **RPG-M5-W18-05 - Criar comandos e build de imagem:** Novo colaborador executa tudo em até 15 minutos e CI gera imagem.
- [ ] **RPG-M5-W18-06 - Publicar episódio 9:** Vídeo publicado e setup foi testado em clone limpo.

### Semana 19 - Documentação executável

- **Período:** 28/12/2026 a 03/01/2027
- **Objetivo:** Eliminar dependência de explicação verbal para usar ou contribuir.
- **Entrega:** README, OpenAPI, Bruno e arquitetura atualizados.
- **Conteúdo:** Episódio 10 / Short 19

- [ ] **RPG-M5-W19-01 - Finalizar README principal:** Pessoa externa entende e executa o projeto sem mensagem privada.
- [ ] **RPG-M5-W19-02 - Completar OpenAPI:** Todos os endpoints públicos aparecem e exemplos correspondem aos testes.
- [ ] **RPG-M5-W19-03 - Automatizar collection runner:** Runner executa local e público sem edição manual.
- [ ] **RPG-M5-W19-04 - Atualizar diagramas e ADRs:** Diagramas refletem o código e decisões possuem status correto.
- [ ] **RPG-M5-W19-05 - Criar guia de onboarding:** Contribuidor realiza primeira mudança seguindo apenas o guia.
- [ ] **RPG-M5-W19-06 - Produzir Short 19 e capturar episódio 10:** Short publicado e assets de documentação organizados.

### Semana 20 - Observabilidade, desempenho e segurança

- **Período:** 04/01/2027 a 10/01/2027
- **Objetivo:** Transformar a aplicação em candidato a produção.
- **Entrega:** Logs, métricas, revisão OWASP e release candidate.
- **Conteúdo:** Episódio 10 / Short 20

- [ ] **RPG-M5-W20-01 - Implementar logs estruturados:** Uma requisição é rastreável do HTTP ao banco sem dado sensível.
- [ ] **RPG-M5-W20-02 - Adicionar métricas técnicas e de negócio:** Métricas respondem e não criam cardinalidade por usuário/personagem.
- [ ] **RPG-M5-W20-03 - Analisar queries e índices:** Relatório compara plano antes/depois e remove N+1.
- [ ] **RPG-M5-W20-04 - Executar revisão OWASP:** Checklist possui evidência e issue para cada risco restante.
- [ ] **RPG-M5-W20-05 - Criar quality gates e RC:** Main só recebe merge verde e RC passa regressão completa.
- [ ] **RPG-M5-W20-06 - Publicar episódio 10:** Vídeo publicado com resultados antes/depois e limites honestos.

### Semana 21 - Deploy e operação

- **Período:** 11/01/2027 a 17/01/2027
- **Objetivo:** Publicar com procedimentos de recuperação e verificação.
- **Entrega:** API HTTPS, banco gerenciado, smoke e monitoramento.
- **Conteúdo:** Episódio 11 / Short 21

- [ ] **RPG-M6-W21-01 - Escolher plataforma e registrar ADR:** ADR explica critérios, escolha, riscos e plano de saída.
- [ ] **RPG-M6-W21-02 - Provisionar banco e aplicação:** API responde por HTTPS e banco aceita apenas conexão necessária.
- [ ] **RPG-M6-W21-03 - Controlar migrations em produção:** Deploy concorrente não executa migration perigosa duas vezes.
- [ ] **RPG-M6-W21-04 - Criar backup e rollback:** Runbook registra RPO/RTO aproximados e evidência do ensaio.
- [ ] **RPG-M6-W21-05 - Automatizar smoke e alertas:** Smoke pós-deploy passa e cada alerta aponta para ação do runbook.
- [ ] **RPG-M6-W21-06 - Produzir Short 21 e capturar episódio 11:** Short publicado sem expor credencial e gravações organizadas.

### Semana 22 - Governança open source

- **Período:** 18/01/2027 a 24/01/2027
- **Objetivo:** Permitir colaboração real com histórico profissional.
- **Entrega:** Community files, templates e contribuição simulada.
- **Conteúdo:** Episódio 11 / Short 22

- [ ] **RPG-M6-W22-01 - Revisar licença e terceiros:** Nenhum asset/dependência está sem licença compatível conhecida.
- [ ] **RPG-M6-W22-02 - Adicionar conduta, segurança e suporte:** Repositório informa comportamento, vulnerabilidades e dúvidas.
- [ ] **RPG-M6-W22-03 - Criar templates de issue e PR:** Toda nova issue/PR nasce com informações acionáveis.
- [ ] **RPG-M6-W22-04 - Organizar labels, milestones e board:** Backlog público é filtrável e cada issue tem próximo passo.
- [ ] **RPG-M6-W22-05 - Simular contribuição externa:** Histórico prova o fluxo profissional do início ao fim.
- [ ] **RPG-M6-W22-06 - Publicar episódio 11:** Vídeo publicado e repositório recebe chamadas para contribuição.

### Semana 23 - Estabilização e release candidate

- **Período:** 25/01/2027 a 31/01/2027
- **Objetivo:** Eliminar bloqueadores antes da versão 1.0.
- **Entrega:** RC aprovada, changelog e relatório de carga.
- **Conteúdo:** Episódio 12 / Short 23

- [ ] **RPG-M6-W23-01 - Executar bug bash:** Cada falha possui passos, evidência, impacto e decisão.
- [ ] **RPG-M6-W23-02 - Resolver blockers e regressões:** Nenhum blocker/critical fica aberto e CI permanece verde.
- [ ] **RPG-M6-W23-03 - Executar teste de carga mínimo:** Relatório contém p50/p95/p99, erros, gargalo e limite conhecido.
- [ ] **RPG-M6-W23-04 - Fazer revisão final:** Nenhum finding crítico/alto permanece sem mitigação documentada.
- [ ] **RPG-M6-W23-05 - Preparar changelog e upgrade:** Changelog reconcilia PRs e um usuário da v0.4 atualiza para RC.
- [ ] **RPG-M6-W23-06 - Produzir Short 23 e capturar episódio final:** Short publicado e demo final possui backup de gravação.

### Semana 24 - Release 1.0, portfólio e mercado

- **Período:** 01/02/2027 a 07/02/2027
- **Objetivo:** Transformar o projeto concluído em prova pública de competência.
- **Entrega:** v1.0.0, case study, demo e candidaturas iniciadas.
- **Conteúdo:** Episódio 12 / Short 24

- [ ] **RPG-M6-W24-01 - Publicar v1.0.0:** Release pública corresponde ao commit implantado e smoke passa.
- [ ] **RPG-M6-W24-02 - Escrever estudo de caso:** Case possui evidências, links e decisões explicadas com suas palavras.
- [ ] **RPG-M6-W24-03 - Gravar demonstração técnica:** Demo prova funcionamento sem depender de cortes confusos.
- [ ] **RPG-M6-W24-04 - Atualizar GitHub e currículo:** Recrutador encontra contexto, código, execução e resultados em poucos minutos.
- [ ] **RPG-M6-W24-05 - Iniciar candidaturas e feedback:** Candidaturas começaram antes de qualquer sensação de perfeição e feedback vira issue/estudo.
- [ ] **RPG-M6-W24-06 - Publicar episódio 12 e encerrar a temporada:** Final publicado com playlist completa, CTA para repositório e retrospectiva após 7 dias.
