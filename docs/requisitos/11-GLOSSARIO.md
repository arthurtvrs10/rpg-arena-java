# Glossário

| Termo | Definição |
|---|---|
| Account | identidade autenticável; proprietária dos personagens |
| Player | papel padrão e ator que controla progresso próprio |
| Admin | papel que gerencia e publica conteúdo; não controla personagem alheio |
| Character | agregado que representa personagem, estado, stats, nível, XP e ouro |
| Base stat | atributo próprio do personagem antes de equipamento |
| Derived stat | resultado calculado de base, nível, equipamento e efeitos |
| Character class | conteúdo versionado que define atributos e crescimento iniciais |
| Skill | conteúdo versionado usado em batalha, com custo, cooldown e efeito |
| Cooldown | quantidade de turnos próprios antes de reutilizar habilidade |
| Item definition/version | catálogo e versão imutável das regras de um item |
| Inventory entry | posse/pilha de uma versão de item por personagem |
| Equipment | associação entre personagem, slot e entrada equipada |
| Loot | recompensa de item sorteada por tabela versionada |
| Battle | agregado de combate PvE com snapshot, turno, eventos e versão |
| Combatant snapshot | cópia dos dados usados na batalha, imune a mudanças posteriores de catálogo |
| Battle event | registro imutável e ordenado de algo ocorrido no combate |
| Turn | direito atual de agir e unidade que controla cooldown/efeitos |
| Quest definition/version | catálogo e versão imutável da missão publicada |
| Quest instance | jornada concreta de um personagem ligada a uma versão |
| Objective | condição mensurável necessária à missão |
| Narrative node | ponto da história que apresenta texto/opções |
| Choice | decisão imutável tomada em um nó |
| Reward claim | comando que aplica recompensa concluída uma única vez |
| Region | agrupamento de locais |
| Location | nó publicado do grafo do mundo |
| Location edge | conexão direcionada entre origem e destino |
| Encounter | resultado elegível de viagem que pode iniciar batalha |
| Merchant | conteúdo publicado que oferece estoque em um local |
| Merchant stock | quantidade/preço mutáveis de item do comerciante |
| Ledger/economy transaction | registro imutável de compra, venda ou ajuste |
| Content draft | versão editável ainda invisível ao gameplay |
| Published content | versão validada, imutável e disponível para novas instâncias |
| Archived content | versão preservada, mas indisponível para novas instâncias |
| Ownership | vínculo entre identidade autenticada e recurso privado |
| BOLA/IDOR | acesso indevido obtido ao trocar identificador de recurso |
| RBAC | autorização baseada em papéis |
| Access token | JWT curto apresentado em cada requisição privada |
| Refresh token | segredo opaco de uso único para renovar a sessão |
| Idempotency-Key | chave que faz repetição do mesmo comando devolver o mesmo resultado |
| Optimistic locking | detecção de atualização perdida por coluna de versão |
| Problem Details | formato padronizado de erro HTTP |
| TraceId | identificador correlacionável entre resposta e logs |
| Domain event | fato de negócio imutável emitido pelo domínio |
| Projection | modelo de leitura derivado, como ranking |
| Migration | mudança incremental, versionada e imutável do schema |
| Seed | dados fictícios/controlados para ambiente local/demonstração |
| Smoke test | validação curta de que a versão implantada responde e executa o mínimo |
| Fatia vertical | entrega que cruza contrato, caso, regra, persistência e teste |
| DoR | condições para uma história entrar em desenvolvimento |
| DoD | condições para uma história ser considerada concluída |
