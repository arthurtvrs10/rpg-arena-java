# Riscos e trade-offs

## Registro de riscos

| ID | Risco | Prob. | Impacto | Sinal | Mitigação | Contingência |
|---|---|---:|---:|---|---|---|
| R1 | Escopo não cabe em 30 dias | Alta | Alto | Must acumulado na quinta | WIP 1 e fatias verticais | Remover Should/Could |
| R2 | Regra fica no Controller | Média | Alto | testes exigem HTTP para tudo | domínio Java puro | refatorar antes de expandir |
| R3 | Acesso cruzado BOLA | Média | Crítico | consultas apenas por id | owner no caso de uso/query | bloquear release |
| R4 | Recompensa duplicada | Alta | Alto | retry aumenta XP | idempotência + unique | bloquear release |
| R5 | Corrida no turno | Alta | Alto | duas ações aceitas | version + teste concorrente | serializar ação temporariamente |
| R6 | Migrations divergentes | Média | Alto | só funciona no banco local | criar do zero na CI/teste | recriar ambiente |
| R7 | Teste H2 mascara PostgreSQL | Média | Alto | SQL diferente | Testcontainers | teste manual SQL até corrigir |
| R8 | JWT mal configurado | Média | Crítico | token alterado aceito | algoritmo fixo e testes | desabilitar deploy |
| R9 | Segredo versionado | Baixa | Crítico | scanner/diff encontra | env e revisão | revogar e limpar conforme procedimento |
| R10 | CI lenta/instável | Média | Médio | PR ignorado | separar testes e cache | manter suíte crítica obrigatória |
| R11 | Deploy consome o mês | Média | Médio | três dias em provedor | timebox e alternativa local | demo Docker local |
| R12 | Cópia sem compreensão | Média | Alto | não explica decisão | exemplo neutro + recuperação | reimplementar pequena fatia |

## Decisões e alternativas

### Monólito modular versus microsserviços

Escolha: monólito modular.

Motivo: um produto, uma pessoa, um mês e transações fortes. Microsserviços adicionariam rede, observabilidade distribuída, deploys e consistência entre serviços sem necessidade demonstrada.

Sinal de revisão: equipes independentes, limites estáveis e gargalo operacional medido.

### Optimistic versus pessimistic locking

Escolha inicial: optimistic locking na batalha.

Vantagem: simples para conflitos raros e duração curta.

Custo: cliente/caso de uso precisa tratar conflito.

Sinal de revisão: taxa alta de conflito medida ou processamento exclusivo obrigatório.

### Entidade rica versus service procedural

Escolha: invariantes e transições próximas ao objeto de domínio; orquestração no caso de uso.

Risco evitado: setters públicos permitem estado impossível.

Limite: não colocar acesso a banco ou autenticação na entidade.

### Ranking como projeção versus consulta agregada toda vez

Escolha: projeção simples atualizada quando resultado é contabilizado.

Vantagem: leitura previsível.

Custo: exige idempotência e possibilidade de reconstrução.

Alternativa segura se faltar tempo: consulta agregada paginada, documentando custo.

### JWT versus sessão

Escolha do projeto: token bearer por exigência de portfólio/API.

Trade-off: revogação e rotação ficam mais complexas. Não afirmar que JWT é “mais seguro” por si só.

### H2 versus PostgreSQL nos testes

Escolha: PostgreSQL em container para integração. Regras puras continuam sem banco.

Motivo: constraints, SQL e concorrência são riscos reais do projeto.

## Orçamento de complexidade

Cada tecnologia nova gasta capacidade em configuração, falha, documentação, teste e operação. No mês, o orçamento já está comprometido com Spring, PostgreSQL, segurança, Testcontainers, Bruno, Docker e Actions. Redis, Kafka e Kubernetes excedem o orçamento.

## Registro de dívida

Formato:

- ID:
- Contexto:
- Atalho:
- Risco:
- Evidência:
- Condição para pagar:
- Prioridade:

Dívida documentada não significa que toda pendência é aceitável. Falha de propriedade, perda de dados ou segredo exposto bloqueiam release.

## Perguntas para defender decisões

- Qual requisito motivou a escolha?
- Quais alternativas reais foram consideradas?
- Qual risco foi reduzido?
- Qual custo foi aceito?
- Como a decisão é testada?
- Que sinal faria revisar?
