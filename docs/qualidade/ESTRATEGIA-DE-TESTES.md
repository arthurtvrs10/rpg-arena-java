# Estratégia de testes baseada em risco

## Objetivo

Detectar violações de regra, segurança, consistência e contrato. Cobertura é indicador secundário; cada risco crítico precisa de teste que falhe quando o risco ocorrer.

## Camadas

| Camada | Ferramenta | Testa | Não deve testar |
|---|---|---|---|
| domínio | JUnit + AssertJ | invariantes, fórmulas, estados, Clock/Random | Spring, banco, JSON |
| aplicação | JUnit + fakes/Mockito | orquestração, autorização, transação lógica, eventos | detalhes JPA |
| persistência | Testcontainers PostgreSQL | mapeamento, query, constraint, lock, migration | regra duplicada sem necessidade |
| web slice | Spring MVC Test | status, DTO, validação, segurança e Problem Details | banco real quando não necessário |
| integração | Spring Boot + PostgreSQL | fatia vertical e rollback | todos os casos combinatórios do domínio |
| contrato/jornada | Bruno CLI | fluxo externo, variáveis e erros críticos | detalhes internos |
| arquitetura | ArchUnit | dependências entre módulos/camadas | comportamento funcional |
| carga | k6/Gatling ou equivalente | latência, throughput, erros e gargalos | “provar escala infinita” |

## Riscos críticos e testes

| Risco | Teste mínimo |
|---|---|
| acesso horizontal | A usa ID de personagem, item, missão e batalha de B |
| recompensa duplicada | duas requisições concorrentes e repetição após timeout |
| dois turnos vencedores | barreira sincroniza duas ações na mesma versão |
| último estoque vendido duas vezes | duas compras concorrentes; um sucesso |
| migration quebrada | banco vazio e upgrade do marco anterior |
| rollback parcial | falha injetada entre cada passo de recompensa/compra |
| sorte instável | seed/fake gera sequência conhecida |
| relógio instável | Clock fixo controla expiração e cooldown |
| N+1 | contagem/log de queries em listagens críticas |
| segredo exposto | varredura de response/log por padrões proibidos |

## Convenção de nome

`should<Resultado>When<Condição>_<CODIGO_DA_REGRA>`.

Exemplos:

```text
shouldRejectFourthCharacterWhenLimitReached_RN_CHR_003
shouldReturnStoredResultWhenActionIsRepeated_RN_CBT_018
shouldAllowOnlyOnePurchaseWhenLastItemIsContested_RN_ECO_008
```

## Dados de teste

- Test Data Builders com defaults válidos e métodos explícitos para estado inválido.
- IDs, Clock e RandomSource determinísticos.
- Cada teste cria seus próprios dados; não depender de ordem.
- Teste de integração limpa por transação/schema controlado.
- Seeds da aplicação não substituem fixtures de teste.
- Nunca usar e-mail, senha ou token real em fixture.

## Gates

- domínio/application: cobertura mínima inicial 80% linhas e 70% branches após Semana 17, com exclusões justificadas;
- 100% das regras críticas listadas na matriz com ao menos um teste negativo;
- zero teste flaky conhecido;
- suíte unitária ideal < 30 s; verify completo alvo < 10 min no CI;
- PR não faz merge com teste, scanner ou ArchUnit vermelho.

## Execução alvo

```bash
./mvnw test
./mvnw verify
docker compose up --build
bru run bruno/RPG-Arena --env Local
```

Os comandos entram gradualmente. README só deve anunciá-los como funcionais depois da implementação correspondente.

## Revisão por PR

- [ ] o teste falha sem a mudança;
- [ ] cobre feliz, erro e limite proporcionais ao risco;
- [ ] não testa método privado nem implementação irrelevante;
- [ ] não depende de horário, sorte ou ordem global;
- [ ] concorrência realmente executa operações sobrepostas;
- [ ] erro e response não expõem dados;
- [ ] evidência está na issue/PR.
