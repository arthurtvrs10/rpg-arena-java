# Dia 18 — API de batalha, integração, review e candidaturas

**Data:** 05/09/2026  
**Sprint:** 3  
**Tempo núcleo:** 3h  
**Extensão:** 60 min  
**Resultado:** ciclo missão → recompensa → batalha demonstrado com falhas e concorrência.

## Antes de começar

- [ ] Congele features.
- [ ] Prepare dois jogadores, missão e inimigo.
- [ ] Abra matriz REG-MI/REG-BA.
- [ ] Prepare ambiente limpo.

## O que você precisa compreender

- Contrato deve refletir versão, idempotência e estado.
- Teste de jornada não substitui os testes de regras.
- Demo de concorrência precisa mostrar estado final.
- Erros previsíveis não são 500.
- Review inspeciona o Sprint Goal completo.

## Fontes

- HTTP semantics: https://www.rfc-editor.org/rfc/rfc9110.html
- Problem Details: https://www.rfc-editor.org/rfc/rfc9457.html
- Bruno assertions: https://docs.usebruno.com/testing/tests/assertions
- Spring Boot testing: https://docs.spring.io/spring-boot/reference/testing/index.html

## Exemplo neutro — execução de pedido

Fluxo integrado prova que pedido pago é separado, retry não cobra novamente e duas tentativas de expedição não duplicam estoque. A apresentação mostra dados finais, não somente respostas.

## Tarefa prática

### 1. Finalizar contrato, 25 min

Revise rotas de missão e batalha:

- auth/owner;
- requestId;
- expectedVersion, se exposta;
- status;
- códigos de erro;
- resposta repetida;
- paginação de histórico se existir.

### 2. Integração, 40 min

Complete casos de uso/endpoints:

- iniciar missão;
- concluir/recompensar;
- iniciar batalha PvE;
- executar ação;
- consultar batalha própria.

Inimigo pode agir automaticamente após ação do jogador ou como turno explícito interno; escolha e documente.

### 3. Coleção Bruno, 35 min

Fluxo:

1. login A;
2. personagem;
3. iniciar/concluir missão;
4. repetir recompensa;
5. iniciar batalha;
6. ataque/habilidade;
7. fora de turno/estado;
8. repetir ação;
9. finalizar;
10. agir após fim;
11. A tenta battle de B.

Assertions guardam ids/versão.

### 4. Suíte e banco, 25 min

Rode unitários, integração e concorrência. Consulte:

- uma reward;
- XP correto;
- ações sem duplicidade;
- version;
- estado FINISHED;
- owner.

### 5. PR/review/retro, 30 min

Revise transações, exceções, queries e logs. Demo em até sete minutos. Retro escolhe uma ação para release.

### 6. Conteúdo/candidaturas, 25 min

- publique explicação de concorrência/idempotência;
- atualize README com o que existe;
- candidate-se a quatro vagas;
- registre perguntas recorrentes.

## Critérios de aceite

- [ ] ciclo integrado funciona;
- [ ] recompensa única provada;
- [ ] ação repetida não duplica;
- [ ] conflito concorrente tem teste;
- [ ] A não consulta batalha de B;
- [ ] estados terminais rejeitam ação;
- [ ] PR/retro concluídos;
- [ ] quatro candidaturas registradas.

## Testes obrigatórios

- todos REG-MI/BA Must ligados a teste;
- banco vazio;
- Bruno feliz e falhas;
- mesma chave cinco vezes;
- duas threads;
- log sem token;
- erro sem stack.

## Evidências

- matriz regra/teste;
- coleção;
- PR e CI;
- consulta do estado final;
- demo;
- candidaturas;
- commit: test(battle): integrate mission reward and concurrent battle flow.

## Perguntas de recuperação

1. Onde está a transação de recompensa?
2. Qual diferença entre retry e conflito?
3. Como termina batalha?
4. Que dado prova efeito único?
5. Qual trade-off vai explicar em entrevista?

## Erros comuns

- demo só feliz;
- esconder teste instável;
- devolver 500 no conflito;
- endpoint aceita owner/actor;
- mesma chave cria duas ações;
- adicionar ranking antes de fechar defeitos.

## Extensão opcional

Peça a alguém para executar apenas a coleção e relatar ambiguidades. Transforme achados em issues priorizadas.

## Correção e conferência — só depois da tentativa

O incremento está pronto se dados finais confirmam exatamente uma recompensa e uma ação vencedora por turno. A resposta HTTP isolada não basta. Qualquer teste concorrente intermitente bloqueia a afirmação; simplifique a sincronização ou registre a limitação de forma honesta.
