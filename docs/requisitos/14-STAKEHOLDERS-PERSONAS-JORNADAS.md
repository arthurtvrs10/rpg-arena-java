# Stakeholders, personas e jornadas

## Stakeholders

| Stakeholder | Interesse | Poder | Necessidade | Estratégia |
|---|---|:---:|---|---|
| Arthur Tavares / mantenedor | aprender, entregar e demonstrar | Alto | escopo executável, evidência e continuidade | decide prioridade e aceita release |
| Jogador da API | experimentar jornada sem perda/abuso | Médio | erros claros, progresso seguro | validar por Bruno e feedback |
| Avaliador técnico/recrutador | verificar competência rapidamente | Médio | setup, código, testes e decisões legíveis | README, demo e case study |
| Contribuidor open source | colaborar sem contexto privado | Baixo/Médio | issues acionáveis e padrões | templates, guide e review |
| Operador/plataforma | manter serviço recuperável | Médio | health, logs, backup e rollback | runbooks e smoke |
| Público da minissérie | aprender acompanhando decisões reais | Baixo | narrativa, demonstração e honestidade | episódio quinzenal e release ligada |

## Personas

### Júlia — jogadora técnica curiosa

- quer criar um personagem e entender a API rapidamente;
- usa Bruno, mas não conhece a implementação;
- espera mensagens acionáveis e nenhuma perda por clique repetido;
- sucesso: completa a jornada principal usando documentação pública.

### Caio — administrador de conteúdo

- cria itens, inimigos, locais e missões;
- precisa validar erros antes de publicar;
- não pode alterar silenciosamente jornadas existentes;
- sucesso: publica uma nova versão e consegue auditar quem fez.

### Renata — avaliadora técnica

- tem 15–30 minutos para avaliar o repositório;
- procura regras, testes, segurança, banco e decisões, não quantidade de pastas;
- sucesso: executa build/demo, encontra evidências e entende trade-offs.

### Diego — contribuidor iniciante

- escolhe uma `good first issue`;
- precisa saber requisito, regra, teste e fluxo de PR;
- sucesso: conclui uma mudança pequena sem pedir instruções privadas.

## Jornada do jogador

| Etapa | Ação | Resposta esperada | Falhas relevantes | Evidência |
|---|---|---|---|---|
| Entrada | cadastro/login | sessão segura | duplicidade/credencial inválida | Bruno auth |
| Criação | personagem/classe | stats, kit e local | limite/nome/classe | teste UC-04 |
| Preparação | inventário/equipamento | stats derivados | item/slot/owner | Bruno inventory |
| Missão | aceitar | instância versionada | requisitos/duplicidade | teste quest |
| Exploração | viajar | custo, posição, encontro | sem conexão/ouro/batalha | Bruno world |
| Combate | agir | eventos, turno e resultado | turno/mana/versão/replay | suíte combat |
| Progressão | receber XP/loot | nível/inventário | capacidade/duplicidade | integração result |
| Economia | comprar/vender | saldos e ledger | estoque/local/corrida | teste concorrente |
| Narrativa | escolher/resgatar | consequência/recompensa | escolha/estado/replay | Bruno quest |
| Comparação | ranking | página pública | paginação/dados privados | contrato ranking |

## Jornada do administrador

1. Autentica como ADMIN por conta provisionada.
2. Cria definição/código ou nova versão em rascunho.
3. Salva payload tipado.
4. Executa validação e recebe todos os erros conhecidos.
5. Corrige somente rascunho.
6. Publica com chave idempotente.
7. Gameplay passa a usar a nova versão em novas instâncias.
8. Instâncias anteriores continuam ligadas à versão antiga.
9. Arquiva quando não deseja novos usos.
10. Consulta auditoria para autoria e instante.

## Jornada do avaliador

1. Lê README e status real.
2. Executa `./mvnw verify` e/ou Docker.
3. Abre diagramas, requisitos e ADRs.
4. Executa jornada Bruno.
5. Inspeciona testes de regra, BOLA, idempotência e concorrência.
6. Confere CI, releases, changelog e deploy.
7. Assiste ao episódio ligado à release.

## Pontos de decisão e feedback

- Toda dúvida nova vira issue; não altera regra em conversa privada.
- Feedback que quebra Must recebe análise de impacto imediata.
- Sugestão de feature entra em backlog e só substitui escopo por decisão do mantenedor.
- Métricas de vídeo não mudam arquitetura; servem para formato editorial.
