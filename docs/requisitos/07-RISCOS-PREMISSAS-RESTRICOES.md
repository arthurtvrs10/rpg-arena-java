# Riscos, premissas e restrições

## Premissas congeladas

| ID | Premissa |
|---|---|
| PR-01 | Uma pessoa desenvolve o projeto entre 18 e 22 horas por semana. |
| PR-02 | O cliente funcional da versão 1.0 é Bruno/OpenAPI, não um frontend. |
| PR-03 | PostgreSQL 16+ está disponível localmente por Docker ou instalação nativa. |
| PR-04 | O sistema atende carga de portfólio, não milhões de usuários. |
| PR-05 | Conteúdo inicial será pequeno e versionado no próprio repositório/API admin. |
| PR-06 | Jogador controla somente um personagem por comando e batalha. |
| PR-07 | Combate é síncrono por request, sem websocket. |
| PR-08 | Uma única moeda, ouro, é suficiente para 1.0. |
| PR-09 | Português é o idioma do conteúdo inicial; códigos internos são estáveis e independem do idioma. |
| PR-10 | Java 21 e Spring Boot 4.1.x permanecem durante a temporada, salvo vulnerabilidade crítica. |

## Restrições

| ID | Restrição | Consequência |
|---|---|---|
| RT-01 | Seis meses e 24 semanas | mudanças entram por troca de escopo, não por aumento infinito de carga |
| RT-02 | Backend API-first | toda funcionalidade precisa ser demonstrável por teste/Bruno |
| RT-03 | Monólito modular | não extrair microserviço antes da 1.0 |
| RT-04 | PostgreSQL como banco real | não validar persistência crítica apenas com H2/mocks |
| RT-05 | Sem infraestrutura paga obrigatória | escolher deploy com faixa gratuita/baixo custo e plano de saída |
| RT-06 | Open source MIT | somente assets e dependências compatíveis/documentados |
| RT-07 | Ambiente principal Windows | scripts devem possuir alternativa `.cmd`/Docker quando necessário |
| RT-08 | Docker Desktop pode estar indisponível no início | oferecer instalação nativa do PostgreSQL como plano temporário; testes Docker entram quando daemon estiver disponível |

## Registro de riscos

Escala: probabilidade (P) e impacto (I) de 1 a 5; exposição = P × I.

| ID | Risco | P | I | Exposição | Mitigação | Gatilho/contingência |
|---|---|---:|---:|---:|---|---|
| RK-01 | Escopo grande para uma pessoa | 4 | 5 | 20 | Must primeiro, fatias verticais, limite 2 dias/história | atraso de 1 semana: remover Could/Should na ordem definida |
| RK-02 | Docker Desktop indisponível | 4 | 4 | 16 | checklist Windows/WSL, plano PostgreSQL nativo | daemon ausente: seguir domínio puro e corrigir ambiente antes da Semana 5 |
| RK-03 | Dependência incompatível com Spring Boot 4.1 | 3 | 4 | 12 | usar BOM, docs oficiais e spike isolado | build quebra: remover biblioteca não essencial ou escolher alternativa suportada |
| RK-04 | Modelo de domínio acoplado ao JPA | 3 | 5 | 15 | ArchUnit e adapters separados | import `jakarta.persistence` no domínio: bloquear PR |
| RK-05 | Autorização apenas no controller | 3 | 5 | 15 | ownership no caso de uso/repository e testes cruzados | teste BOLA falha: blocker de release |
| RK-06 | Recompensa/compra duplicada | 3 | 5 | 15 | idempotência, unique constraints e teste concorrente | duplicidade detectada: interromper feature e criar regressão |
| RK-07 | Atualização perdida no combate | 3 | 5 | 15 | optimistic locking e expectedVersion | dois sucessos para o mesmo turno: blocker |
| RK-08 | Migrations inconsistentes | 3 | 5 | 15 | migrate em banco vazio e upgrade em CI | migration aplicada precisa correção: criar nova migration, nunca editar a antiga |
| RK-09 | Testes lentos/instáveis | 4 | 3 | 12 | pirâmide, builders, clock/random injetáveis | suíte >10 min ou flaky: separar e eliminar dependência global |
| RK-10 | Documentação promete algo inexistente | 4 | 4 | 16 | matriz de status e revisão por release | README divergente: corrigir antes de tag/vídeo |
| RK-11 | Exposição de segredo em gravação | 3 | 5 | 15 | perfis fictícios, redação e checklist de gravação | vazamento: revogar imediatamente e substituir mídia |
| RK-12 | Conteúdo ramificado complexo demais | 4 | 3 | 12 | schema mínimo, uma missão exemplo e validação antecipada | história >2 dias: reduzir tipos de nó/efeito |
| RK-13 | N+1 e ranking lento | 3 | 3 | 9 | consultas explícitas, índices e plano EXPLAIN | p95 alvo falha: medir e otimizar apenas consulta real |
| RK-14 | Deploy gratuito hibernar/limitar banco | 4 | 2 | 8 | documentar cold start e manter demo local | indisponibilidade recorrente: usar vídeo/smoke local e migrar plataforma |
| RK-15 | Burnout por código + conteúdo | 4 | 4 | 16 | gravar durante trabalho, episódio quinzenal, buffer | duas semanas sem entrega: pausar Shorts, preservar desenvolvimento |
| RK-16 | Mudança contínua de tecnologia | 4 | 4 | 16 | ADR e stack congelada | nova tecnologia sem problema mensurável: rejeitar para 1.0 |

## Dependências externas

| Dependência | Uso | Plano de falha |
|---|---|---|
| GitHub | código, issues, PR e CI | manter Git local e pacote ZIP; publicar quando recuperar |
| Maven Central | dependências | cache local; não trocar versões durante build crítico |
| PostgreSQL | persistência | Docker ou instalação nativa |
| Docker | reprodução/Testcontainers | executar unitários sem Docker e corrigir daemon antes das semanas de integração |
| Plataforma de deploy | API pública | runbook, export do banco e imagem portátil |
| YouTube | minissérie | manter masters e roteiro local; publicar depois sem bloquear release |

## Dívidas aceitas na 1.0

- access token não possui blacklist por requisição; é curto e conta bloqueada é verificada pela política definida;
- rate limiting pode ser simples e local; não será distribuído;
- ranking é projeção no mesmo banco;
- conteúdo possui um idioma público inicial;
- observabilidade usa solução básica da plataforma, sem cluster dedicado;
- nenhuma garantia formal de disponibilidade comercial.

Essas dívidas devem aparecer nas release notes e não podem ser apresentadas como capacidades implementadas.
