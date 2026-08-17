# Dia 4 — Base Spring, PostgreSQL, Flyway e Docker

**Data:** 20/08/2026  
**Sprint:** 1  
**Tempo núcleo:** 2h  
**Extensão:** 90 min  
**Resultado:** aplicação reproduzível com build, banco saudável e schema versionado.

## Antes de começar

- [ ] Use Java 21.
- [ ] Mantenha a versão Spring Boot que já funciona no seu ambiente.
- [ ] Confirme Docker.
- [ ] Não reutilize banco antigo sem saber seu estado.
- [ ] Crie branch feat/EN-02-postgres-flyway.

## O que você precisa compreender

- Maven resolve build e dependências; o IDE não é fonte de verdade.
- Configuração varia por ambiente e segredo não entra no Git.
- Flyway é dono da evolução do schema.
- JPA validate detecta divergência; update automático não substitui migration.
- depends_on sem healthcheck não prova que PostgreSQL aceita conexões.
- Healthcheck da aplicação deve diferenciar processo ativo de dependência pronta.

## Fontes oficiais

- Spring Initializr: https://start.spring.io/
- Spring Boot reference: https://docs.spring.io/spring-boot/reference/index.html
- Flyway: https://documentation.red-gate.com/flyway
- Docker Compose quickstart: https://docs.docker.com/compose/gettingstarted/
- Startup order: https://docs.docker.com/compose/how-tos/startup-order/
- Maven: https://maven.apache.org/guides/getting-started/

## Exemplo neutro — serviço de catálogo

Uma aplicação sobe mesmo com tabela criada manualmente no notebook do autor, mas falha no computador de outra pessoa. A correção não é escrever “crie esta tabela” no README; é versionar migration e testar banco vazio.

## Tarefa prática

### 1. Projeto e dependências, 20 min

Confirme no POM apenas o necessário agora:

- web;
- validation;
- data JPA;
- PostgreSQL driver;
- Flyway;
- Actuator;
- test.

Security pode entrar hoje ou no Dia 7. Não adicione Lombok, mapper, cache e outras bibliotecas sem decisão.

Rode o Maven pelo wrapper. Registre versões.

### 2. Perfis e variáveis, 20 min

Crie:

- application.yml com configurações comuns;
- application-local.yml para conveniência sem segredo;
- application-test.yml para testes;
- .env.example com nomes falsos;
- .gitignore cobrindo .env e artefatos.

Configure JPA para validar schema quando a migration terminar.

### 3. Docker Compose, 25 min

Defina serviço postgres com:

- imagem com versão explícita;
- database, user e password por variáveis;
- volume nomeado;
- porta local documentada;
- healthcheck com pg_isready;
- restart apenas se souber o efeito.

Não coloque credenciais reais no arquivo.

### 4. Primeira migration, 25 min

Crie V1 para accounts e V2 para characters ou, se preferir uma migration inicial coesa, documente a escolha. Inclua:

- PK;
- nulabilidade;
- unicidade normalizada de e-mail/nome;
- FK;
- checks básicos;
- timestamps;
- version.

Não crie todas as tabelas do mês.

### 5. Verificação do zero, 20 min

Em um ambiente descartável:

1. suba PostgreSQL;
2. inicie aplicação;
3. verifique migrations;
4. consulte tabela de histórico do Flyway;
5. confira health;
6. pare e suba novamente;
7. rode testes.

### 6. Evidência, 10 min

Documente comandos exatos em README, crie commit e anote qualquer diferença entre IDE e Maven.

## Critérios de aceite

- [ ] build funciona pelo wrapper;
- [ ] PostgreSQL possui versão explícita e healthcheck;
- [ ] banco vazio recebe migrations automaticamente;
- [ ] JPA não cria/altera schema silenciosamente;
- [ ] segunda inicialização não reaplica migration;
- [ ] .env não está rastreado;
- [ ] healthcheck responde;
- [ ] README contém sequência reproduzível.

## Testes obrigatórios

- migration em banco vazio;
- reinício com banco existente;
- credencial incorreta falha de forma observável;
- migration propositalmente inválida falha e não é “corrigida” editando histórico;
- mvnw test ou equivalente verde.

## Evidências

- compose.yml;
- migrations;
- application profiles;
- saída resumida de build;
- histórico Flyway;
- commit: chore(platform): bootstrap postgres migrations and healthcheck.

## Perguntas de recuperação

1. Por que ddl-auto update é inadequado para entrega?
2. Qual diferença entre container iniciado e banco pronto?
3. Onde fica segredo local?
4. O que Flyway validate protege?
5. Por que imagem latest é risco?

## Erros comuns

- senha versionada;
- migration gigante com todo domínio;
- editar migration aplicada;
- depender do banco criado pelo IDE;
- fixar porta sem documentar conflito;
- dizer que health está pronto sem testar dependência.

## Extensão opcional

Crie um teste de contexto usando PostgreSQL real apenas se não atrapalhar a fatia. Caso contrário, registre para Dia 22.

## Conteúdo

“Por que meu schema nasce por migration e não pelo Hibernate”.

## Correção e conferência — só depois da tentativa

A sequência robusta é: Compose declara PostgreSQL saudável; Spring lê variáveis; Flyway aplica versões; JPA valida; Actuator mostra estado. O build deve funcionar fora do IDE. Se você precisou executar SQL manual não documentado, a entrega ainda não é reproduzível.
