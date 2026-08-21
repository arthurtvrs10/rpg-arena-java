# Dia 10 — Criação de personagem, classes e atributos

**Data:** 27/08/2026  
**Sprint:** 2  
**Tempo núcleo:** 2h  
**Extensão:** 90 min  
**Resultado:** personagem criado com regras, propriedade e atributos calculados pelo servidor.

## Antes de começar

- [ ] US-03 cumpre Ready.
- [ ] Defina três classes simples.
- [ ] Crie branch feat/CH-01-create-character.
- [ ] Escreva tabela de atributos antes da migration.

## O que você precisa compreender

- Catálogo estático em código pode ser suficiente no MVP.
- Atributos derivados não vêm do cliente.
- Limite por conta é regra transacional.
- Unicidade precisa do banco para corrida.
- Entidade nasce válida; estado inicial não é conjunto de setters.
- Criação pode coordenar personagem e kit inicial na mesma transação.

## Fontes

- Spring Data transactions: https://docs.spring.io/spring-data/jpa/reference/jpa/transactions.html
- Bean Validation: https://docs.spring.io/spring-framework/reference/core/validation/beanvalidation.html
- PostgreSQL constraints: https://www.postgresql.org/docs/current/ddl-constraints.html

## Exemplo neutro — abertura de conta bancária

Cliente envia tipo e apelido, mas não envia saldo, status aprovado ou limite. Aplicação valida quantidade de contas, cria estado inicial e garante unicidade. Kit/benefício inicial ocorre junto ou não ocorre.

## Especificação inicial

Classes:

| Código | Vida | Ataque | Defesa | Mana |
|---|---:|---:|---:|---:|
| WARRIOR | 140 | 18 | 12 | 30 |
| RANGER | 110 | 22 | 8 | 45 |
| MAGE | 90 | 26 | 5 | 80 |

Números são hipótese de jogo, não foco de balanceamento. Não gaste tempo refinando.

## Tarefa prática

### 1. Contrato e casos, 15 min

Entrada: name e classCode. Liste explicitamente campos rejeitados/ignorados: level, XP, owner, health, attack, role.

### 2. Domínio, 25 min

Implemente criação válida:

- nome normalizado;
- classe ativa;
- atributos base;
- nível 1/XP0;
- owner obrigatório;
- resultado imutável.

Reutilize Progression do Dia 5.

### 3. Persistência/migration, 25 min

Crie migration aditiva e mapeamento. Garanta:

- FK owner;
- unique lower(name);
- checks;
- version;
- timestamps.

Não deixe JPA criar coluna.

### 4. Caso de uso transacional, 25 min

Ordem:

1. CurrentActor;
2. contar personagens do owner;
3. validar limite;
4. validar nome/classe;
5. criar personagem e kit mínimo, se incluído;
6. persistir;
7. mapear resposta.

Trate conflito de constraint como código de domínio/contrato.

### 5. API e testes, 35 min

Teste:

- primeiro, terceiro e quarto personagem;
- nome no limite e inválido;
- nome duplicado variando caixa;
- classe inválida;
- campos manipulados;
- lista própria;
- criação concorrente documentada/testada se possível.

Crie requests Bruno.

### 6. Evidência, 15 min

Atualize OpenAPI rascunho e README do fluxo.

## Critérios de aceite

- [ ] cliente só escolhe nome e classe;
- [ ] owner vem do token;
- [ ] estado inicial é válido;
- [ ] limite de três é aplicado;
- [ ] nome duplicado case-insensitive falha;
- [ ] atributos seguem catálogo do servidor;
- [ ] entidade não é resposta;
- [ ] migration e testes estão verdes.

## Testes obrigatórios

- WARRIOR tem atributos previstos;
- quarto personagem falha;
- “Aria” e “aria” conflitam;
- accountId enviado não muda owner;
- level=99 não é aceito;
- conta B ainda cria seus próprios três.

## Evidências

- tabela de classes;
- migration;
- regra/testes;
- Bruno;
- commit: feat(character): create owned characters with server-side stats.

## Perguntas de recuperação

1. Por que atributos não vêm do cliente?
2. Onde garantir unicidade?
3. Qual corrida existe no limite de três?
4. O que entra na transação de criação?
5. Quando catálogo deveria virar tabela?

## Erros comuns

- DTO com entidade inteira;
- aceitar owner;
- apenas exists antes de insert;
- balancear jogo por horas;
- retornar password/account;
- classe com setters de level/XP.

## Extensão opcional

Desenhe uma solução segura para duas criações simultâneas quando a conta já possui dois personagens. Compare lock da conta, constraint por slot e serialização.

## Conteúdo

“O cliente escolhe a classe, mas o servidor decide os atributos”.

## Correção e conferência — só depois da tentativa

O fluxo seguro não confia em nenhum estado derivado. O banco resolve nome duplicado mesmo sob corrida. O limite de três pode exigir controle adicional em concorrência; se você não implementar agora, registre risco e teste sequencial, sem afirmar garantia absoluta.

Para o mês, enum/registro em código para três classes é defensável. Tabela administrável só entra se houver história real e tempo.
