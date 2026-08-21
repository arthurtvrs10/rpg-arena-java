# Estrutura de pastas

```text
rpg-arena-completo-6-meses/
├── 00-COMECE-AQUI.md
├── README.md
├── README.pt-BR.md
├── MANIFESTO-DO-PACOTE.md
├── VALIDACAO-DO-PACOTE.md
├── pom.xml
├── mvnw / mvnw.cmd / .mvn/
├── src/
│   ├── main/java/io/github/arthurtvrs10/rpgarena/
│   │   └── RpgArenaApplication.java
│   ├── main/resources/application.properties
│   └── test/java/io/github/arthurtvrs10/rpgarena/
├── docs/
│   ├── requisitos/
│   │   ├── 00-INDICE-E-DECISOES-FECHADAS.md
│   │   ├── 01-ESPECIFICACAO-DO-PRODUTO.md
│   │   ├── 02-CATALOGO-REQUISITOS.md
│   │   ├── 03-REGRAS-DE-NEGOCIO.md
│   │   ├── 04-CASOS-DE-USO.md
│   │   ├── 05-HISTORIAS-E-CRITERIOS-BDD.md
│   │   ├── 06-MATRIZ-PERMISSOES-E-SEGURANCA.md
│   │   ├── 07-RISCOS-PREMISSAS-RESTRICOES.md
│   │   ├── 08-MATRIZ-DE-RASTREABILIDADE.md
│   │   ├── 09-PLANO-DE-HOMOLOGACAO.md
│   │   ├── 10-ORDEM-EXATA-DE-IMPLEMENTACAO.md
│   │   ├── 11-GLOSSARIO.md
│   │   ├── 12-CATALOGO-DE-ERROS.md
│   │   ├── 13-MAPA-STATUS-IMPLEMENTACAO.md
│   │   ├── 14-STAKEHOLDERS-PERSONAS-JORNADAS.md
│   │   └── 15-CATALOGO-DE-EVENTOS.md
│   ├── api/openapi.yaml
│   ├── arquitetura/
│   │   ├── ARQUITETURA-ALVO.md
│   │   └── diagramas/*.mmd
│   ├── dados/MODELO-E-DICIONARIO-DE-DADOS.md
│   ├── decisoes/001-...010-*.md
│   ├── game-design/SISTEMAS-E-CONTEUDO-INICIAL.md
│   ├── qualidade/ESTRATEGIA-DE-TESTES.md
│   ├── pt-BR/  (plano intensivo anterior preservado)
│   └── en/     (documentação anterior preservada)
├── planejamento/
│   ├── 00-LEIA-PRIMEIRO.md
│   ├── 01-...09-*.md
│   ├── BACKLOG-MESTRE-6-MESES.xlsx
│   ├── PLANO-MESTRE-RPG-ARENA-6-MESES.pdf
│   ├── tarefas/semana-01.tarefas ... semana-24.tarefas
│   ├── youtube/episodio-01.md ... episodio-12.md
│   └── github-ready/
├── bruno/RPG-Arena/
│   ├── environments/Local.bru
│   ├── 00-health/
│   ├── 01-auth/
│   ├── 02-characters/
│   └── 03-gameplay/
└── .github/
    ├── ISSUE_TEMPLATE/
    ├── workflows/ci.yml
    └── PULL_REQUEST_TEMPLATE.md
```

Durante o desenvolvimento, os módulos de domínio entram dentro de `src/main/java/io/github/arthurtvrs10/rpgarena/` na ordem definida em `docs/requisitos/10-ORDEM-EXATA-DE-IMPLEMENTACAO.md`.
