# Dia 16 — Turnos, habilidades, mana e cooldown

**Data:** 03/09/2026  
**Sprint:** 3  
**Tempo núcleo:** 2h  
**Extensão:** 90 min  
**Resultado:** comandos de batalha validam turno, recurso e cooldown, avançando estado corretamente.

## Antes de começar

- [ ] Ataque básico está verde.
- [ ] Escolha uma habilidade por classe.
- [ ] Crie branch feat/BA-03-turn-skills.
- [ ] Defina como cooldown diminui.

## O que você precisa compreender

- Turno é parte do estado, não informação do cliente.
- Comando expressa intenção; servidor calcula efeito.
- Cooldown tem semântica exata: quando inicia e quando decrementa.
- Recurso é validado antes do efeito.
- Ordem das operações muda resultado.
- Estado terminal deve ser verificado antes de alternar.

## Fontes

- Java API: https://docs.oracle.com/en/java/javase/21/docs/api/
- JUnit: https://docs.junit.org/current/user-guide/
- Contrato local: ../../docs/06-CONTRATO-API.md

## Exemplo neutro — workflow de aprovação

Documento só pode ser aprovado pelo responsável da etapa atual. A aprovação consome a etapa, registra ação e avança. Se encerra o fluxo, não cria etapa seguinte.

## Especificação mínima

- WARRIOR: POWER_STRIKE, +10 poder, 10 mana, cooldown 2.
- RANGER: PIERCING_SHOT, +8 poder, 12 mana, cooldown 2.
- MAGE: FIREBALL, +15 poder, 20 mana, cooldown 3.

Não balanceie; valide mecanismo.

Defina cooldown:

1. usar habilidade define N;
2. ao final de cada turno do próprio ator, cooldowns positivos diminuem conforme regra escolhida;
3. escreva três turnos em tabela para eliminar ambiguidade.

## Tarefa prática

### 1. Sequência de turnos, 20 min

Desenhe:

- validações;
- custo;
- cálculo;
- aplicação;
- morte;
- encerramento ou cooldown;
- troca de turno;
- resultado.

### 2. Habilidade, 20 min

Modele catálogo/definição de habilidade separado do estado de cooldown. Cliente envia code; servidor encontra poder/custo.

### 3. Comando e domínio, 30 min

Implemente BASIC_ATTACK e SKILL. Rejeite:

- ator errado;
- desconhecida;
- não pertencente;
- mana insuficiente;
- cooldown;
- batalha terminal.

### 4. Cooldown, 20 min

Escreva testes de sequência com três/quatro turnos. Não dependa de tempo de relógio.

### 5. Persistência e API, 30 min

Modele snapshot suficiente da batalha e battle_actions. Implemente caso de uso preliminar e contrato POST /actions sem concorrência final, que entra amanhã.

### 6. Bruno/evidência, 20 min

Salve requests: ataque, habilidade, erro de mana, cooldown e fora de turno.

## Critérios de aceite

- [ ] turno vem do estado;
- [ ] cliente não envia dano;
- [ ] habilidade vem do catálogo;
- [ ] mana não fica negativa;
- [ ] cooldown é determinístico;
- [ ] batalha terminal não alterna;
- [ ] ação gera registro;
- [ ] erro não muta estado.

## Testes obrigatórios

- habilidade válida;
- mana exatamente igual ao custo;
- um abaixo;
- cooldown zero e positivo;
- habilidade de outra classe;
- ator errado;
- golpe fatal;
- ação após FINISHED;
- sequência de cooldown.

## Evidências

- tabela temporal;
- domínio/testes;
- migration/entidade se criada;
- Bruno;
- commit: feat(battle): enforce turns skills resources and cooldowns.

## Perguntas de recuperação

1. Em que momento cooldown muda?
2. Por que dano não vem do corpo?
3. O que ocorre após golpe fatal?
4. Como provar ausência de mutação em falha?
5. Qual diferença entre definição e estado da habilidade?

## Erros comuns

- confiar em actor do JSON;
- cooldown por timestamp sem necessidade;
- debitar mana antes de validar;
- alternar turno depois do fim;
- código if gigante por classe;
- aceitar habilidade desconhecida como ataque básico.

## Extensão opcional

Implemente DEFEND com efeito consumido uma vez. Escreva primeiro a sequência; não faça se Must estiver atrasado.

## Conteúdo

“A ordem das regras muda uma batalha: validação, efeito e turno”.

## Correção e conferência — só depois da tentativa

Ordem segura: validar estado/ator/vivos → resolver ação do catálogo → validar mana/cooldown → calcular → aplicar custo e efeito → verificar fim → atualizar cooldowns/turno somente se continuar → registrar resultado.

Se o golpe mata, não existe próximo turno. Se falha por mana, nada muda.
