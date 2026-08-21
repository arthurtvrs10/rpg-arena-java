# Dia 15 — Motor de combate em Java puro

**Data:** 02/09/2026  
**Sprint:** 3  
**Tempo núcleo:** 2h  
**Extensão:** 60 min  
**Resultado:** ataque determinístico com regras testadas sem Spring ou banco.

## Antes de começar

- [ ] Defina apenas ataque básico e defesa.
- [ ] Prepare tabela de casos.
- [ ] Crie branch feat/BA-02-combat-engine.
- [ ] Não implemente endpoint ainda.

## O que você precisa compreender

- Motor recebe estado e comando, valida e produz novo estado/resultado.
- Determinismo acelera teste.
- Aleatoriedade, se existir, entra por porta substituível.
- Dano mínimo e limite de vida são invariantes.
- Entidade decide se pode agir; caso de uso decide owner/transação.
- Resultado da ação serve persistência e resposta sem recalcular.

## Fontes

- Java API: https://docs.oracle.com/en/java/javase/21/docs/api/
- JUnit parameterized tests: https://docs.junit.org/current/user-guide/#writing-tests-parameterized-tests
- Documento de regras: ../../docs/03-REGRAS-DE-NEGOCIO.md

## Exemplo neutro — cálculo de frete

Função recebe peso, faixa e destino e produz preço/detalhes. Não acessa Controller ou banco. Relógio e tarifa externa entram por parâmetros/porta. Casos de limite provam regra.

## Especificação

Dano bruto = ataque do ator + poder da ação − defesa do alvo.  
Dano aplicado = máximo 1.  
Vida final = máximo 0.

Ataque básico tem poder 0 e custo 0.

DEFEND reduz o próximo dano por uma regra simples escolhida e documentada. Se ameaçar o prazo, deixe DEFEND como Should.

## Tarefa prática

### 1. Tabela de decisão, 20 min

Inclua:

- ataque > defesa;
- ataque = defesa;
- ataque < defesa;
- dano exato à vida;
- dano acima da vida;
- ator morto;
- alvo morto;
- batalha não iniciada.

Preencha dano, vida e erro esperados.

### 2. Objetos, 20 min

Modele:

- Battle;
- Combatant;
- BattleStatus;
- TurnOwner;
- ActionCommand;
- ActionResult;
- DamageCalculator.

Crie apenas o necessário. Estado não deve ficar parcialmente mutado após falha.

### 3. Testes primeiro, 30 min

Escreva testes parametrizados da fórmula e testes comportamentais:

- ator correto;
- ator/alvo vivos;
- redução a zero;
- fim de batalha;
- ação depois do fim;
- resultado contém dano e estados.

### 4. Implementação, 30 min

Faça a menor implementação. Não importe Spring/JPA. Se usar crítico, crie RandomSource e fake fixo; caso contrário, registre pós-MVP.

### 5. Refatoração, 10 min

Cheque nomes, mutação, responsabilidades e resultado. Procure regra duplicada.

### 6. Explicação/evidência, 10 min

Simule à mão e compare com teste.

## Critérios de aceite

- [ ] nenhum framework no motor;
- [ ] dano mínimo 1;
- [ ] vida não fica negativa;
- [ ] morto não age;
- [ ] fim ocorre ao zerar vida;
- [ ] falha não muta parcialmente;
- [ ] testes cobrem limites;
- [ ] resultado não exige recalcular.

## Testes obrigatórios

Para cada linha da tabela, teste. Acrescente propriedade informal: dano aplicado >=1 e vida final entre 0 e vida anterior. Verifique estado após exceção.

## Evidências

- tabela;
- domínio;
- testes;
- saída Maven;
- commit: feat(battle): implement deterministic combat domain.

## Perguntas de recuperação

1. Por que motor não precisa do Spring?
2. Quando a batalha termina?
3. Por que limitar vida a zero?
4. Como testar aleatoriedade?
5. Qual camada verifica owner?

## Erros comuns

- Math.random direto;
- dano no Controller;
- vida negativa;
- continuar turno após morte;
- mockar Battle;
- teste só de um ataque comum.

## Extensão opcional

Implemente RandomSource com resultado fixo no teste e uma chance crítica pequena, sem mudar o contrato central.

## Conteúdo

“Como testei um combate sem subir servidor”.

## Correção e conferência — só depois da tentativa

O método deve validar tudo antes de atribuir novo estado. Calcule valores locais, determine se terminou e só então confirme a mutação. O ActionResult carrega dano, vida antes/depois, vencedor, status e próximo turno quando existir.
