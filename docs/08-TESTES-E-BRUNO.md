# Estratégia de testes e Bruno

## Princípio

Teste é uma resposta a risco. Não busque porcentagem vazia. Proteja regras que mudam estado, segurança por proprietário, transações, idempotência, concorrência e contratos públicos.

## Camadas

| Nível | O que prova | Ferramenta | Velocidade |
|---|---|---|---|
| Domínio | Regra isolada e estados | JUnit, asserts | Muito rápida |
| Aplicação | Orquestração, autorização e portas | JUnit + doubles controlados | Rápida |
| Persistência | Mapeamento, query, constraints | Spring test + Testcontainers | Média |
| API/segurança | HTTP, JSON, filtros e status | MockMvc ou teste HTTP | Média |
| Fluxo | Jornada integrada | Bruno | Mais lenta/manual ou CLI |

## Matriz mínima por funcionalidade

| Funcionalidade | Feliz | Limite | Falha | Segurança | Concorrência |
|---|---|---|---|---|---|
| Cadastro | conta válida | tamanho de senha | e-mail duplicado | campos proibidos | unicidade |
| Personagem | primeiro personagem | terceiro permitido | quarto rejeitado | A acessa B | duas criações simultâneas |
| Equipamento | slot compatível | troca no mesmo slot | item alheio/incompatível | A usa item de B | duas trocas |
| Missão | concluir ativa | XP sobe níveis | estado terminal | tentativa alheia | recompensa repetida |
| Batalha | ataque válido | dano mínimo 1 | turno errado/mana | batalha alheia | duas ações mesma versão |
| Ranking | página ordenada | página vazia/máximo | parâmetro inválido | sem dado privado | resultado contado uma vez |

## Testes unitários do domínio

Use Arrange–Act–Assert e nome que descreva comportamento. Evite subir Spring para testar fórmula ou transição.

Casos essenciais:

- XP exata, abaixo, acima e múltiplos níveis;
- equipar, trocar, incompatibilidade e item ausente;
- transições válidas e terminais de missão;
- dano mínimo e morte;
- mana e cooldown;
- turno alternado;
- batalha termina antes de novo turno;
- idempotência do objeto quando aplicável.

## Testes de aplicação

Verifique:

- identidade atual é usada;
- Repository recebe consulta por proprietário;
- transação engloba alterações;
- falha não chama dependência seguinte;
- resultado de domínio vira DTO;
- erro mantém código público.

Mocks não devem repetir implementação. Use fake pequeno quando o comportamento em memória torna o teste mais legível.

## Testes de integração com PostgreSQL

Use Testcontainers para validar:

- migrations;
- tipos e constraints reais;
- unicidade case-insensitive escolhida;
- optimistic locking;
- consulta de ranking;
- índices e SQL específico;
- rollback.

Não substitua PostgreSQL por H2 nos riscos que dependem do banco.

## Teste de concorrência

Roteiro para batalha:

1. criar batalha na versão N;
2. sincronizar duas threads para ler N;
3. ambas tentam ação válida;
4. liberar gravações juntas;
5. aguardar resultados;
6. afirmar uma ação efetiva;
7. afirmar uma rejeição/releitura;
8. verificar vida, turno, versão e quantidade de ações no banco.

O teste precisa ter timeout para não travar a suíte.

## Estrutura da coleção Bruno

~~~text
bruno/
├── environments/
│   ├── local.bru
│   └── deployed.bru.example
├── 01-auth/
│   ├── 01-register.bru
│   ├── 02-login.bru
│   └── 03-invalid-login.bru
├── 02-characters/
├── 03-inventory/
├── 04-missions/
├── 05-battles/
└── 06-ranking/
~~~

Variáveis:

- baseUrl;
- accessTokenA e accessTokenB;
- characterIdA e characterIdB;
- inventoryItemId;
- missionAttemptId;
- battleId;
- currentVersion;
- idempotencyKey.

## Assertions no Bruno

Cada requisição relevante verifica:

- status;
- Content-Type;
- campos essenciais e tipos;
- ausência de passwordHash e dados privados;
- código do erro;
- mudança de estado;
- repetição idempotente;
- tempo apenas como observação, não garantia rígida local.

## Fluxos obrigatórios

### Fluxo A — jornada feliz

Cadastro → login → personagem → inventário → equipamento → missão → recompensa → batalha → ranking.

### Fluxo B — isolamento

Criar A e B → autenticar como A → tentar characterId, item, tentativa e battleId de B → nenhuma informação de B é devolvida.

### Fluxo C — repetição

Repetir conclusão de missão e ação de batalha com mesma chave → efeito único e resposta documentada.

### Fluxo D — erros de estado

Concluir missão finalizada, agir fora do turno, usar habilidade em cooldown e agir em batalha encerrada.

## Evidências

Salvar no repositório:

- coleção Bruno sem segredos;
- saída do verify no PR;
- relatório de testes quando disponível;
- tabela ligando REG-xx a testes;
- captura da CI;
- instrução de reprodução.

## Antipadrões

- testar apenas status 200;
- testar implementação privada;
- usar Thread.sleep como sincronização principal;
- mockar entidade e regra em excesso;
- compartilhar estado entre testes;
- depender da ordem;
- aceitar teste intermitente;
- declarar “cobertura alta” sem cenários críticos.
