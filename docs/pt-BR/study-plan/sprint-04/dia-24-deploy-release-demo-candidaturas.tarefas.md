# Dia 24 — Deploy, release, demo e candidaturas

**Data:** 12/09/2026  
**Sprint:** 4  
**Tempo núcleo:** 3h  
**Extensão:** 90 min  
**Resultado:** versão 1.0.0 publicada, reproduzível e apresentada com honestidade técnica.

## Antes de começar

- [ ] RC verde e sem P0/P1.
- [ ] Escolha Render como roteiro principal ou Railway como alternativa.
- [ ] Crie segredos novos para deploy.
- [ ] Nunca cole credenciais em issue, PR, vídeo ou Bruno versionado.
- [ ] Prepare plano de rollback.

## Fontes oficiais atuais

### Roteiro principal — Render

- Docker: https://render.com/docs/docker
- PostgreSQL: https://render.com/docs/postgresql-creating-connecting
- variáveis/segredos: https://render.com/docs/configure-environment-variables
- deploys: https://render.com/docs/deploys
- primeira publicação: https://render.com/docs/your-first-deploy

### Alternativa — Railway

- Spring Boot: https://docs.railway.com/guides/spring-boot
- PostgreSQL: https://docs.railway.com/databases/postgresql
- Docker Compose para serviços: https://docs.railway.com/guides/docker-compose

Planos, preços e limites mudam. Confira as páginas oficiais no dia. Não coloque cartão ou aceite custo que não compreende.

## O que você precisa compreender

- Deploy é processo repetível, não clique isolado.
- Ambiente recebe configuração e segredo separadamente.
- Migration em produção precisa de compatibilidade/rollback.
- Health determina se revisão está pronta.
- Demo usa dados falsos e controlados.
- Release declara também limitações conhecidas.

## Tarefa prática

### 1. Pré-deploy, 25 min

- CI verde;
- imagem local;
- porta via variável;
- health;
- conexão por variável;
- segredo JWT forte;
- perfil de deploy;
- OpenAPI conforme política;
- logs;
- migration aditiva;
- sem dados reais.

### 2. Banco, 20 min

Crie PostgreSQL gerenciado no mesmo provedor/região quando possível. Use conexão interna para aplicação. Registre:

- versão;
- URL/variáveis sem valores;
- política de acesso;
- backup/limitação do plano;
- expiração dos dados de demo.

### 3. Serviço Docker, 30 min

Conecte repositório, selecione Dockerfile, configure variáveis e healthcheck. Publique a RC. Observe:

- build;
- startup;
- Flyway;
- pool/conexão;
- health.

Se falhar, use protocolo sintoma → hipótese → experimento; não altere várias coisas.

### 4. Smoke no deploy, 30 min

Use ambiente deployed local do Bruno sem token versionado:

- health;
- cadastro/login;
- personagem;
- missão/retry;
- batalha/retry;
- ranking;
- BOLA.

Não faça teste de carga contra plano gratuito.

### 5. Documentação final, 25 min

Transforme:

- README-GITHUB.md em README.md;
- escopo em docs/PRODUCT-SCOPE.md;
- arquitetura/domínio/API/SECURITY;
- ADRs;
- coleção;
- setup;
- variáveis;
- limitações;
- roadmap;
- link do deploy;
- licença/autor.

Teste links e comandos.

### 6. Release 1.0.0, 15 min

Se smoke passou:

- merge;
- tag 1.0.0;
- GitHub Release com changelog;
- artefatos/coleção;
- rollback documentado.

Se não passou, mantenha RC e publique limitação; não force tag.

### 7. Demo e explicação, 30 min

Grave até oito minutos conforme docs/13:

- problema;
- arquitetura;
- jornada;
- BOLA;
- idempotência;
- concorrência;
- CI/deploy;
- trade-off.

### 8. Retro e candidaturas, 25 min

- review final;
- retro do mês;
- rubrica de domínio;
- cinco candidaturas personalizadas;
- uma lista de feedback para o próximo ciclo.

## Critérios de aceite

- [ ] deploy saudável ou limitação honesta com execução Docker reproduzível;
- [ ] segredos fora do Git/vídeo;
- [ ] migrations concluídas;
- [ ] smoke completo;
- [ ] README testado;
- [ ] release/tag coerente;
- [ ] demo explica decisões;
- [ ] cinco candidaturas registradas.

## Auditoria final

- [ ] constrói backend Java/Spring;
- [ ] modela regras por objetos;
- [ ] usa PostgreSQL/SQL/migrations/transações;
- [ ] API autentica, autoriza e isola;
- [ ] JUnit/Testcontainers/Bruno;
- [ ] Git/branches/PR/commits;
- [ ] Docker;
- [ ] publicação/documentação;
- [ ] decisões/trade-offs;
- [ ] candidaturas antes da perfeição.

## Evidências

- URL;
- release/tag;
- CI;
- README;
- OpenAPI/Bruno;
- vídeo;
- retro;
- cinco candidaturas;
- commit: release: publish rpg arena api 1.0.0.

## Perguntas de recuperação

1. Qual decisão mais protege dados?
2. Onde está a garantia de efeito único?
3. Como trata duas ações concorrentes?
4. Por que monólito modular?
5. Que limitação você admite?
6. Como outra pessoa executa?
7. Qual feedback das vagas mudou sua comunicação?

## Erros comuns

- segredo em screenshot;
- tag com smoke falhando;
- URL sem health;
- documentação de feature inexistente;
- demo longa de código;
- dizer “produção” para plano de hobby sem ressalvas;
- parar candidaturas após uma rejeição.

## Extensão opcional

Peça a outra pessoa para clonar e executar sem ajuda. Abra issues para qualquer instrução implícita.

## Correção e conferência — só depois da tentativa

Release é válida quando o mesmo commit passou CI, gerou imagem e foi testado no ambiente. Se o provedor bloquear por plano/custo, a entrega mínima profissional é Docker Compose reproduzível, release, documentação e vídeo; registre “deploy online pendente por restrição externa” sem fingir.

Você não termina “sabendo tudo”. Termina com evidência de um ciclo profissional completo e um backlog consciente para continuar.
