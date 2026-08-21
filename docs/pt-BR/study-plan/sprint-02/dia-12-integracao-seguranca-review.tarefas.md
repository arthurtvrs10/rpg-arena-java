# Dia 12 — Integração, segurança, review e candidaturas

**Data:** 29/08/2026  
**Sprint:** 2  
**Tempo núcleo:** 3h  
**Extensão:** 60 min  
**Resultado:** fluxo autenticado de personagem/inventário comprovado e revisado.

## Antes de começar

- [ ] Congele novas funcionalidades.
- [ ] Prepare banco limpo.
- [ ] Abra matriz de segurança do Dia 7.
- [ ] Use template de review/retro.

## O que você precisa compreender

- Suíte integrada verifica costuras que testes unitários não veem.
- Segurança deve ser testada no transporte e no caso de uso.
- Coleção Bruno é documentação executável.
- Review demonstra resultado do Sprint Goal.
- Evidência de falha é tão importante quanto jornada feliz.

## Fontes

- Spring Boot testing: https://docs.spring.io/spring-boot/reference/testing/index.html
- Spring Security testing: https://docs.spring.io/spring-security/reference/servlet/test/index.html
- Bruno tests: https://docs.usebruno.com/testing/tests/introduction
- Assertions: https://docs.usebruno.com/testing/tests/assertions

## Exemplo neutro — conta e fatura

O teste unitário prova a regra; o integrado prova que token A, URL de B, query e serialização resultam na rejeição esperada. O teste não termina em “status != 200”: afirma código e ausência de dados.

## Tarefa prática

### 1. Matriz de regressão, 25 min

Ligue cada REG-AU, REG-CH e REG-IN implementada a:

- nome de teste;
- nível;
- cenário Bruno;
- resultado.

Regra crítica sem teste vira prioridade.

### 2. Testes HTTP/segurança, 40 min

Automatize:

- register/login;
- token inválido;
- criar/listar/detalhar próprio;
- A busca B;
- equipar próprio;
- A usa item/personagem de B;
- payload proibido;
- PLAYER chama admin.

Valide corpo e ausência de campos.

### 3. Fluxo Bruno, 35 min

Organize execução:

1. registrar A e B;
2. login;
3. criar personagens;
4. obter/fornecer itens de teste;
5. equipar A;
6. ataque de A contra B;
7. repetir equip;
8. limpar/registrar ids.

Use variáveis locais e exemplos sem segredo.

### 4. Verificação de dados, 20 min

Inspecione banco:

- hashes;
- owners;
- slot único;
- migrations;
- versões;
- ausência de senha/token.

### 5. PR e review, 30 min

Revise:

- validação versus regra;
- Controller simples;
- transação;
- queries por owner;
- DTOs;
- erros;
- docs.

Corrija apenas bloqueadores e defeitos da sprint.

### 6. Demo e retro, 25 min

Demo:

- login;
- personagem;
- equipamento;
- acesso cruzado rejeitado;
- teste/PR.

Retro com uma ação.

### 7. Portfólio/candidaturas, 25 min

- publique “JWT não basta” ou tema da sprint;
- atualize README com features reais;
- candidate-se a três vagas;
- registre requisitos recorrentes e não mude stack impulsivamente.

## Critérios de aceite

- [ ] Sprint Goal demonstrado;
- [ ] matriz liga regras a testes;
- [ ] A nunca acessa B;
- [ ] senha/hash/token não vazam;
- [ ] Bruno executa em ordem documentada;
- [ ] banco limpo reproduz;
- [ ] PR e retro concluídos;
- [ ] três candidaturas registradas.

## Testes obrigatórios

- verify completo;
- coleção Bruno feliz;
- coleção/requests de segurança;
- migrations do zero;
- busca textual por password, Authorization e secret em logs/config;
- revisão de todos findById privados.

## Evidências

- PR;
- matriz de testes;
- coleção;
- captura CI se já existir;
- demo;
- candidaturas;
- commit: test(security): prove account isolation across protected resources.

## Perguntas de recuperação

1. Qual teste mais reduz risco?
2. Que controle está no banco?
3. Onde a transação de equipamento começa?
4. Como prova que corpo não vaza?
5. Qual ação da retro entra na Sprint 3?

## Erros comuns

- apenas teste feliz;
- Bruno com token commitado;
- limpar banco manualmente sem roteiro;
- alterar escopo durante review;
- três candidaturas idênticas;
- “100% seguro” no README.

## Extensão opcional

Peça a outra pessoa para trocar ids na coleção e tentar quebrar isolamento. Registre achado como issue, sem discutir defensivamente.

## Correção e conferência — só depois da tentativa

O incremento esperado permite login, personagem próprio e equipamento próprio; qualquer troca de id para B é rejeitada sem vazamento. Se existe endpoint privado ainda baseado apenas em findById, ele bloqueia a afirmação de isolamento até ser revisado.
