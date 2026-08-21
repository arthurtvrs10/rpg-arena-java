# Dia 21 — OpenAPI, erros, logs e Actuator

**Data:** 09/09/2026  
**Sprint:** 4  
**Tempo núcleo:** 2h  
**Extensão:** 90 min  
**Resultado:** sistema explicável e diagnosticável sem expor detalhes.

## Antes de começar

- [ ] Congele contratos funcionais.
- [ ] Liste todos os códigos de erro.
- [ ] Crie branch docs/OP-01-contract-observability.
- [ ] Defina trace/correlation id.

## O que você precisa compreender

- OpenAPI é contrato, não substituto de teste.
- Erro estável usa código; mensagem pode mudar.
- Log registra evento para diagnóstico, não dump de objeto.
- TraceId conecta resposta e log.
- Health/liveness/readiness têm propósitos diferentes.
- Métricas não devem vazar dados.

## Fontes oficiais

- OpenAPI 3.1.1: https://spec.openapis.org/oas/v3.1.1.html
- Problem Details: https://www.rfc-editor.org/rfc/rfc9457.html
- Spring Boot Actuator: https://docs.spring.io/spring-boot/reference/actuator/
- Spring Boot logging: https://docs.spring.io/spring-boot/reference/features/logging.html

## Exemplo neutro — processamento de pedido

Quando pedido falha, cliente recebe ORDER_ALREADY_PAID e traceId. Log interno registra orderId, ator, resultado e latência, mas não cartão. Health não devolve credenciais nem stack.

## Tarefa prática

### 1. Catálogo de erros, 20 min

Crie docs/API.md com:

- code;
- status;
- situação;
- campos;
- exemplo.

Revise inconsistências entre módulos.

### 2. Handler global, 25 min

Mapeie:

- validação;
- regra;
- não encontrado;
- acesso;
- conflito de versão/unique;
- erro inesperado.

Use Problem Details ou formato compatível documentado. Nunca devolva exception.getMessage de infraestrutura diretamente.

### 3. OpenAPI, 30 min

Documente:

- segurança;
- schemas de entrada/saída;
- status e erros;
- paginação;
- Idempotency-Key;
- exemplos mínimos;
- version.

Compare contrato gerado com Bruno.

### 4. Logs correlacionados, 20 min

Defina eventos:

- auth success/failure sem credencial;
- character created;
- mission reward granted/retried;
- battle action/conflict/finished;
- deploy startup/migration.

Campos: traceId, actorId seguro, resourceId, action, outcome e duration. Redija cabeçalhos sensíveis.

### 5. Actuator, 15 min

Exponha apenas health e info/metrics necessários. Diferencie configuração local/deploy. Garanta proteção de detalhes.

### 6. Testes/evidência, 10 min

Gere erro conhecido e inesperado controlado, encontre pelo traceId e revise resposta.

## Critérios de aceite

- [ ] todos endpoints Must no OpenAPI;
- [ ] códigos de erro documentados;
- [ ] validação lista campos;
- [ ] 500 não expõe internals;
- [ ] traceId aparece em resposta/log;
- [ ] log não contém segredo;
- [ ] health é mínimo;
- [ ] Bruno e contrato não divergem.

## Testes obrigatórios

- erro de validação com dois campos;
- conflito de estado;
- optimistic lock;
- acesso negado;
- 500 controlado;
- correlação de trace;
- busca por segredo;
- OpenAPI abre/valida.

## Evidências

- docs/API.md;
- spec/endpoint de docs;
- logs redigidos;
- testes;
- commit: docs(api): publish contract errors and safe observability.

## Perguntas de recuperação

1. Por que code é separado de detail?
2. O que traceId resolve?
3. O que não deve ir ao log?
4. Qual diferença health e readiness?
5. OpenAPI prova regra?

## Erros comuns

- documentar apenas 200;
- mensagem da constraint pública;
- logar request inteiro;
- actuator aberto;
- traceId novo em cada camada;
- documentação incompatível com resposta.

## Extensão opcional

Valide a especificação com ferramenta de lint OpenAPI. Corrija apenas erros objetivos; não mude contrato por estilo no fim.

## Conteúdo

“Como transformar erro 500 em diagnóstico sem vazar a aplicação”.

## Correção e conferência — só depois da tentativa

A resposta pública identifica tipo, status, code, detail seguro, instance, timestamp e traceId. O log interno usa o mesmo traceId e registra causa com acesso restrito. Senha, hash, token, corpo completo e SQL sensível não aparecem.
