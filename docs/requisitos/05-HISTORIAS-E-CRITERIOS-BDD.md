# Histórias de usuário e critérios BDD

Cada história só entra em desenvolvimento quando a dependência indicada estiver concluída. Os cenários abaixo são critérios de aceite; detalhes adicionais permanecem nas regras e casos de uso.

## US-AUT-01 — Cadastrar e autenticar

**Como** visitante, **quero** criar conta e autenticar **para** acessar meu progresso.  
**Prioridade:** Must. **Semana:** 11. **Dependência:** banco e contrato REST.

```gherkin
Cenário: cadastrar conta válida
  Dado que não existe conta para "julia@example.com"
  Quando cadastro nome "Júlia", e-mail " JULIA@example.com " e senha válida
  Então recebo 201 sem senha ou hash
  E a conta é persistida como ACTIVE e PLAYER com e-mail normalizado

Cenário: não enumerar e-mail no login
  Quando tento login com e-mail inexistente ou senha incorreta
  Então recebo 401 com o mesmo código INVALID_CREDENTIALS
```

## US-AUT-02 — Renovar e encerrar sessão

**Como** jogador, **quero** renovar e encerrar sessão **para** manter acesso seguro.  
**Prioridade:** Must. **Semana:** 11.

```gherkin
Cenário: rotação de refresh
  Dado um refresh token válido
  Quando solicito renovação
  Então o token anterior é marcado como usado
  E recebo um novo par da mesma família

Cenário: detectar reutilização
  Dado que um refresh token já foi usado
  Quando tento usá-lo novamente
  Então recebo 401 REFRESH_TOKEN_REUSED
  E toda a família é revogada
```

## US-CHR-01 — Criar personagem

**Como** jogador, **quero** criar um personagem de uma classe publicada **para** iniciar a jornada.  
**Prioridade:** Must. **Semanas:** 3, 5 e 10.

```gherkin
Cenário: criar personagem com kit inicial
  Dado um jogador com dois personagens ativos e a classe WARRIOR publicada
  Quando cria "Arin"
  Então Arin nasce no nível 1, XP 0, vida e mana máximas
  E recebe kit inicial e posição VILA_DE_ASTER na mesma transação

Cenário: rejeitar quarto personagem
  Dado um jogador com três personagens ativos
  Quando tenta criar outro
  Então recebe 409 CHARACTER_LIMIT_REACHED
  E nenhum personagem, item ou posição é criado
```

## US-CHR-02 — Evoluir personagem

**Como** jogador, **quero** receber XP e subir de nível **para** fortalecer meu personagem.  
**Prioridade:** Must. **Semana:** 7.

```gherkin
Cenário: subir vários níveis
  Dado um personagem de nível 1 com XP 0
  Quando recebe XP suficiente para ultrapassar dois limiares
  Então o nível sobe duas vezes
  E o saldo de XP corresponde às subtrações de 100 × nível²

Cenário: respeitar nível máximo
  Dado um personagem no nível 50
  Quando recebe XP
  Então permanece no nível 50 com XP 0
```

## US-INV-01 — Equipar item

**Como** jogador, **quero** equipar itens próprios **para** alterar meus atributos.  
**Prioridade:** Must. **Semanas:** 6 e 10.

```gherkin
Cenário: trocar arma atomicamente
  Dado um personagem com uma espada equipada e um machado compatível no inventário
  Quando equipa o machado em WEAPON
  Então a espada volta para OWNED, o machado fica EQUIPPED
  E os atributos derivados refletem somente o machado

Cenário: impedir item de outro jogador
  Dado o identificador de um item pertencente a outra conta
  Quando tento equipá-lo
  Então recebo 404 RESOURCE_NOT_FOUND
  E nenhum estado é alterado
```

## US-INV-02 — Consumir e receber loot

**Como** jogador, **quero** usar consumíveis e receber loot **para** sustentar a progressão.  
**Prioridade:** Must. **Semanas:** 6 e 14.

```gherkin
Cenário: consumir uma poção
  Dado uma pilha de duas poções e vida abaixo do máximo
  Quando uso uma poção
  Então a vida aumenta sem ultrapassar o máximo
  E a pilha passa a uma unidade

Cenário: inventário cheio no loot
  Dado um inventário com 40 pilhas sem possibilidade de empilhar
  Quando uma recompensa contém um novo item
  Então a recompensa inteira permanece não resgatada
  E recebo INVENTORY_FULL
```

## US-CBT-01 — Iniciar batalha

**Como** jogador, **quero** iniciar uma batalha elegível **para** enfrentar um inimigo.  
**Prioridade:** Must. **Semanas:** 4 e 12.

```gherkin
Cenário: criar snapshot e primeiro turno
  Dado Arin com velocidade 8 e um inimigo publicado com velocidade 6
  Quando inicio a batalha
  Então a batalha fica IN_PROGRESS com snapshots persistidos
  E o turno atual pertence a Arin

Cenário: impedir duas batalhas ativas
  Dado que Arin já está em batalha IN_PROGRESS
  Quando tenta iniciar outra
  Então recebe 409 CHARACTER_BUSY
```

## US-CBT-02 — Atacar, defender e usar habilidade

**Como** jogador, **quero** escolher uma ação no meu turno **para** vencer a batalha.  
**Prioridade:** Must. **Semanas:** 4, 7 e 12.

```gherkin
Cenário: ataque básico válido
  Dado uma batalha em andamento no turno de Arin
  Quando envio BASIC_ATTACK com versão e chave novas
  Então o dano é max(1, ataque - defesa)
  E o evento é registrado antes da resposta do inimigo

Cenário: habilidade sem mana
  Dado que Arin não possui mana suficiente
  Quando tenta usar a habilidade
  Então recebe 409 INSUFFICIENT_RESOURCE
  E mana, cooldown, eventos e turno permanecem iguais

Cenário: defesa reduz próximo dano
  Dado que Arin escolheu DEFEND
  Quando recebe o próximo dano
  Então o dano é reduzido em 40 por cento com mínimo 1
  E a proteção é removida
```

## US-CBT-03 — Impedir duplicidade e corrida

**Como** jogador, **quero** que repetição e concorrência sejam tratadas **para** não perder progresso.  
**Prioridade:** Must. **Semanas:** 10 e 12.

```gherkin
Cenário: repetir mesma ação
  Dado uma ação já concluída com uma Idempotency-Key
  Quando repito a mesma chave e o mesmo corpo
  Então recebo o resultado original
  E nenhum novo evento, dano ou turno é criado

Cenário: duas ações para a mesma versão
  Dado duas requisições simultâneas com expectedVersion 3
  Quando ambas tentam agir
  Então somente uma atualiza a batalha
  E a outra recebe 409 BATTLE_CONCURRENTLY_MODIFIED
```

## US-QST-01 — Aceitar e avançar missão

**Como** jogador, **quero** aceitar missão e avançar objetivos **para** seguir a história.  
**Prioridade:** Must. **Semanas:** 8 e 12.

```gherkin
Cenário: aceitar versão publicada
  Dado uma missão publicada e requisitos atendidos
  Quando Arin aceita a missão
  Então é criada instância ACTIVE ligada à versão atual

Cenário: evento repetido
  Dado que o evento de vitória E-123 já avançou o objetivo
  Quando E-123 é processado novamente
  Então o progresso não aumenta novamente
```

## US-QST-02 — Escolher consequência narrativa

**Como** jogador, **quero** escolher opções disponíveis **para** mudar a jornada.  
**Prioridade:** Must. **Semana:** 15.

```gherkin
Cenário: aplicar escolha válida
  Dado uma instância no nó ENCRUZILHADA com a escolha AJUDAR disponível
  Quando confirmo AJUDAR
  Então a escolha fica imutável
  E flags, objetivo e próximo nó são atualizados atomicamente

Cenário: tentar escolha bloqueada
  Quando envio uma opção inexistente ou sem pré-requisito
  Então recebo 409 CHOICE_NOT_AVAILABLE
  E a instância permanece no mesmo nó
```

## US-QST-03 — Resgatar recompensa uma vez

**Como** jogador, **quero** resgatar a recompensa concluída **para** evoluir sem duplicidade.  
**Prioridade:** Must. **Semana:** 8.

```gherkin
Cenário: resgate atômico
  Dado uma missão COMPLETED e inventário com espaço
  Quando resgato a recompensa
  Então XP, ouro e itens são aplicados juntos
  E a instância fica REWARDED

Cenário: repetir resgate
  Dado que a recompensa já foi concedida
  Quando repito a requisição
  Então recebo o resumo original
  E nenhum valor é concedido outra vez
```

## US-WLD-01 — Viajar e encontrar inimigo

**Como** jogador, **quero** viajar por locais conectados **para** explorar o mundo.  
**Prioridade:** Must. **Semana:** 13.

```gherkin
Cenário: viajar por conexão válida
  Dado Arin em VILA_DE_ASTER e uma conexão ativa para FLORESTA_SUSSURRANTE
  Quando viaja com ouro suficiente
  Então custo e posição são atualizados na mesma transação
  E o encontro é escolhido somente entre opções elegíveis

Cenário: impedir teletransporte
  Dado um destino sem conexão a partir do local atual
  Quando tento viajar
  Então recebo 409 TRAVEL_NOT_ALLOWED
  E posição e ouro não mudam
```

## US-ECO-01 — Comprar item

**Como** jogador, **quero** comprar de um comerciante local **para** preparar meu personagem.  
**Prioridade:** Must. **Semana:** 14.

```gherkin
Cenário: comprar com sucesso
  Dado ouro, estoque e espaço suficientes
  Quando compro duas poções
  Então ouro, estoque, inventário e ledger são atualizados atomicamente

Cenário: disputar último item
  Dado estoque igual a um
  Quando duas compras simultâneas são processadas
  Então uma tem sucesso e a outra recebe conflito
  E o estoque final é zero, nunca negativo
```

## US-ECO-02 — Vender item

**Como** jogador, **quero** vender item elegível **para** obter ouro.  
**Prioridade:** Must. **Semana:** 14.

```gherkin
Cenário: vender item próprio
  Dado um item vendável, próprio e não equipado
  Quando vendo uma unidade
  Então o item é removido, o ouro creditado e o ledger gravado juntos

Cenário: impedir venda de equipado
  Dado um item equipado
  Quando tento vendê-lo
  Então recebo 409 ITEM_IN_USE
  E os saldos permanecem iguais
```

## US-ADM-01 — Criar e publicar conteúdo

**Como** administrador, **quero** publicar conteúdo validado **para** ampliar o jogo sem editar o banco.  
**Prioridade:** Must. **Semana:** 16.

```gherkin
Cenário: publicar rascunho válido
  Dado um rascunho com referências e schema válidos
  Quando o ADMIN publica
  Então nasce uma versão PUBLISHED imutável
  E a operação é auditada com autor e instante

Cenário: rejeitar publicação inconsistente
  Dado um rascunho de missão apontando para item inexistente
  Quando o ADMIN publica
  Então recebe 422 CONTENT_VALIDATION_FAILED com caminho do campo
  E nenhuma versão se torna publicada
```

## US-SEC-01 — Isolar recursos por proprietário

**Como** jogador, **quero** que meus recursos sejam privados **para** impedir acesso horizontal.  
**Prioridade:** Must. **Semana:** 12.

```gherkin
Esquema do Cenário: esconder recurso alheio
  Dado que o jogador B possui um <recurso>
  E estou autenticado como jogador A
  Quando uso o identificador do recurso de B
  Então recebo 404 RESOURCE_NOT_FOUND
  E a resposta não contém dados de B

  Exemplos:
    | recurso          |
    | personagem       |
    | item de inventário |
    | instância de missão |
    | batalha          |
```

## US-RNK-01 — Consultar ranking

**Como** visitante, **quero** consultar ranking **para** comparar progresso público.  
**Prioridade:** Must. **Semana:** 19.

```gherkin
Cenário: ordenar empates de forma determinística
  Dado personagens com mesmas vitórias, derrotas e nível
  Quando consulto o ranking duas vezes
  Então a ordem final por characterId é idêntica
  E nenhum e-mail ou accountId é retornado
```

## US-OPS-01 — Executar e verificar o sistema

**Como** avaliador, **quero** iniciar e validar o projeto **para** reproduzir as evidências.  
**Prioridade:** Must. **Semanas:** 18–21.

```gherkin
Cenário: clone limpo
  Dado uma máquina com Git e Docker compatíveis
  Quando sigo o README e executo docker compose up --build
  Então API e PostgreSQL ficam saudáveis
  E o smoke test e a coleção principal passam sem editar código
```

## Definition of Ready de cada história

- ator e valor identificados;
- requisito, regras e caso de uso ligados;
- dependências concluídas;
- entrada, saída e erros conhecidos;
- impacto de banco, segurança, transação e idempotência analisado;
- cenários de aceite executáveis;
- estimativa máxima de 2 dias; caso maior, fatiar.

## Definition of Done de cada história

- implementação e migrations versionadas;
- testes exigidos pelo risco passando;
- OpenAPI e Bruno atualizados;
- nenhuma entidade JPA exposta;
- logs sem segredo;
- PR ligado à issue com evidência;
- CI verde;
- documentação e tarefa semanal atualizadas;
- material de gravação capturado quando previsto.
