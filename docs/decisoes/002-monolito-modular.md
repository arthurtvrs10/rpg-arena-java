# ADR-002 — Monólito modular por domínio

**Status:** Aceita — 20/08/2026.

## Decisão

Uma aplicação e um banco, separados internamente em módulos de negócio. Dependências públicas são controladas; ArchUnit protege as fronteiras.

## Alternativas descartadas

Microserviços adicionariam rede, deploy e consistência distribuída sem requisito de escala. Pacotes globais MVC misturariam regras e infraestrutura.

## Consequências

Transações críticas permanecem simples. Extração futura exige métrica/problema real e contrato claro, não moda tecnológica.
