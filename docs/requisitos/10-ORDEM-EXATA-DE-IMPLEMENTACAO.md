# Ordem exata de implementação

Use este documento para escolher a próxima fatia. A tarefa detalhada permanece em `planejamento/tarefas/semana-XX.tarefas`.

## Regra de início

Antes de codar uma fatia, copie para a issue: requisitos RF/RNF, regras RN, caso de uso, cenários BDD, dados afetados, endpoint, teste e evidência. Se faltar um desses itens, refine antes.

## Mês 1 — núcleo jogável sem banco

### Semana 01

1. Publicar baseline dos requisitos e marcar versão 1.0 da especificação.
2. Criar labels, milestones e board.
3. Importar 144 tarefas ou abrir as 24 issues semanais.
4. Preparar trailer e identidade da série.

**Saída:** escopo fechado e nenhuma funcionalidade anunciada como pronta.

### Semana 02

1. Corrigir pacote base para `io.github.arthurtvrs10.rpgarena`.
2. Criar módulos e `package-info.java` sem dependência circular.
3. Registrar ADRs de stack, monólito modular, UUID/Clock/RandomSource e erros.
4. Fazer o esqueleto compilar e o CI passar.

**Saída:** aplicação inicial e teste de arquitetura.

### Semana 03

1. Criar value objects `CharacterId`, `CharacterName`, `Level`, `Experience`, `Health`, `Mana` e `Stats`.
2. Criar classe publicada e factory de personagem.
3. Criar agregado `Character` com dano, cura e estado.
4. Implementar progressão pura e testes RN-CHR/RN-PRG.

**Saída:** personagem válido em memória.

### Semana 04

1. Criar `Battle`, `CombatantSnapshot`, `Turn`, `BattleAction` e `BattleEvent`.
2. Implementar ataque, defesa, política do inimigo e fim de batalha.
3. Injetar `Clock` e `RandomSource`.
4. Testar uma batalha completa determinística.

**Saída:** tag `v0.1.0`.

## Mês 2 — persistência e jornada

### Semana 05

1. Adicionar PostgreSQL, Flyway e Testcontainers.
2. Criar migrations de conta futura, personagem e conteúdo mínimo.
3. Criar entidades JPA/adapters separados do domínio.
4. Testar round-trip, constraints e banco vazio.

### Semana 06

1. Criar catálogo/versionamento mínimo de item.
2. Implementar pilha, inventário e equipamento.
3. Criar migrations e transação de troca.
4. Testar capacidade, slot, rollback e conflito.

### Semana 07

1. Persistir progressão e habilidades.
2. Implementar múltiplos níveis, cap e desbloqueio.
3. Publicar eventos internos idempotentes.
4. Testar limites e reprocessamento.

### Semana 08

1. Criar definição/versão/instância/objetivos de missão.
2. Implementar aceite, progresso e estados.
3. Implementar contabilização de batalha e recompensa atômica.
4. Testar reinício e repetição.

**Saída:** tag `v0.2.0`.

## Mês 3 — REST e segurança

### Semana 09

1. Implementar Problem Details, validação, traceId e paginação.
2. Criar DTOs/mappers e OpenAPI base.
3. Montar ambientes e requests iniciais no Bruno.

### Semana 10

1. Expor personagem e inventário.
2. Implementar `expectedVersion` e idempotência reutilizável.
3. Testar WebMvc, integração e contratos.

### Semana 11

1. Criar account, cadastro, senha e login.
2. Implementar access JWT, refresh opaco rotativo e logout.
3. Configurar RBAC e status da conta.
4. Cobrir tokens inválidos, reuso e logs.

### Semana 12

1. Aplicar ownership por consulta/caso de uso.
2. Expor missão, batalha e ações.
3. Executar a matriz SEC-T01–12.
4. Automatizar jornada Bruno.

**Saída:** tag `v0.3.0`.

## Mês 4 — mundo, economia e conteúdo

### Semana 13

1. Criar region, location, edge e character location.
2. Implementar viagem transacional/idempotente.
3. Implementar filtro e sorteio de encontros.
4. Expor mapa e viagem.

### Semana 14

1. Criar `Gold`, merchant, stock e ledger.
2. Implementar compra e venda.
3. Testar duas compras do último item e repetição.
4. Liberar consumo em combate se todos os Must estiverem verdes.

### Semana 15

1. Definir schema de nós, escolhas, condições e efeitos.
2. Implementar cadeia, escolha imutável e consequência.
3. Manter instância presa à versão aceita.
4. Testar uma missão com dois finais.

### Semana 16

1. Criar fluxo genérico de draft/validate/publish/archive.
2. Implementar APIs admin por tipo de conteúdo.
3. Registrar auditoria e proteger RBAC.
4. Executar ArchUnit e jornada com conteúdo publicado.

**Saída:** tag `v0.4.0`.

## Mês 5 — qualidade e operação

### Semana 17

1. Fechar mapa risco→teste.
2. Criar builders e corrigir testes frágeis.
3. Configurar JaCoCo por módulo e testes PostgreSQL reutilizáveis.

### Semana 18

1. Criar Dockerfile multi-stage sem root.
2. Criar Compose API + PostgreSQL e `.env.example`.
3. Adicionar liveness/readiness e testar clone limpo.

### Semana 19

1. Conciliar implementação com OpenAPI.
2. Completar coleção e runner Bruno.
3. Atualizar README, diagramas e onboarding.

### Semana 20

1. Implementar logs estruturados e métricas.
2. Medir consultas e corrigir N+1/índices.
3. Executar revisão OWASP e fechar quality gates.

**Saída:** tag `v1.0.0-rc.1`.

## Mês 6 — entrega pública

### Semana 21

Deploy, migration controlada, smoke, backup, restauração, rollback e alertas.

### Semana 22

Licenças, community files, templates, labels, milestones e contribuição externa simulada.

### Semana 23

Bug bash, regressão, carga, revisão final, changelog e upgrade do marco anterior.

### Semana 24

Tag `v1.0.0`, release, case study, demo, GitHub/currículo, candidaturas e episódio final.

## Dependências que não podem ser invertidas

```text
Personagem -> Combate puro -> Persistência
Persistência -> Inventário/Progressão -> Missão
Contrato REST -> Conta/JWT -> Ownership -> Gameplay HTTP
Inventário + Mundo -> Economia
Missão básica + Mundo -> Narrativa versionada
Conteúdo versionado -> API administrativa
Funcionalidades completas -> Docker/observabilidade/carga -> Deploy
```

## Regra de corte

Se uma semana atrasar, finalize o Must da semana antes de iniciar Should da seguinte. Corte, nesta ordem: filtros, efeitos extras, consumo em combate, arquivamento de personagem, endpoints admin menos usados, métricas adicionais. Nunca corte testes de ownership, transações, migrations, idempotência, build ou documentação do fluxo principal.
