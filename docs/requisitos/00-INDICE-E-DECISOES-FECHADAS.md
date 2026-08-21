# Índice da análise de requisitos e decisões fechadas

Versão da especificação: **1.0**  
Produto: **RPG Arena API**  
Baseline: **20/08/2026**  
Responsável: **Arthur Tavares**  
Estado: **Aprovada para desenvolvimento**

## Objetivo deste conjunto

Eliminar decisões abertas que impediriam a implementação. Os documentos abaixo definem o produto, o comportamento observável, as regras, os dados, a segurança, os testes e a ordem de entrega. Quando uma mudança for necessária, abra uma issue `change-request`, avalie impacto e atualize a versão da especificação.

## Documentos obrigatórios

| Ordem | Documento | Uso |
|---:|---|---|
| 1 | `01-ESPECIFICACAO-DO-PRODUTO.md` | visão, atores, jornadas, escopo e releases |
| 2 | `02-CATALOGO-REQUISITOS.md` | requisitos funcionais e não funcionais numerados |
| 3 | `03-REGRAS-DE-NEGOCIO.md` | invariantes, fórmulas, limites e erros |
| 4 | `04-CASOS-DE-USO.md` | fluxos principais, alternativos e exceções |
| 5 | `05-HISTORIAS-E-CRITERIOS-BDD.md` | backlog funcional e cenários de aceite |
| 6 | `06-MATRIZ-PERMISSOES-E-SEGURANCA.md` | autenticação, RBAC, ownership e ameaças |
| 7 | `07-RISCOS-PREMISSAS-RESTRICOES.md` | riscos, mitigação e limites assumidos |
| 8 | `08-MATRIZ-DE-RASTREABILIDADE.md` | ligação entre requisito, regra, caso, semana e teste |
| 9 | `09-PLANO-DE-HOMOLOGACAO.md` | como provar que a versão pode ser liberada |
| 10 | `10-ORDEM-EXATA-DE-IMPLEMENTACAO.md` | sequência técnica sem dependências circulares |
| 11 | `11-GLOSSARIO.md` | significado único dos termos do produto |
| 12 | `12-CATALOGO-DE-ERROS.md` | códigos e status estáveis |
| 13 | `13-MAPA-STATUS-IMPLEMENTACAO.md` | diferença entre planejado e entregue |
| 14 | `14-STAKEHOLDERS-PERSONAS-JORNADAS.md` | públicos, necessidades e fluxos ponta a ponta |
| 15 | `15-CATALOGO-DE-EVENTOS.md` | eventos, payloads e consumidores |
| 16 | `../dados/MODELO-E-DICIONARIO-DE-DADOS.md` | tabelas, campos, chaves, índices e transações |
| 17 | `../api/openapi.yaml` | contrato HTTP inicial da versão 1.0 |
| 18 | `../game-design/SISTEMAS-E-CONTEUDO-INICIAL.md` | fórmulas e catálogo mínimo demonstrável |
| 19 | `../arquitetura/ARQUITETURA-ALVO.md` | módulos, dependências e estrutura do código |

## Decisões fechadas para a versão 1.0

| Tema | Decisão |
|---|---|
| Produto | API backend de RPG PvE, single-player e por turnos |
| Interface | API REST e coleção Bruno; não haverá frontend completo |
| Plataforma | Java 21, Spring Boot 4.1.x e Maven Wrapper |
| Arquitetura | Monólito modular orientado por domínio |
| Banco | PostgreSQL; schema criado exclusivamente por Flyway |
| Identificadores | UUID gerado pelo servidor |
| Tempo | Instantes persistidos em UTC; ISO 8601 no contrato |
| Conta | E-mail normalizado e único; papéis `PLAYER` e `ADMIN` |
| Sessão | JWT de acesso de 15 minutos e refresh token rotativo de 7 dias |
| Privacidade | Recurso privado de outro jogador responde 404 sem vazar existência |
| Personagens | Máximo de três personagens ativos por conta |
| Classes iniciais | `WARRIOR`, `MAGE` e `RANGER` |
| Progressão | Níveis 1–50; XP para próximo nível = `100 × nível²` |
| Combate | PvE; determinístico por padrão; aleatoriedade entra por `RandomSource` injetável |
| Turno | Maior velocidade começa; empate favorece o personagem |
| Ações | `BASIC_ATTACK`, `DEFEND`, `SKILL`, `USE_ITEM`, `FLEE` |
| Dano | `max(1, ataque + poder - defesa)` antes de modificadores explícitos |
| Inventário | 40 pilhas; quantidade e limite de pilha definidos pelo item |
| Equipamento | Um item por slot: `WEAPON`, `HEAD`, `CHEST`, `LEGS`, `ACCESSORY` |
| Moeda | Ouro inteiro não negativo; `long`/`bigint`; sem ponto flutuante |
| Mundo | Grafo direcionado de locais publicados |
| Missões | Definição versionada e instância persistente; recompensa única |
| Conteúdo | Ciclo `DRAFT -> PUBLISHED -> ARCHIVED`; versão publicada é imutável |
| Idempotência | `Idempotency-Key` obrigatório em ações críticas; mesma chave + corpo diferente retorna conflito |
| Concorrência | Optimistic locking em agregados mutáveis e restrições únicas no banco |
| Ranking | Ordenação determinística por vitórias, derrotas, nível e UUID |
| Erros | RFC 9457/Problem Details com `code`, `traceId` e erros de campo |
| Paginação | página 0, tamanho 20, máximo 100 |
| Testes | JUnit; regras puras unitárias; persistência crítica com PostgreSQL via Testcontainers |
| Deploy | Docker/Compose e uma plataforma com HTTPS e PostgreSQL gerenciado |
| Licença | MIT |

## Termos normativos

- **DEVE:** obrigatório para aceitar a versão.
- **NÃO DEVE:** comportamento proibido.
- **DEVERIA:** esperado, salvo decisão registrada.
- **PODE:** opcional e sem bloqueio da release.
- **MUST/SHOULD/COULD/WON'T:** prioridade MoSCoW.

## Controle de mudança

Uma mudança de requisito deve registrar: motivo, solicitante, requisitos afetados, regras afetadas, migração necessária, impacto no OpenAPI, testes, risco, semanas impactadas e decisão final. Alterações incompatíveis após `v1.0.0-rc.1` exigem adiamento ou nova versão de contrato.

## Critério de prontidão da análise

A análise está pronta porque cada capacidade da versão 1.0 possui identificador, regra, caso de uso, critério de aceite, dados, permissão, erro esperado, prioridade, release e evidência de teste. Nenhum requisito funcional depende de decisão básica ainda não tomada.
