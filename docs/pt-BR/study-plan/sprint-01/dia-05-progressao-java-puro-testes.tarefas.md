# Dia 5 — Progressão em Java puro e testes

**Data:** 21/08/2026  
**Sprint:** 1  
**Tempo núcleo:** 2h  
**Extensão:** 60 min  
**Resultado:** regra de XP/nível independente de Spring, protegida por testes de limite.

## Antes de começar

- [ ] Responda revisões 1–3–7 previstas.
- [ ] Desligue a aplicação: esta regra não precisa de servidor.
- [ ] Escreva exemplos antes da implementação.

## O que você precisa compreender

- Regra de domínio deve manter invariantes em toda entrada.
- Testar fronteiras é mais valioso que repetir valores comuns.
- Resultado explícito evita o chamador reconstruir o que aconteceu.
- Exceção de domínio precisa indicar violação, não detalhe técnico.
- Relógio, aleatoriedade e I/O não pertencem à fórmula.
- Método pequeno não significa regra trivial; explique pré e pós-condições.

## Fontes

- JUnit User Guide: https://docs.junit.org/current/user-guide/
- Java API: https://docs.oracle.com/en/java/javase/21/docs/api/
- Documento de regras: ../../docs/03-REGRAS-DE-NEGOCIO.md

## Exemplo neutro — pontos de fidelidade

Cliente muda de categoria ao atravessar limiares. Uma compra pode atravessar mais de um. Testes devem cobrir um ponto abaixo, exatamente no limiar, um acima e vários limiares. O programa não deve confiar em categoria enviada pelo cliente.

## Especificação da regra

XP para próximo nível em L = 100 × L².

Estado inicial: nível 1, XP 0.

Ao conceder XP:

1. rejeitar valor negativo;
2. zero não altera;
3. somar;
4. enquanto atingir o limiar, subtrair e elevar nível;
5. devolver nível anterior, novo, XP restante e níveis ganhos.

Defina um nível máximo ou documente que não existe no MVP. Proteja overflow de cálculo.

## Tarefa prática

### 1. Tabela de decisão, 20 min

Preencha resultados esperados:

| Inicial | Concessão | Resultado |
|---|---:|---|
| L1, XP0 | 0 | ? |
| L1, XP0 | 99 | ? |
| L1, XP0 | 100 | ? |
| L1, XP90 | 10 | ? |
| L1, XP0 | 500 | ? |
| L2, XP399 | 1 | ? |
| L3, XP10 | -1 | ? |

Não codifique até completar.

### 2. Modelo, 20 min

Escolha entre:

- Character com comportamento grantExperience; ou
- value object Progression usado por Character.

Registre prós e contras. Evite setters públicos para level/experience. Crie resultado imutável.

### 3. Testes primeiro, 25 min

Escreva testes para:

- zero;
- abaixo;
- exatamente no limite;
- um acima;
- estado já próximo do limite;
- múltiplos níveis;
- negativo;
- número grande controlado.

Use teste parametrizado onde reduz repetição sem esconder significado.

### 4. Implementação mínima, 25 min

Implemente até os testes passarem. Não adicione JPA, Repository ou Controller. Mantenha fórmula nomeada e proteja cálculo.

### 5. Refatoração, 15 min

Leia apenas o diff. Verifique:

- nomes explicam unidade;
- condição de loop;
- resultado;
- ausência de mutação parcial quando falha;
- complexidade e overflow.

### 6. Explicação e commit, 15 min

Explique um caso de múltiplos níveis com contas. Rode suíte e faça commit.

## Critérios de aceite

- [ ] domínio não importa Spring;
- [ ] nível nunca fica abaixo de 1;
- [ ] XP nunca fica negativa;
- [ ] múltiplos níveis funcionam;
- [ ] valor negativo não altera estado;
- [ ] testes cobrem fronteiras;
- [ ] resultado informa mudança;
- [ ] fórmula está centralizada e nomeada.

## Testes obrigatórios

Além da tabela:

- propriedade informal: após concessão válida, XP restante é menor que o limiar do nível atual;
- estado antes da exceção negativa é igual ao estado depois;
- duas concessões que somam o mesmo valor produzem o mesmo estado, salvo eventos/metadados documentados.

## Evidências

- tabela preenchida;
- classe(s) de domínio;
- testes;
- resultado do Maven;
- commit: feat(character): model tested experience progression.

## Perguntas de recuperação

1. Por que usar while e não apenas if?
2. Qual invariante fica verdadeira após o método?
3. O que acontece no limiar exato?
4. Por que não aceitar level no DTO?
5. Como detectar overflow?

## Erros comuns

- um if que sobe apenas um nível;
- teste apenas de 100 XP;
- setter público;
- fórmula duplicada no Service;
- usar double;
- alterar XP antes de validar entrada;
- carregar Spring para testar regra.

## Extensão opcional

Crie uma segunda estratégia de progressão por tabela configurável sem alterar Character. Compare com a fórmula, mas não integre ao MVP.

## Conteúdo

Faça live coding curto de um teste de fronteira e explique o erro que ele evita.

## Correção e conferência — só depois da tentativa

Resultados esperados principais:

- L1 + 99 → L1 XP99;
- L1 + 100 → L2 XP0;
- L1 XP90 + 10 → L2 XP0;
- L1 + 500 → L3 XP0, pois gasta 100 e depois 400;
- L2 XP399 + 1 → L3 XP0;
- negativo → exceção sem mutação.

Pseudocódigo:

~~~text
validar quantidade
novoXp = xp atual + quantidade
novoNivel = nível atual
enquanto novoXp >= limiar(novoNivel):
    novoXp -= limiar(novoNivel)
    novoNivel += 1
atribuir estado final uma única vez
devolver resultado
~~~

Calcule em tipo amplo e valide limites antes da atribuição.
