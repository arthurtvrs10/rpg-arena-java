# Dia 2 — Domínio, invariantes e estados

**Data:** 18/08/2026  
**Sprint:** 1  
**Tempo núcleo:** 2h  
**Extensão:** 60–90 min  
**Resultado:** linguagem do negócio e modelo que impedem estados impossíveis.

## Antes de começar

- [ ] Responda as cinco perguntas do Dia 1 sem consultar.
- [ ] Revise Product Goal e histórias Must.
- [ ] Mova apenas esta tarefa para In Progress.

## O que você precisa compreender

- Entidade possui identidade ao longo do tempo.
- Value object é definido por valor e pode validar sua própria consistência.
- Agregado protege invariantes dentro de um limite de consistência.
- Estado não é apenas uma string; transições têm pré-condições e efeitos.
- Regra de negócio deve sobreviver se o Controller for trocado.
- Nem toda tabela merece uma classe de domínio rica; modele comportamento e risco.

## Fontes

1. Java 21 API e linguagem: https://docs.oracle.com/en/java/javase/21/
2. Spring Data — Domain Events, para leitura conceitual posterior:  
   https://docs.spring.io/spring-data/jpa/reference/repositories/core-domain-events.html
3. Documento local de regras: ../../docs/03-REGRAS-DE-NEGOCIO.md

## Exemplo neutro — empréstimo de biblioteca

BookCopy possui identidade. ISBN é value object. Loan protege as transições ACTIVE → RETURNED ou ACTIVE → LOST. Um empréstimo devolvido não pode ser devolvido novamente. Member não precisa carregar todos os empréstimos da instituição no mesmo agregado.

Princípio: desenhe o limite de consistência ao redor da regra que precisa ser verdadeira na mesma decisão.

## Tarefa prática

### 1. Glossário, 20 min

Crie docs/DOMAIN.md. Defina em uma frase, sem usar sinônimo circular:

- conta;
- jogador;
- personagem;
- classe;
- atributo base e derivado;
- item de catálogo;
- item de inventário;
- slot;
- missão;
- tentativa;
- recompensa;
- batalha;
- combatente;
- turno;
- ação;
- habilidade;
- cooldown;
- ranking.

Liste também termos proibidos ou ambíguos, como User podendo significar conta ou personagem.

### 2. Eventos e comandos, 20 min

Para a jornada principal, escreva comandos no imperativo e eventos no passado:

- CreateCharacter → CharacterCreated;
- EquipItem → ItemEquipped;
- CompleteMission → MissionCompleted e RewardGranted;
- PerformBattleAction → BattleActionPerformed;
- FinishBattle → BattleFinished.

Não implemente eventos hoje; use-os para descobrir mudanças de estado.

### 3. Agregados e invariantes, 30 min

Proponha os agregados:

- Character;
- Inventory;
- MissionAttempt;
- Battle.

Para cada um, escreva:

- identidade;
- estado interno;
- comandos aceitos;
- invariantes;
- resultado devolvido;
- referências externas apenas por id;
- o que fica fora do limite.

### 4. Máquinas de estado, 25 min

Desenhe estados e transições de MissionAttempt e Battle. Para cada seta, escreva:

- condição;
- efeito;
- erro se condição falhar;
- se é repetível;
- se exige transação.

### 5. Exemplos e contraexemplos, 15 min

Para cinco regras, escreva um exemplo válido, um limite e um inválido. Inclua:

- quarto personagem;
- XP que sobe dois níveis;
- item incompatível;
- missão já concluída;
- ação concorrente.

### 6. Evidência, 10 min

Atualize regras numeradas, crie commit e explique um agregado em voz alta.

## Critérios de aceite

- [ ] Glossário evita termos ambíguos.
- [ ] Pelo menos quatro agregados têm responsabilidade clara.
- [ ] Invariantes não dependem apenas de DTO.
- [ ] MissionAttempt e Battle possuem estados terminais.
- [ ] Transição inválida tem código de erro.
- [ ] Recompensa exatamente uma vez aparece no modelo.
- [ ] Concorrência aparece como risco de Battle.
- [ ] Você explica por que Inventory não é apenas uma lista.

## Testes de mesa

Sem código, execute:

1. personagem nível 1 recebe 550 XP;
2. missão complete é chamada duas vezes;
3. dois itens tentam ocupar MAIN_HAND;
4. batalha recebe duas ações com a mesma versão;
5. jogador A usa battleId de B.

Para cada um, identifique objeto responsável, decisão e resultado.

## Evidências

- docs/DOMAIN.md;
- diagramas;
- tabela comando/evento;
- regras atualizadas;
- commit: docs(domain): model aggregates invariants and state transitions.

## Perguntas de recuperação

1. Qual diferença entre validação estrutural e invariante?
2. Qual agregado protege recompensa?
3. Por que estado terminal não deve reabrir?
4. Quando referenciar outro agregado por id?
5. Que estado impossível um setter público permitiria?

## Erros comuns

- criar uma classe para cada substantivo;
- agregado que carrega o jogo inteiro;
- entidade composta só de getters/setters;
- service decide tudo e domínio apenas armazena;
- persistir enum sem pensar em evolução;
- confundir evento descoberto com obrigação de usar mensageria.

## Extensão opcional

Modele o domínio de reserva de assento e compare os limites. Se usar exatamente as mesmas classes, você copiou estrutura em vez de transferir princípio.

## Conteúdo

Título: “Como usei estados e invariantes para sair do CRUD”.

## Correção e conferência — só depois da tentativa

Uma divisão defensável é:

- Character protege identidade, progressão e atributos.
- Inventory protege posse, estado e slots.
- MissionAttempt protege ciclo e concessão.
- Battle protege combatentes, turno, recursos e encerramento.

O caso de uso coordena agregados e transação. Não coloque Repository dentro de Battle. Não faça uma única classe GameService controlar tudo.
