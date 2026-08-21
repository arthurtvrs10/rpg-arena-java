# Coleção Bruno

O conteúdo atual é um esqueleto executável que deve evoluir junto com `docs/api/openapi.yaml`.

## Uso

1. Abra a pasta `bruno/RPG-Arena` no Bruno.
2. Selecione o ambiente `Local`.
3. Ajuste e-mail/nome fictícios se já existirem.
4. Execute Health, Register, Login e Create Character nessa ordem.
5. Implemente novos requests na mesma ordem do OpenAPI.

## Variáveis geradas

`accessToken`, `refreshToken`, `characterId`, `characterVersion`, `battleId` e `battleVersion` são preenchidas por scripts pós-resposta. Nunca commite valores reais.

## Estrutura final esperada

```text
00-health/
01-auth/
02-characters/
03-inventory/
04-quests/
05-world/
06-battles/
07-economy/
08-ranking/
09-admin/
10-security-negative/
11-regression/
```

Cada endpoint deve ter cenário feliz e, em pasta de regressão/segurança, as falhas críticas correspondentes.
