# Segurança e modelo de ameaças

## Objetivo

Proteger identidade, propriedade e integridade do progresso. Segurança não é apenas “colocar JWT”; cada caso de uso precisa decidir quem age, sobre qual recurso e em qual estado.

## Fronteiras de confiança

~~~mermaid
flowchart TD
    U["Cliente não confiável"] --> F["Filtros de segurança"]
    F --> C["Controller e validação"]
    C --> A["Caso de uso e autorização"]
    A --> D["Domínio"]
    A --> P["Persistência"]
~~~

Tudo enviado pelo cliente é não confiável, inclusive id, papel, dano, nível, preço, dono, timestamp e versão.

## Fluxo de autenticação

1. Cadastro valida e normaliza e-mail.
2. Senha é transformada por PasswordEncoder adequado.
3. Login compara por mecanismo seguro.
4. Token inclui subject estável, papel mínimo, emissão e expiração.
5. Filtro valida assinatura, expiração e estrutura.
6. Identidade é colocada no contexto.
7. Caso de uso consulta recurso e verifica propriedade.
8. Logs recebem traceId, nunca token.

## Matriz de autorização

| Operação | Público | PLAYER | ADMIN | Propriedade |
|---|---:|---:|---:|---|
| Registrar/login | Sim | Sim | Sim | Não |
| Consultar ranking | Sim | Sim | Sim | Não |
| Consultar perfil próprio | Não | Sim | Sim | Próprio |
| Criar/listar personagem | Não | Sim | Opcional | Próprio |
| Alterar inventário | Não | Sim | Não por padrão | Próprio |
| Iniciar missão/batalha | Não | Sim | Não por padrão | Próprio |
| Manter catálogo | Não | Não | Sim | N/A |

ADMIN não deve automaticamente “virar o jogador” sem requisito e auditoria.

## Ameaças prioritárias

| Ameaça | Exemplo | Controle | Teste |
|---|---|---|---|
| BOLA | Trocar characterId na URL | Buscar por id e owner ou verificar owner no caso de uso | Jogador A tenta recurso de B |
| Autenticação quebrada | Token expirado/forjado | Validação de assinatura, expiração e algoritmo permitido | Token ausente, expirado, alterado |
| Propriedade manipulada | Enviar accountId no JSON | Ignorar/remover campo; usar subject | Corpo com id de outra conta |
| Mass assignment | Enviar level, role ou damage | DTO allowlist e cálculo no servidor | Campos proibidos |
| Consumo irrestrito | size enorme ou spam de login | Limites, paginação e proteção de abuso | size acima do máximo |
| Função administrativa exposta | PLAYER chama /admin | Regras por rota e método | 403 |
| SSRF | URL enviada pelo cliente | Não existe chamada remota no MVP | Manter fora do escopo |
| Misconfiguration | Actuator/stack trace aberto | Expor mínimo, perfil e erros seguros | Verificar endpoints |
| Inventário impróprio | Dependência vulnerável | Atualizações deliberadas e scanner | Pipeline |
| Logs sensíveis | Authorization em log | Redação e revisão | Buscar segredos no log |

## Política BOLA

Escolha uma destas respostas e mantenha consistência:

- 404 para recurso alheio, reduzindo confirmação de existência; ou
- 403 após localizar, quando o produto precisa distinguir.

Para portfólio, 404 pode ser defendida em recursos privados. Documente a escolha e teste que dados do recurso não vazam.

## Senhas e segredos

- não criar algoritmo próprio;
- usar PasswordEncoder suportado;
- não registrar senha, hash ou token;
- segredo JWT vem de variável de ambiente;
- .env real fica fora do Git;
- .env.example contém nomes e exemplos falsos;
- rotação e invalidação avançadas ficam como risco conhecido se não implementadas.

## JWT: decisões mínimas

- algoritmo permitido fixo;
- segredo/tamanho adequado ao algoritmo;
- subject não é e-mail mutável, se possível;
- expiração curta e explícita;
- papéis vindos do servidor;
- clock testável;
- rejeitar token sem campos obrigatórios;
- não colocar dados sensíveis no payload.

## Validação e erros

Validação reduz superfície, mas não substitui autorização. Mensagens públicas não revelam bibliotecas, SQL, tabela, stack ou existência de conta. TraceId permite correlacionar investigação interna.

## Abuso

No MVP, documente limites:

- máximo de tamanho de página;
- limite de tamanho de corpo;
- tentativas repetidas de login;
- criação de batalha/missão;
- chaves de idempotência;
- timeouts.

Se não houver rate limiter implementado, não finja. Registre como risco e demonstre controles que existem.

## Checklist antes do release

- [ ] jogador A não acessa personagem, inventário, missão ou batalha de B;
- [ ] token ausente, expirado e alterado falham;
- [ ] PLAYER não acessa administração;
- [ ] cliente não define role, level, XP, damage ou owner;
- [ ] erro 500 não expõe detalhes;
- [ ] logs não contêm Authorization, senha ou hash;
- [ ] paginação tem máximo;
- [ ] segredo não está no repositório ou histórico;
- [ ] dependências e imagem base foram revisadas;
- [ ] README explica configuração sem publicar segredo.

## Referência de risco

O mapa de riscos deve ser revisado contra o OWASP API Security Top 10, mas somente controles presentes no sistema podem ser declarados como implementados.
