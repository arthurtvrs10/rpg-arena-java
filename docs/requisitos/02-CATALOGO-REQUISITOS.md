# Catálogo de requisitos

Todos os requisitos estão em estado **Aprovado**. A prioridade e a release-alvo fazem parte do contrato de planejamento.

## Identidade e sessão

| ID | Requisito funcional | Pri. | Release |
|---|---|:---:|:---:|
| RF-AUT-001 | O sistema deve cadastrar conta com e-mail, senha e nome público. | Must | v0.3 |
| RF-AUT-002 | O sistema deve normalizar e validar o e-mail antes de verificar unicidade. | Must | v0.3 |
| RF-AUT-003 | O sistema deve autenticar conta ativa e emitir access token. | Must | v0.3 |
| RF-AUT-004 | O sistema deve emitir refresh token rotativo associado a uma família de sessão. | Must | v0.3 |
| RF-AUT-005 | O sistema deve revogar a família quando detectar reutilização de refresh token. | Must | v0.3 |
| RF-AUT-006 | O sistema deve encerrar a sessão atual no logout. | Must | v0.3 |
| RF-AUT-007 | O jogador deve consultar e alterar apenas o próprio nome público. | Must | v0.3 |
| RF-AUT-008 | O administrador deve bloquear ou reativar conta, registrando motivo e autor. | Should | v0.4 |
| RF-AUT-009 | O sistema deve impedir autenticação e refresh de conta bloqueada. | Must | v0.3 |
| RF-AUT-010 | O sistema deve atribuir `PLAYER` por padrão e impedir autoatribuição de `ADMIN`. | Must | v0.3 |

## Personagem e progressão

| ID | Requisito funcional | Pri. | Release |
|---|---|:---:|:---:|
| RF-CHR-001 | O jogador deve criar personagem escolhendo nome e classe publicada. | Must | v0.1/v0.3 |
| RF-CHR-002 | O sistema deve limitar a três personagens ativos por conta. | Must | v0.1 |
| RF-CHR-003 | O jogador deve listar e detalhar apenas personagens próprios. | Must | v0.3 |
| RF-CHR-004 | O jogador deve arquivar personagem fora de batalha e sem transação pendente. | Should | v0.4 |
| RF-CHR-005 | O sistema deve inicializar nível, XP, atributos, posição e kit conforme classe publicada. | Must | v0.2 |
| RF-CHR-006 | O sistema deve aplicar dano, cura, mana e estados sem violar limites. | Must | v0.1 |
| RF-CHR-007 | O sistema deve conceder XP e processar múltiplas subidas de nível. | Must | v0.2 |
| RF-CHR-008 | O sistema deve impedir nível acima de 50 e converter XP excedente conforme regra. | Must | v0.2 |
| RF-CHR-009 | O jogador deve consultar atributos base, bônus e valores derivados separados. | Must | v0.2 |
| RF-CHR-010 | O sistema deve desbloquear habilidades ao atingir os requisitos publicados. | Must | v0.2 |
| RF-CHR-011 | O jogador deve consultar suas habilidades, custo, cooldown e elegibilidade. | Must | v0.3 |
| RF-CHR-012 | O sistema deve restaurar vida e mana ao subir de nível. | Should | v0.2 |

## Inventário, equipamento e loot

| ID | Requisito funcional | Pri. | Release |
|---|---|:---:|:---:|
| RF-INV-001 | O jogador deve consultar inventário paginado do próprio personagem. | Must | v0.3 |
| RF-INV-002 | O sistema deve armazenar itens empilháveis até o limite da definição. | Must | v0.2 |
| RF-INV-003 | O sistema deve rejeitar inclusão que exceda 40 pilhas sem alteração parcial. | Must | v0.2 |
| RF-INV-004 | O jogador deve equipar item possuído e compatível com o slot. | Must | v0.2 |
| RF-INV-005 | O jogador deve desequipar item, mantendo-o no inventário. | Must | v0.2 |
| RF-INV-006 | O sistema deve manter no máximo um item por slot. | Must | v0.2 |
| RF-INV-007 | O jogador deve consumir item elegível e aplicar seu efeito uma vez. | Must | v0.4 |
| RF-INV-008 | O sistema deve conceder loot com tabela e fonte aleatória reproduzíveis. | Must | v0.2 |
| RF-INV-009 | O sistema deve recalcular atributos derivados após equipar ou desequipar. | Must | v0.2 |
| RF-INV-010 | O sistema deve impedir uso, venda ou equipamento do mesmo item de forma concorrente. | Must | v0.4 |

## Combate

| ID | Requisito funcional | Pri. | Release |
|---|---|:---:|:---:|
| RF-CBT-001 | O jogador deve iniciar batalha PvE com personagem elegível e inimigo publicado. | Must | v0.1/v0.3 |
| RF-CBT-002 | O sistema deve criar snapshot de atributos e conteúdo usados na batalha. | Must | v0.2 |
| RF-CBT-003 | O sistema deve definir o primeiro turno pela velocidade. | Must | v0.1 |
| RF-CBT-004 | O jogador deve executar ataque básico somente no próprio turno. | Must | v0.1 |
| RF-CBT-005 | O jogador deve adotar defesa para reduzir o próximo dano recebido. | Must | v0.1 |
| RF-CBT-006 | O jogador deve usar habilidade conhecida com recurso e cooldown válidos. | Must | v0.2 |
| RF-CBT-007 | O jogador deve usar item consumível permitido durante a batalha. | Should | v0.4 |
| RF-CBT-008 | O jogador deve tentar fugir de encontro não marcado como chefe. | Should | v0.4 |
| RF-CBT-009 | O sistema deve aplicar e expirar efeitos de status por turno. | Should | v0.4 |
| RF-CBT-010 | O sistema deve registrar cada ação como evento imutável e ordenado. | Must | v0.2 |
| RF-CBT-011 | O sistema deve executar a decisão do inimigo após ação válida do jogador. | Must | v0.1 |
| RF-CBT-012 | O sistema deve finalizar batalha quando um participante atingir zero de vida ou a fuga for aceita. | Must | v0.1 |
| RF-CBT-013 | O sistema deve conceder resultado, XP e loot exatamente uma vez. | Must | v0.2 |
| RF-CBT-014 | O sistema deve tratar repetição de ação pela chave de idempotência. | Must | v0.3 |
| RF-CBT-015 | O sistema deve rejeitar atualização baseada em versão obsoleta. | Must | v0.3 |
| RF-CBT-016 | O jogador deve consultar estado e histórico resumido de batalha própria. | Must | v0.3 |
| RF-CBT-017 | O sistema deve impedir mais de uma batalha ativa por personagem. | Must | v0.2 |

## Missões e narrativa

| ID | Requisito funcional | Pri. | Release |
|---|---|:---:|:---:|
| RF-QST-001 | O jogador deve listar missões publicadas disponíveis ao personagem. | Must | v0.3 |
| RF-QST-002 | O sistema deve explicar pré-requisitos não atendidos sem revelar conteúdo oculto. | Should | v0.4 |
| RF-QST-003 | O jogador deve aceitar missão elegível e criar instância ligada à versão publicada. | Must | v0.2 |
| RF-QST-004 | O sistema deve avançar objetivos por eventos idempotentes. | Must | v0.2 |
| RF-QST-005 | O jogador deve escolher apenas opções disponíveis no nó narrativo atual. | Must | v0.4 |
| RF-QST-006 | O sistema deve aplicar consequências da escolha atomicamente. | Must | v0.4 |
| RF-QST-007 | O jogador deve abandonar missão abandonável. | Should | v0.4 |
| RF-QST-008 | O sistema deve falhar missão quando condição terminal configurada ocorrer. | Should | v0.4 |
| RF-QST-009 | O jogador deve resgatar recompensa de missão concluída. | Must | v0.2 |
| RF-QST-010 | O sistema deve conceder a recompensa de cada instância uma única vez. | Must | v0.2 |
| RF-QST-011 | O sistema deve preservar instâncias antigas quando uma nova versão for publicada. | Must | v0.4 |
| RF-QST-012 | O jogador deve consultar instâncias ativas e histórico pessoal. | Must | v0.3 |

## Mundo e exploração

| ID | Requisito funcional | Pri. | Release |
|---|---|:---:|:---:|
| RF-WLD-001 | O jogador deve consultar a localização atual e destinos adjacentes publicados. | Must | v0.4 |
| RF-WLD-002 | O jogador deve viajar apenas por conexão ativa a partir do local atual. | Must | v0.4 |
| RF-WLD-003 | O sistema deve validar custo, restrição de nível e bloqueios antes da viagem. | Must | v0.4 |
| RF-WLD-004 | O sistema deve atualizar custo e posição na mesma transação. | Must | v0.4 |
| RF-WLD-005 | O sistema deve sortear encontro elegível por fonte reproduzível. | Must | v0.4 |
| RF-WLD-006 | O sistema deve impedir viagem durante batalha ativa. | Must | v0.4 |
| RF-WLD-007 | O jogador deve consultar detalhes públicos do local sem conteúdo administrativo em rascunho. | Must | v0.4 |

## Economia e comerciantes

| ID | Requisito funcional | Pri. | Release |
|---|---|:---:|:---:|
| RF-ECO-001 | O jogador deve consultar comerciante ativo no mesmo local. | Must | v0.4 |
| RF-ECO-002 | O sistema deve apresentar preço efetivo e estoque atual. | Must | v0.4 |
| RF-ECO-003 | O jogador deve comprar quantidade válida com ouro e espaço suficientes. | Must | v0.4 |
| RF-ECO-004 | Compra deve debitar ouro, reduzir estoque, incluir item e registrar transação atomicamente. | Must | v0.4 |
| RF-ECO-005 | O jogador deve vender item elegível possuído e não equipado. | Must | v0.4 |
| RF-ECO-006 | Venda deve remover item, creditar ouro, ajustar estoque e registrar transação atomicamente. | Must | v0.4 |
| RF-ECO-007 | O sistema deve impedir ouro e estoque negativos. | Must | v0.4 |
| RF-ECO-008 | O sistema deve impedir duas compras vencedoras do último item. | Must | v0.4 |
| RF-ECO-009 | Repetição da mesma compra ou venda deve retornar o resultado anterior. | Must | v0.4 |
| RF-ECO-010 | O administrador deve repor ou ajustar estoque com auditoria e justificativa. | Should | v0.4 |

## Conteúdo administrativo

| ID | Requisito funcional | Pri. | Release |
|---|---|:---:|:---:|
| RF-ADM-001 | O administrador deve criar rascunho de classe, habilidade, item, inimigo, local, conexão, comerciante e missão. | Must | v0.4 |
| RF-ADM-002 | O administrador deve alterar apenas versões em rascunho. | Must | v0.4 |
| RF-ADM-003 | O sistema deve validar referências, estados, limites e schema antes de publicar. | Must | v0.4 |
| RF-ADM-004 | O administrador deve publicar uma nova versão válida. | Must | v0.4 |
| RF-ADM-005 | O sistema deve tornar versão publicada imutável. | Must | v0.4 |
| RF-ADM-006 | O administrador deve arquivar conteúdo, impedindo novas instâncias sem invalidar antigas. | Must | v0.4 |
| RF-ADM-007 | O sistema deve registrar autor, instante, versão, operação e resumo da alteração. | Must | v0.4 |
| RF-ADM-008 | O administrador deve paginar e filtrar conteúdo por tipo, código e estado. | Should | v0.4 |

## Ranking e operação

| ID | Requisito funcional | Pri. | Release |
|---|---|:---:|:---:|
| RF-RNK-001 | Qualquer pessoa deve consultar ranking público paginado. | Must | v0.3 |
| RF-RNK-002 | O sistema deve atualizar projeção após contabilizar batalha finalizada. | Must | v0.3 |
| RF-RNK-003 | O ranking deve permitir filtro controlado por classe. | Should | v1.0-rc |
| RF-RNK-004 | O ranking não deve expor e-mail, conta, token ou dados privados. | Must | v0.3 |
| RF-OPS-001 | A API deve fornecer liveness e readiness separados. | Must | v1.0-rc |
| RF-OPS-002 | A API deve publicar contrato OpenAPI da versão implementada. | Must | v0.3 |
| RF-OPS-003 | A coleção Bruno deve cobrir jornada feliz e falhas críticas. | Must | v0.3 |
| RF-OPS-004 | Toda requisição deve possuir `traceId` correlacionável nos logs e erros. | Must | v1.0-rc |
| RF-OPS-005 | O sistema deve expor métricas técnicas e de negócio sem alta cardinalidade. | Should | v1.0-rc |
| RF-OPS-006 | O sistema deve registrar eventos administrativos e de segurança em auditoria. | Must | v0.4 |

## Requisitos não funcionais

| ID | Categoria | Requisito verificável | Pri. |
|---|---|---|:---:|
| RNF-SEC-001 | Segurança | Todo endpoint privado deve autenticar e autorizar papel e propriedade no servidor. | Must |
| RNF-SEC-002 | Segurança | Senha deve ser armazenada somente por codificador suportado; token, senha e hash não podem aparecer em log ou resposta. | Must |
| RNF-SEC-003 | Segurança | Segredos devem vir de variáveis/secret store e nunca do Git. | Must |
| RNF-SEC-004 | Segurança | Payload deve usar allowlist; cliente não define papel, proprietário, dano, XP, preço, estoque ou timestamps. | Must |
| RNF-SEC-005 | Segurança | Dependências e imagem devem passar por verificação de vulnerabilidades antes da release. | Must |
| RNF-DAT-001 | Dados | Toda mudança de schema deve ser migration incremental; banco vazio deve alcançar a versão atual. | Must |
| RNF-DAT-002 | Dados | Operações identificadas como atômicas devem executar em uma única transação. | Must |
| RNF-DAT-003 | Dados | Unicidade e idempotência críticas devem possuir barreira no banco, não só validação prévia. | Must |
| RNF-DAT-004 | Dados | Instantes devem ser persistidos em UTC e identificadores em UUID. | Must |
| RNF-CON-001 | Concorrência | Batalha, inventário, estoque, missão e personagem devem detectar atualização perdida. | Must |
| RNF-API-001 | Contrato | API deve usar `/api/v1`, JSON UTF-8, ISO 8601 e Problem Details. | Must |
| RNF-API-002 | Contrato | Paginação deve ter ordenação determinística, padrão 20 e máximo 100. | Must |
| RNF-API-003 | Contrato | Mudança incompatível deve exigir nova versão ou adiamento após RC. | Must |
| RNF-PER-001 | Desempenho | Em ambiente de referência com 25 usuários concorrentes, leituras devem atingir p95 <= 400 ms e comandos p95 <= 800 ms, sem erro inesperado. | Should |
| RNF-PER-002 | Desempenho | Listagens não devem produzir N+1; consultas críticas devem possuir plano registrado. | Must |
| RNF-REL-001 | Confiabilidade | Repetição de comando idempotente não deve duplicar efeito, mesmo após timeout do cliente. | Must |
| RNF-REL-002 | Confiabilidade | Deploy deve possuir smoke test, rollback e backup documentados. | Must |
| RNF-TST-001 | Testabilidade | Regras de domínio não devem depender de Spring, JPA, relógio global ou aleatoriedade global. | Must |
| RNF-TST-002 | Testabilidade | Persistência crítica deve ser testada em PostgreSQL real via Testcontainers. | Must |
| RNF-TST-003 | Testabilidade | Cada regra crítica deve possuir teste feliz, erro e limite; cada risco crítico deve ter teste de mitigação. | Must |
| RNF-ARC-001 | Arquitetura | Dependências devem seguir `interfaces -> application -> domain`; infraestrutura implementa portas. | Must |
| RNF-ARC-002 | Arquitetura | Entidades JPA não devem ser expostas pelo HTTP e domínio não deve importar frameworks. | Must |
| RNF-OBS-001 | Observabilidade | Logs estruturados devem incluir traceId, operação e resultado sem dado sensível. | Must |
| RNF-OBS-002 | Observabilidade | Métricas não devem usar accountId, characterId ou token como label. | Must |
| RNF-OPS-001 | Portabilidade | Aplicação e PostgreSQL devem iniciar por Docker Compose em clone limpo. | Must |
| RNF-OPS-002 | Automação | Push e PR devem executar build, testes e quality gates. | Must |
| RNF-DOC-001 | Documentação | README, OpenAPI, Bruno, ADRs e diagramas devem refletir a release publicada. | Must |
| RNF-PRI-001 | Privacidade | O produto deve coletar somente e-mail e nome público; ranking deve expor apenas nome do personagem e dados de jogo. | Must |

## Requisitos Won't para 1.0

| ID | Requisito adiado | Motivo |
|---|---|---|
| RW-001 | PvP e multiplayer em tempo real | concorrência e infraestrutura fora do objetivo |
| RW-002 | Frontend completo | foco em backend e API-first |
| RW-003 | Pagamentos e marketplace | risco e domínio financeiro desnecessários |
| RW-004 | Microserviços e mensageria externa | complexidade sem escala comprovada |
| RW-005 | Recuperação de senha por e-mail | integração externa fora do recorte |
| RW-006 | IA generativa dentro do jogo | não contribui para os objetivos técnicos centrais |
