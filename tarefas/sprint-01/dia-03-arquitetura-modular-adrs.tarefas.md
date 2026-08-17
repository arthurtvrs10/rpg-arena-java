# Dia 3 — Arquitetura modular e ADRs

**Data:** 19/08/2026  
**Sprint:** 1  
**Tempo núcleo:** 2h  
**Extensão:** 60 min  
**Resultado:** estrutura de código que torna limites e decisões visíveis.

## Antes de começar

- [ ] Responda perguntas dos dias 1 e 2 marcadas para revisão.
- [ ] Leia docs/04-ARQUITETURA-E-PASTAS.md.
- [ ] Identifique a estrutura atual do seu projeto, se já existe.

## O que você precisa compreender

- Arquitetura é conjunto de decisões e dependências, não desenho decorativo.
- Package-by-feature reduz acoplamento entre casos não relacionados.
- API, application, domain e infrastructure são responsabilidades, não obrigação de criar quatro classes para tudo.
- ADR preserva contexto e trade-off.
- Monólito modular é uma escolha profissional, não uma versão “inferior”.
- Teste de arquitetura pode impedir erosão.

## Fontes oficiais

1. Spring Boot — Structuring Your Code:  
   https://docs.spring.io/spring-boot/reference/using/structuring-your-code.html
2. ArchUnit User Guide:  
   https://www.archunit.org/userguide/html/000_Index.html
3. Spring Modulith, apenas para conceitos e exemplos; não adicionar dependência hoje:  
   https://docs.spring.io/spring-modulith/reference/

## Exemplo neutro — pedidos

Estrutura por camada global coloca todos os controllers, services e repositories juntos. Estrutura por funcionalidade mantém order, catalog e payment separados, cada um com seus limites. Isso não transforma módulos em serviços de rede.

Princípio: proximidade por mudança de negócio costuma ser mais útil que proximidade por tipo técnico.

## Tarefa prática

### 1. Mapa de dependências, 20 min

Desenhe os módulos auth, player, character, inventory, mission, battle e ranking. Para cada seta, escreva:

- por que existe;
- dado atravessado;
- se a dependência é de domínio, aplicação ou infraestrutura;
- como removeria o acoplamento se crescer.

Evite um grafo em que todos dependem de todos.

### 2. Estrutura do repositório, 20 min

Crie somente diretórios necessários para o incremento atual:

- shared/config, shared/error e shared/security;
- character/api, application, domain, infrastructure;
- resources/db/migration;
- espelho mínimo em test;
- docs/adr;
- bruno.

Registre a estrutura alvo completa em docs, mas não crie arquivos Java vazios.

### 3. Regras de arquitetura, 20 min

Escreva ao menos oito regras, incluindo:

- domain não depende de Spring;
- Controller não chama Repository;
- API não retorna entidade;
- módulo não acessa Repository interno de outro;
- shared tem critérios de entrada;
- transação começa em caso de uso;
- identidade chega por porta/current actor;
- erro público é mapeado.

Escolha duas regras para automatizar com ArchUnit na Sprint 4.

### 4. ADR-001, 20 min

Use o template e compare:

- camadas globais;
- monólito modular;
- microsserviços.

Decida monólito modular, registre benefícios, custos e gatilhos de revisão.

### 5. ADR-002, 20 min

Registre a autorização por identidade autenticada:

- contexto de BOLA;
- alternativas;
- busca por id + owner ou verificação explícita;
- política 404/403;
- teste de A contra B.

### 6. Revisão, 20 min

Verifique nomes, dependências e se cada pasta tem motivo. Faça commit e abra uma issue para o ADR de concorrência da Sprint 3.

## Critérios de aceite

- [ ] Pacotes principais são por funcionalidade.
- [ ] Domain não depende do framework.
- [ ] Limites entre módulos estão escritos.
- [ ] ADR-001 compara pelo menos três alternativas.
- [ ] ADR-002 liga decisão ao risco BOLA.
- [ ] Nenhuma pasta vazia foi criada só para “parecer arquitetura”.
- [ ] Há duas regras candidatas a teste ArchUnit.
- [ ] Microsserviços têm gatilho de revisão, não data arbitrária.

## Testes de arquitetura no papel

Classifique como permitido ou proibido:

1. BattleController chama BattleRepository.
2. BattleUseCase chama uma porta de CurrentActor.
3. Battle importa CharacterJpaEntity.
4. Battle recebe snapshot mínimo do personagem.
5. Ranking consulta projeção própria.
6. Domain lança ResponseStatusException.

Justifique cada resposta.

## Evidências

- árvore de pastas;
- diagrama de módulos;
- ADR-001 e ADR-002;
- lista de regras;
- commit: docs(architecture): define modular boundaries and ownership ADR.

## Perguntas de recuperação

1. Qual diferença entre módulo e microsserviço?
2. Por que Controller não abre regra transacional?
3. O que pode entrar em shared?
4. Qual custo do monólito modular?
5. Que evidência faria separar battle no futuro?

## Erros comuns

- quatro camadas multiplicadas sem comportamento;
- shared como depósito;
- domínio com anotações web;
- ADR escrito depois só para justificar;
- diagrama sem regra de dependência;
- usar mensageria para dois módulos no mesmo processo sem necessidade.

## Extensão opcional

Adicione um teste ArchUnit mínimo que bloqueie dependência do pacote domain para api ou infrastructure. Consulte o guia; não copie suíte completa.

## Conteúdo

Explique em três minutos: “Por que comecei com monólito modular”.

## Correção e conferência — só depois da tentativa

Permitidos: caso de uso → domínio; infraestrutura → portas/domínio; API → caso de uso. Proibidos: Controller → Repository, domain → web/security/JPA repository, battle → entidade JPA interna de character.

Uma boa ADR menciona desvantagens: disciplina de limites ainda é necessária e o deploy continua único.
