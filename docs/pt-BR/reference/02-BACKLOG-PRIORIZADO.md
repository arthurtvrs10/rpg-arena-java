# Backlog priorizado

## Convenções

- Prioridade: Must, Should ou Could.
- Pontos: comparação relativa de esforço e incerteza, não horas.
- Valor: impacto no ciclo principal.
- Risco: possibilidade de falha técnica ou de segurança.
- Uma história só entra na sprint após cumprir Definition of Ready.

## Backlog do MVP

| ID | História | Pri. | Pontos | Valor | Risco | Sprint | Dependência |
|---|---|---:|---:|---:|---:|---:|---|
| EN-01 | Repositório, build e ambientes | Must | 3 | 5 | 2 | 1 | Nenhuma |
| EN-02 | PostgreSQL, Flyway e healthcheck | Must | 5 | 5 | 3 | 1 | EN-01 |
| CH-01 | Criar personagem com limite | Must | 5 | 5 | 3 | 1/2 | EN-02, AU-01 |
| CH-02 | Evoluir XP e nível | Must | 3 | 5 | 3 | 1 | Nenhuma para regra pura |
| AU-01 | Cadastro seguro | Must | 5 | 5 | 4 | 2 | EN-02 |
| AU-02 | Login e emissão de JWT | Must | 5 | 5 | 5 | 2 | AU-01 |
| AU-03 | Política de propriedade | Must | 5 | 5 | 5 | 2 | AU-02 |
| IN-01 | Consultar inventário próprio | Must | 3 | 4 | 4 | 2 | AU-03, CH-01 |
| IN-02 | Equipar e desequipar item | Must | 5 | 5 | 4 | 2 | IN-01 |
| MI-01 | Iniciar tentativa de missão | Must | 5 | 5 | 3 | 3 | CH-01 |
| MI-02 | Concluir/falhar por estado | Must | 5 | 5 | 4 | 3 | MI-01 |
| MI-03 | Aplicar recompensa uma vez | Must | 8 | 5 | 5 | 3 | MI-02, CH-02 |
| BA-01 | Criar batalha PvE | Must | 5 | 5 | 3 | 3 | CH-01 |
| BA-02 | Ataque básico determinístico | Must | 5 | 5 | 4 | 3 | BA-01 |
| BA-03 | Habilidade, mana e cooldown | Should | 5 | 4 | 4 | 3 | BA-02 |
| BA-04 | Turno e encerramento | Must | 5 | 5 | 5 | 3 | BA-02 |
| BA-05 | Idempotência e concorrência | Must | 8 | 5 | 5 | 3 | BA-04 |
| RA-01 | Ranking paginado | Must | 5 | 4 | 3 | 4 | BA-04 |
| OP-01 | Erros e correlação de logs | Must | 3 | 4 | 3 | 4 | APIs existentes |
| OP-02 | OpenAPI e coleção Bruno | Must | 5 | 5 | 2 | 4 | APIs existentes |
| QA-01 | Testcontainers | Must | 5 | 5 | 4 | 4 | EN-02 |
| QA-02 | Testes de segurança | Must | 5 | 5 | 5 | 4 | AU-03 |
| DE-01 | Docker Compose completo | Must | 3 | 5 | 3 | 4 | EN-02 |
| DE-02 | GitHub Actions | Must | 3 | 5 | 3 | 4 | Testes |
| DE-03 | Release e deploy | Must | 5 | 5 | 4 | 4 | DE-01, DE-02 |
| AD-01 | Administração de itens | Should | 5 | 3 | 3 | 4 | AU-02 |
| HI-01 | Histórico detalhado de batalha | Could | 5 | 2 | 3 | Pós-MVP | BA-04 |
| EV-01 | Eventos e outbox | Could | 8 | 2 | 5 | Pós-MVP | MVP estável |

## Ordem recomendada dentro da sprint

1. atacar risco desconhecido primeiro;
2. produzir uma fatia executável;
3. fechar teste e evidência;
4. só então iniciar outra história.

## Exemplo de refinamento

História ampla: “fazer batalha”.

Fatiamento:

1. criar batalha com combatentes e estado inicial;
2. calcular ataque básico em memória;
3. persistir uma ação válida;
4. alternar turno;
5. encerrar ao chegar a zero pontos de vida;
6. rejeitar ator errado;
7. impedir repetição;
8. tratar concorrência.

Cada item deve produzir comportamento testável.

## Itens técnicos que não são histórias de usuário

Itens como pipeline, migration ou logs permanecem no backlog porque reduzem risco de entrega. Eles precisam de resultado observável e critério de aceite, não devem ser adicionados como tarefas vagas do tipo “estudar Docker”.

## Política de mudança

Durante a sprint:

- defeito que impede o Sprint Goal substitui item de mesmo tamanho;
- funcionalidade nova vai ao backlog;
- tecnologia nova exige problema, alternativa e impacto documentados;
- item Must incompleto impede iniciar item Could;
- Product Owner reduz escopo, não qualidade essencial.

## Roteiro de refinamento de 15 minutos

1. Quem se beneficia?
2. Qual comportamento muda?
3. Quais regras podem ser violadas?
4. Qual o menor fluxo demonstrável?
5. Quais falhas precisam de teste?
6. Há migration, segurança ou transação?
7. Cabe em um dia?
8. Qual evidência prova conclusão?
