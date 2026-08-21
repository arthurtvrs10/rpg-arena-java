# Dia 20 — Hardening de segurança baseado em risco

**Data:** 08/09/2026  
**Sprint:** 4  
**Tempo núcleo:** 2h  
**Extensão:** 90 min  
**Resultado:** controles críticos auditados ofensivamente e lacunas documentadas.

## Antes de começar

- [ ] Abra threat model e matriz de autorização.
- [ ] Crie branch test/QA-02-security-hardening.
- [ ] Prepare tokens A, B, ADMIN, expirado e alterado.
- [ ] Não declare conformidade total com OWASP.

## O que você precisa compreender

- Hardening começa pelo risco do produto.
- BOLA e function-level auth são testadas em cada objeto/função.
- Mass assignment ocorre quando cliente controla campo interno.
- Consumo de recursos inclui paginação, corpo e criação repetida.
- Misconfiguration inclui endpoints operacionais e erros.
- Scanner não substitui raciocínio de autorização.

## Fontes oficiais

- OWASP API Top 10: https://owasp.org/API-Security/editions/2023/en/0x11-t10/
- REST Security: https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html
- Spring Security testing: https://docs.spring.io/spring-security/reference/servlet/test/index.html
- Spring Boot Actuator security: https://docs.spring.io/spring-boot/reference/actuator/endpoints.html

## Exemplo neutro — SaaS de documentos

Trocar documentId testa BOLA; chamar rota administrativa testa função; enviar owner/status testa mass assignment; size enorme testa recurso; abrir env/health detalhado testa configuração.

## Tarefa prática

### 1. Inventário de superfície, 15 min

Liste todas as rotas por:

- público/autenticado;
- papel;
- owner;
- entrada;
- custo;
- dado sensível;
- erro.

Qualquer rota esquecida vira issue.

### 2. Ataques de objeto, 25 min

Para character, inventory, missionAttempt e battle:

- A usa id de B;
- A usa id inexistente;
- A tenta alterar;
- A combina character de A com item de B;
- A enumera ids/respostas.

Automatize casos críticos.

### 3. Ataques de função/campo, 20 min

- PLAYER chama todos /admin;
- cadastro envia role/status;
- personagem envia level/XP/owner/stats;
- ação envia damage/actor/winner;
- JSON desconhecido segue política.

### 4. Tokens e erros, 20 min

- ausente;
- malformado;
- expirado;
- assinatura alterada;
- algoritmo/cabeçalho inesperado conforme biblioteca;
- erro 500 seguro;
- 401/403 padronizados.

### 5. Recursos/configuração, 20 min

- size máximo;
- corpo/tamanho documentado;
- login repetido e risco;
- Actuator expõe apenas necessário;
- OpenAPI/health conforme ambiente;
- CORS explícito se existir;
- logs redigidos;
- secrets scan no diff/histórico recente.

### 6. Relatório e correções, 20 min

Classifique:

- corrigido;
- aceito com justificativa;
- bloqueador de release;
- pós-MVP.

Corrija bloqueadores dentro do escopo.

## Critérios de aceite

- [ ] todas as rotas inventariadas;
- [ ] quatro recursos privados testados A/B;
- [ ] ADMIN/PLAYER testados;
- [ ] campos internos não são atribuíveis;
- [ ] tokens inválidos falham;
- [ ] paginação tem limite;
- [ ] Actuator é mínimo;
- [ ] lacunas não são escondidas.

## Testes obrigatórios

Execute matriz completa e procure em resposta/log:

- password;
- hash;
- Authorization;
- secret;
- SQL;
- nome de classe/stack.

## Evidências

- SECURITY.md atualizado;
- matriz rota/controle/teste;
- testes;
- issues de risco;
- commit: test(security): harden API against ownership and function abuse.

## Perguntas de recuperação

1. Qual diferença BOLA e function-level auth?
2. O que é mass assignment no RPG?
3. Que controle limita consumo?
4. Por que 404 pode proteger recurso?
5. Qual risco aceito ficou e por quê?

## Erros comuns

- instalar scanner e encerrar;
- CORS como autenticação;
- ADMIN com acesso total acidental;
- stack trace;
- actuator/env público;
- alegar rate limiting sem implementar.

## Extensão opcional

Execute ferramenta de análise de dependências disponibilizada pelo seu ecossistema/GitHub e transforme achados confirmados em issue. Não atualize versões no último momento sem teste.

## Conteúdo

“Minha checklist OWASP aplicada ao projeto, sem prometer segurança absoluta”.

## Correção e conferência — só depois da tentativa

Release bloqueia com BOLA, segredo, token adulterado aceito, role manipulável ou stack/SQL público. Ausência de rate limiter pode ser risco conhecido em portfólio, desde que você não diga que o controle existe e que limites básicos estejam aplicados.
