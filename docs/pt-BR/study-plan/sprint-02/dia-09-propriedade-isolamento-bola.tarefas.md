# Dia 9 — Propriedade, isolamento e BOLA

**Data:** 26/08/2026  
**Sprint:** 2  
**Tempo núcleo:** 2h  
**Extensão:** 60 min  
**Resultado:** jogador A não lê nem altera recursos do jogador B.

## Antes de começar

- [ ] Crie duas contas e tokens distintos.
- [ ] Confirme a política escolhida para recurso alheio.
- [ ] Crie branch feat/AU-03-owner-isolation.
- [ ] Não use id do token diretamente no Controller se isso acoplar regra.

## O que você precisa compreender

- BOLA é risco por objeto, não apenas rota.
- Busca por id seguida de verificação e busca por id+owner têm trade-offs.
- Identificador aleatório não é controle de acesso.
- Administrador não herda propriedade automaticamente.
- Resposta uniforme pode evitar enumeração.
- Teste de segurança precisa de pelo menos duas identidades.

## Fontes

- OWASP API1 BOLA: https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/
- Spring method security: https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html
- Spring Data query methods: https://docs.spring.io/spring-data/jpa/reference/repositories/query-methods-details.html

## Exemplo neutro — faturas

GET /invoices/{id} exige token, mas isso não basta. Repository busca invoice por id e customerId atual, ou aplicação verifica owner antes de mapear. Teste usa fatura de B com token de A e observa que nenhum valor vaza.

## Tarefa prática

### 1. CurrentActor, 20 min

Crie uma abstração na camada de aplicação que devolva o accountId autenticado. A implementação Spring fica em infraestrutura/segurança. Domínio não lê SecurityContext.

Teste:

- identidade presente;
- ausência gera erro controlado;
- claim inválida não vira id.

### 2. Política de consulta, 25 min

Para Character, escolha:

- findByIdAndAccountId; ou
- findById + authorize.

Registre efeitos sobre 404/403, enumeração e reutilização. Implemente uma política consistente.

### 3. Casos de uso próprios, 25 min

Implemente/lista provisória:

- listar meus personagens;
- detalhar meu personagem;
- obter meu perfil.

Não aceite accountId como query/body. Mapeie entidade para resposta.

### 4. Testes A/B, 30 min

Crie:

- conta A e personagem A;
- conta B e personagem B.

Teste A:

- lista contém A e nunca B;
- detalha A;
- tenta id de B;
- tenta id inexistente;
- tenta alterar B;
- tenta injetar accountId de B.

Repita o padrão no inventário assim que existir.

### 5. Bruno, 15 min

Ambiente local guarda tokenA/tokenB. Requests demonstram o ataque e assertion confirma status/código/ausência de dados.

### 6. Revisão, 10 min

Procure no código todos os métodos findById de recursos privados. Registre os que ainda exigem correção.

## Critérios de aceite

- [ ] accountId não é parâmetro público de recursos próprios;
- [ ] domínio não conhece SecurityContext;
- [ ] lista é filtrada no banco;
- [ ] recurso de B não vaza;
- [ ] inexistente e alheio seguem política;
- [ ] testes usam duas contas reais/fakes independentes;
- [ ] Controller não contém if de owner;
- [ ] Bruno reproduz BOLA rejeitado.

## Testes obrigatórios

- A lista próprios;
- A busca A;
- A busca B;
- A altera B;
- token B busca B;
- id aleatório;
- sem token;
- ADMIN tenta agir como jogador, conforme política.

## Evidências

- ADR/política;
- CurrentActor;
- testes;
- coleção;
- busca documentada por findById pendentes;
- commit: fix(security): enforce authenticated ownership on player resources.

## Perguntas de recuperação

1. Por que UUID não substitui autorização?
2. Qual vantagem de buscar por id+owner?
3. Onde deve ficar CurrentActor?
4. Como provar ausência de vazamento?
5. Papel ADMIN implica propriedade?

## Erros comuns

- validar owner apenas no frontend;
- listar tudo e filtrar em memória;
- usar id do path como owner;
- teste com um único usuário;
- 403 com corpo que revela nome de B;
- método admin reutilizado silenciosamente.

## Extensão opcional

Crie teste parametrizado que aplique a mesma matriz de propriedade a diferentes endpoints.

## Conteúdo

“Como um endpoint com JWT ainda pode vazar dados”.

## Correção e conferência — só depois da tentativa

O padrão mais simples para recurso privado é obter accountId do CurrentActor e consultar por id + accountId. Resultado vazio segue a política 404. Para operações complexas, carregar e autorizar explicitamente pode ser legítimo, mas nunca mapear resposta antes da verificação.

Faça busca textual por findById em módulos privados; cada ocorrência precisa de justificativa.
