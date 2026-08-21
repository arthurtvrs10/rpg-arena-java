# Escopo do produto — versão anterior de 30 dias

> **REFERÊNCIA ANTERIOR:** a especificação oficial atual está em `../requisitos/01-ESPECIFICACAO-DO-PRODUTO.md`.

Documento pronto para ser publicado no repositório como docs/PRODUCT-SCOPE.md.

## 1. Resumo

RPG Arena é uma API REST de RPG por turnos. Jogadores autenticados criam personagens, administram inventário, realizam missões, executam ações de combate e consultam um ranking. O projeto demonstra modelagem de domínio, segurança por propriedade, consistência transacional, concorrência, testes automatizados e entrega de uma aplicação Java.

## 2. Problema

Projetos de portfólio frequentemente demonstram apenas operações CRUD. Eles não evidenciam decisões sobre regras, transições de estado, concorrência, idempotência, autorização ou qualidade de entrega. O RPG Arena usa um domínio compreensível para tornar essas decisões visíveis e testáveis.

## 3. Usuários

### Jogador

Quer criar e evoluir personagens, administrar equipamentos, completar missões e lutar sem que outra conta consiga alterar seus recursos.

### Administrador

Quer manter catálogos de classes, itens, habilidades e missões, sem acesso irrestrito acidental às credenciais dos jogadores.

### Avaliador técnico

Quer executar o sistema, ler decisões, reproduzir testes e entender os trade-offs sem depender de explicação externa.

## 4. Objetivo do MVP

Permitir o ciclo completo:

1. criar conta e autenticar;
2. criar um personagem;
3. consultar inventário e equipar item;
4. iniciar e concluir missão;
5. receber recompensa exatamente uma vez;
6. iniciar uma batalha;
7. agir apenas no próprio turno;
8. concluir a batalha sem ações duplicadas;
9. consultar ranking;
10. executar e testar tudo localmente com comandos documentados.

## 5. Funcionalidades incluídas

| Épico | Capacidade |
|---|---|
| Identidade | Cadastro, login, JWT, papéis PLAYER e ADMIN |
| Jogador | Perfil próprio e isolamento por identidade autenticada |
| Personagem | Criar, listar, detalhar, evoluir e consultar atributos |
| Inventário | Listar itens, equipar, desequipar e validar slot |
| Missão | Iniciar, concluir ou falhar segundo máquina de estados |
| Recompensa | Conceder XP e item uma única vez |
| Batalha | Criar batalha PvE, executar turno, habilidade e finalizar |
| Ranking | Listar classificação paginada por vitórias e nível |
| Administração | Manter catálogos necessários ao jogo |
| Operação | Healthcheck, logs, OpenAPI, Docker Compose e CI |

## 6. Fora do escopo

- interface gráfica ou motor de jogo;
- aplicativo mobile;
- PvP em tempo real;
- chat, guildas ou amigos;
- pagamentos, loja e marketplace;
- mapas procedurais;
- inimigos gerados por inteligência artificial;
- microsserviços, mensageria e Kubernetes;
- recuperação de senha por e-mail;
- alta disponibilidade multi-região.

## 7. Regras centrais

1. Uma conta ativa pode possuir no máximo três personagens.
2. O nome do personagem é único sem diferenciar maiúsculas de minúsculas.
3. Um jogador só consulta ou altera personagens que lhe pertencem.
4. Um item equipado deve existir no inventário do personagem.
5. O slot do item deve ser compatível e comporta somente um item.
6. Uma missão segue DRAFT, ACTIVE, COMPLETED ou FAILED; estados terminais não mudam.
7. A recompensa de uma tentativa concluída é aplicada exatamente uma vez.
8. Uma batalha segue CREATED, IN_PROGRESS, FINISHED ou CANCELLED.
9. Somente o participante do turno atual pode agir.
10. Personagem derrotado não executa ação.
11. Habilidade exige recurso suficiente e cooldown zerado.
12. A mesma requisição de ação não pode produzir efeitos duas vezes.
13. Atualizações concorrentes da mesma batalha devem gerar uma vencedora e uma rejeitada/reprocessada de forma explícita.
14. O ranking só considera batalhas finalizadas e contabilizadas.

## 8. Requisitos não funcionais

| Categoria | Requisito verificável |
|---|---|
| Segurança | Nenhum endpoint de jogador confia em playerId enviado pelo cliente para autorizar propriedade |
| Consistência | Recompensa e atualização de missão acontecem na mesma transação |
| Concorrência | Batalha usa controle otimista de versão |
| Idempotência | Ação e recompensa repetidas não duplicam efeito |
| Dados | Schema nasce exclusivamente por migrations versionadas |
| Testes | Regras puras têm unitários; persistência crítica usa PostgreSQL real em container |
| Contrato | Erros possuem formato estável, código, mensagem, caminho e timestamp |
| Operação | Aplicação e banco sobem por Docker Compose com healthcheck |
| Automação | Push e pull request executam build e testes |
| Documentação | README permite executar o projeto do zero |

## 9. Histórias prioritárias

### US-01 — Criar conta

Como visitante, quero criar uma conta para acessar o jogo.

Critérios:

- e-mail válido e único;
- senha armazenada somente como hash forte;
- resposta nunca expõe hash;
- conflito retorna código de erro estável.

### US-02 — Autenticar

Como jogador, quero receber um token para acessar meus recursos.

Critérios:

- credenciais inválidas não revelam se o e-mail existe;
- token contém identidade e papel mínimos;
- token expirado é rejeitado.

### US-03 — Criar personagem

Como jogador, quero criar um personagem de uma classe disponível.

Critérios:

- limite de três;
- nome único;
- atributos iniciais vêm da classe;
- personagem nasce no nível um.

### US-04 — Equipar item

Como jogador, quero equipar um item do meu inventário.

Critérios:

- personagem e item pertencem ao jogador autenticado;
- slot é compatível;
- troca é atômica;
- atributos derivados são recalculados.

### US-05 — Concluir missão

Como jogador, quero concluir uma missão válida e receber recompensa.

Critérios:

- apenas tentativa ativa pode concluir;
- requisitos são verificados;
- tentativa e recompensa são persistidas juntas;
- repetição não duplica XP ou item.

### US-06 — Executar ação de batalha

Como jogador, quero atacar ou usar habilidade no meu turno.

Critérios:

- batalha está em andamento;
- ator é dono do turno e está vivo;
- recurso e cooldown são válidos;
- ação repetida é idempotente;
- versão concorrente é tratada.

### US-07 — Consultar ranking

Como visitante, quero consultar o ranking sem expor dados privados.

Critérios:

- paginação obrigatória;
- ordenação determinística;
- apenas apelido público e dados de jogo;
- consulta apoiada por índice verificado.

## 10. Contrato inicial de endpoints

| Método | Rota | Acesso | Objetivo |
|---|---|---|---|
| POST | /api/v1/auth/register | Público | Criar conta |
| POST | /api/v1/auth/login | Público | Autenticar |
| GET | /api/v1/me | PLAYER | Perfil próprio |
| POST | /api/v1/characters | PLAYER | Criar personagem |
| GET | /api/v1/characters | PLAYER | Listar próprios personagens |
| GET | /api/v1/characters/{id} | PLAYER | Detalhar se for proprietário |
| GET | /api/v1/characters/{id}/inventory | PLAYER | Consultar inventário próprio |
| PUT | /api/v1/characters/{id}/equipment/{slot} | PLAYER | Equipar item |
| DELETE | /api/v1/characters/{id}/equipment/{slot} | PLAYER | Desequipar |
| POST | /api/v1/characters/{id}/missions/{missionId}/attempts | PLAYER | Iniciar missão |
| POST | /api/v1/mission-attempts/{id}/complete | PLAYER | Concluir tentativa |
| POST | /api/v1/characters/{id}/battles | PLAYER | Iniciar batalha PvE |
| POST | /api/v1/battles/{id}/actions | PLAYER | Executar ação |
| GET | /api/v1/battles/{id} | PLAYER | Consultar batalha própria |
| GET | /api/v1/rankings | Público | Consultar ranking |
| POST | /api/v1/admin/items | ADMIN | Criar item de catálogo |
| POST | /api/v1/admin/missions | ADMIN | Criar missão |

## 11. Métricas de sucesso do projeto

- fluxo principal reproduzido do zero no Bruno;
- zero endpoint de proprietário vulnerável a troca simples de identificador;
- recompensas duplicadas iguais a zero nos testes concorrentes;
- build e testes automatizados verdes;
- setup local concluído por outra pessoa apenas com README;
- todas as decisões críticas ligadas a requisito ou risco;
- demonstração gravada em até oito minutos;
- pelo menos 14 candidaturas personalizadas ao longo das quatro sprints.

## 12. Critério de release 1.0.0

O MVP pode receber a tag 1.0.0 quando todas as histórias Must estão concluídas, migrations funcionam em banco vazio, suíte está verde, coleção Bruno executa o fluxo principal, Docker Compose sobe serviços saudáveis, pipeline está verde, README foi testado e riscos conhecidos estão documentados.
