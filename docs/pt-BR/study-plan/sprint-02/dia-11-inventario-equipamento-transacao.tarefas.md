# Dia 11 — Inventário e equipamento transacional

**Data:** 28/08/2026  
**Sprint:** 2  
**Tempo núcleo:** 2h  
**Extensão:** 90 min  
**Resultado:** equipar e desequipar com posse, slot e atomicidade.

## Antes de começar

- [ ] Defina itens mínimos e slots.
- [ ] Use personagem próprio criado no Dia 10.
- [ ] Crie branch feat/IN-02-equipment.
- [ ] Escreva as invariantes REG-IN antes do código.

## O que você precisa compreender

- Item de catálogo é diferente da instância possuída.
- Trocar slot altera dois itens e possivelmente atributos: uma unidade transacional.
- Posse deve ser verificada para personagem e item.
- Operação repetida pode ser idempotente.
- Constraint protege invariantes sob concorrência.
- Atributo derivado deve ser recalculado, não incrementado cegamente.

## Fontes

- Spring transactions: https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative.html
- Spring Data transactions: https://docs.spring.io/spring-data/jpa/reference/jpa/transactions.html
- PostgreSQL constraints: https://www.postgresql.org/docs/current/ddl-constraints.html
- PostgreSQL partial indexes: https://www.postgresql.org/docs/current/indexes-partial.html

## Exemplo neutro — atribuição de veículo

Veículo do catálogo/frota é diferente do modelo. Um motorista só recebe veículo da unidade correta; um slot de atribuição tem no máximo um ativo. Troca precisa encerrar anterior e criar nova atribuição na mesma transação.

## Tarefa prática

### 1. Modelo e tabela de decisão, 20 min

Itens mínimos:

- sword → MAIN_HAND, +5 attack;
- leather_helmet → HEAD, +3 defense;
- robe → CHEST, +10 health;
- ring → ACCESSORY, +5 mana.

Preveja resultados de equipar, trocar, repetir, incompatível, item de B e consumido.

### 2. Migration, 20 min

Crie item_catalog e inventory_items com:

- owner character;
- item catalog;
- status;
- equipped_slot;
- version;
- índices;
- constraints possíveis.

Decida se slot equipado é representado no item ou em tabela equipment. Registre trade-off.

### 3. Domínio, 25 min

Modele operações:

- equip(item, slot);
- unequip(slot);
- derivedStats().

Mantenha invariantes e resultado explícito. Recalcule a partir da base + itens para evitar drift.

### 4. Caso de uso, 25 min

Em transação:

1. obter owner atual;
2. carregar personagem próprio e inventário necessário;
3. validar item próprio/status/compatibilidade;
4. localizar item atual do slot;
5. aplicar troca;
6. persistir;
7. devolver equipamento/atributos.

### 5. Testes, 30 min

- equipar vazio;
- trocar;
- repetir o mesmo;
- slot errado;
- item de B;
- personagem de B;
- item consumido;
- falha no segundo save e rollback;
- duas trocas concorrentes, ao menos como risco/teste planejado.

### 6. API/Bruno/evidência, 20 min

Implemente PUT e DELETE do contrato, assertions e resposta sem entidade.

## Critérios de aceite

- [ ] catálogo e posse são separados;
- [ ] item e personagem pertencem à identidade;
- [ ] um slot tem no máximo um item;
- [ ] incompatível falha sem mutação;
- [ ] troca é atômica;
- [ ] repetição não soma bônus novamente;
- [ ] atributos derivados não sofrem drift;
- [ ] Bruno cobre A contra B.

## Testes obrigatórios

Compare atributos antes/depois:

- equipar sword aumenta ataque uma vez;
- repetir mantém total;
- trocar por outra arma remove bônus anterior;
- falha deixa estado idêntico;
- item de B não revela nome/atributos;
- rollback preserva os dois itens.

## Evidências

- decisão de modelagem;
- migration;
- testes;
- requests;
- commit: feat(inventory): equip owned items atomically by slot.

## Perguntas de recuperação

1. Por que catálogo e instância são diferentes?
2. Qual é a unidade transacional?
3. Como evitar somar bônus duas vezes?
4. Que constraint apoia o slot?
5. O que ocorre se item pertencer a B?

## Erros comuns

- item global diretamente equipado;
- bônus total armazenado e incrementado;
- dois saves fora de transação;
- validar só character owner;
- status/slot inconsistentes;
- retornar 500 por regra previsível.

## Extensão opcional

Escreva teste concorrente de duas armas no mesmo slot. Se a modelagem não consegue garantir uma, registre e ajuste constraint/locking.

## Conteúdo

“Uma troca de equipamento é pequena, mas não é um CRUD”.

## Correção e conferência — só depois da tentativa

Após qualquer operação válida, derive stats de base + conjunto atual. Uma repetição do mesmo item/slot deve ser no-op ou devolver o mesmo resultado. Se a segunda atualização falhar, a primeira não pode permanecer.

Uma tabela equipment separada torna a unicidade por character+slot direta; slot no inventory item pode simplificar leitura, mas exige constraint/índice parcial e coerência de status. Ambas podem ser defendidas.
