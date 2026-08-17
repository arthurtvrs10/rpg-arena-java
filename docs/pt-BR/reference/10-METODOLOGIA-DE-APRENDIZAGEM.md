# Metodologia de aprendizagem

## Abordagem

Não existe uma única “melhor metodologia do mercado” para todos. Este plano combina práticas com bom suporte para retenção e transferência em um contexto de engenharia de software:

- projeto real com entrega incremental;
- prática de recuperação;
- prática distribuída;
- intercalação;
- exemplos resolvidos com retirada gradual de apoio;
- prática deliberada com feedback;
- explicação em voz alta;
- retrospectiva baseada em evidência.

## Ciclo diário

~~~mermaid
flowchart TD
    R["Recuperar sem notas"] --> M["Modelar antes do código"]
    M --> I["Implementar fatia pequena"]
    I --> T["Testar e observar"]
    T --> E["Explicar e registrar"]
    E --> R
~~~

## 1. Prática de recuperação

Antes de consultar, responda perguntas sobre a tarefa anterior e desenhe o fluxo de memória. A finalidade é forçar recuperação, não reler passivamente.

Exemplos:

- Por que a identidade não vem do corpo?
- Qual alteração precisa estar na mesma transação?
- O que a coluna version impede?
- Como o banco garante que uma chave não repete?

Marque cada resposta:

- 0: não lembro;
- 1: lembro com pista;
- 2: explico;
- 3: aplico em um caso novo.

## 2. Repetição distribuída 1–3–7

Revise uma decisão:

- no dia seguinte;
- três dias depois;
- sete dias depois.

Não releia tudo. Responda duas perguntas, refaça um pequeno teste ou explique um diagrama.

## 3. Intercalação

Misture problemas relacionados sem estudar blocos enormes isolados. Exemplo:

- regra de missão;
- transação da missão;
- teste da missão;
- contrato da missão.

Isso treina a escolha da ferramenta adequada. Não confunda com trocar de tarefa a cada cinco minutos; WIP continua igual a um.

## 4. Exemplo resolvido com retirada de apoio

Cada arquivo diário apresenta um exemplo em outro domínio. Processo:

1. explique por que o exemplo funciona;
2. esconda parte e reconstrua;
3. extraia o princípio;
4. aplique ao RPG sem copiar nomes/estrutura;
5. compare apenas no final.

## 5. Prática deliberada

Escolha uma fragilidade pequena, produza feedback rápido e repita com variação.

Exemplo:

- fragilidade: diferenciar 401, 403, 404 e 409;
- prática: classificar dez cenários;
- feedback: contrato e teste;
- variação: aplicar a personagem, missão e batalha.

## 6. Aprendizagem baseada em projeto

O projeto é o contexto, mas não justifica pular teoria. Para cada tarefa:

- conceito;
- exemplo;
- previsão;
- implementação;
- teste;
- explicação;
- generalização.

## 7. Autoexplicação

Ao terminar, grave áudio ou vídeo de até três minutos respondendo:

1. qual problema resolvi;
2. qual regra poderia quebrar;
3. por que escolhi esta solução;
4. qual alternativa descartei;
5. qual teste prova a decisão.

Se você só consegue narrar nomes de classes, ainda não explicou engenharia.

## 8. Feedback

Fontes de feedback sem IA:

- compilador;
- testes;
- PostgreSQL;
- resposta HTTP;
- diff do Git;
- linter/formatter;
- documentação oficial;
- review de colega ou comunidade;
- entrevista;
- comportamento observado na demo.

## Protocolo de leitura técnica

1. escreva a pergunta;
2. encontre seção oficial diretamente relacionada;
3. leia visão geral e contrato;
4. faça previsão do comportamento;
5. crie experimento mínimo;
6. observe resultado;
7. anote regra em suas palavras;
8. registre link e data.

## Rubrica semanal de domínio

| Nível | Evidência |
|---|---|
| 0 — Reconhece | identifica termos, não aplica |
| 1 — Reproduz | segue exemplo com pequenas mudanças |
| 2 — Aplica | resolve caso do projeto sem roteiro linha a linha |
| 3 — Justifica | compara alternativas e riscos |
| 4 — Transfere | aplica o princípio a outro domínio |

Meta do mês: nível 3 nos riscos centrais; não nível 4 em todas as tecnologias.

## Recuperação após atraso

Não dobre a carga. Faça:

1. preservar Sprint Goal;
2. remover Should/Could;
3. transformar funcionalidade em fatia menor;
4. manter teste do risco principal;
5. registrar dívida;
6. replanejar no sábado.

## Evidência científica consultada

O plano dá prioridade a prática de testes/recuperação e distribuição, técnicas avaliadas como de alta utilidade no levantamento de Dunlosky e colaboradores. Autoexplicação e intercalação entram como apoio, não como substitutas de construção e feedback.

Fontes:

- https://pubmed.ncbi.nlm.nih.gov/26173288/
- https://fatecitapetininga.edu.br/sif/nelfi/pdf/estacad.pdf

## Regra contra ilusão de competência

Reler e reconhecer não contam como domínio. A evidência válida é produzir sem guia, prever um caso de falha, testar, explicar e transferir a regra.
