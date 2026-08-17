# Dia 7 — Modelo de ameaças e desenho da autenticação

**Data:** 24/08/2026  
**Sprint:** 2 — Segurança, personagem e inventário  
**Tempo núcleo:** 2h  
**Extensão:** 60 min  
**Resultado:** política de identidade e autorização definida antes dos filtros.

## Sprint Goal

Permitir que um jogador autenticado crie e administre apenas seus próprios personagens e itens, com contratos e testes que provem isolamento.

## Antes de começar

- [ ] Execute revisão 1–3–7 da Sprint 1.
- [ ] Leia docs/07-SEGURANCA.md.
- [ ] Crie branch docs/AU-00-threat-model.
- [ ] Não implemente login antes de decidir identidade e ameaças.

## O que você precisa compreender

- Autenticação prova/estabelece identidade; autorização decide ação.
- JWT transporta afirmações assinadas, mas não prova propriedade do recurso.
- BOLA ocorre quando um id válido de outro usuário é aceito.
- Papel e propriedade são controles diferentes.
- Senha exige algoritmo apropriado; criptografia caseira é proibida.
- Resposta e log podem vazar tanto quanto o banco.

## Fontes oficiais

- Spring Security architecture: https://docs.spring.io/spring-security/reference/servlet/architecture.html
- Password storage: https://docs.spring.io/spring-security/reference/features/authentication/password-storage.html
- Authorization: https://docs.spring.io/spring-security/reference/servlet/authorization/index.html
- OWASP API Top 10: https://owasp.org/API-Security/editions/2023/en/0x11-t10/
- OWASP REST Security: https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html

## Exemplo neutro — prontuário

Um médico autenticado não pode abrir qualquer prontuário só porque conhece o id. Papel MEDICO permite a função; vínculo com paciente/unidade define o objeto. Token válido não elimina a verificação.

## Tarefa prática

### 1. Ativos e fronteiras, 20 min

Liste ativos:

- senha/hash;
- token;
- identidade;
- personagem;
- inventário;
- progresso;
- ações administrativas;
- logs.

Desenhe cliente → filtro → Controller → caso de uso → banco. Marque tudo que vem do cliente como não confiável.

### 2. Ameaças, 25 min

Para cada fluxo de auth/personagem/inventário, liste:

- ator;
- ação maliciosa/acidental;
- impacto;
- controle preventivo;
- controle de detecção;
- teste.

Priorize BOLA, credenciais, função administrativa, mass assignment, enumeração, segredo e abuso.

### 3. Decisões JWT, 25 min

Registre:

- subject;
- claims mínimas;
- papéis;
- algoritmo permitido;
- expiração;
- clock;
- emissor/audiência se usar;
- tratamento de expirado/alterado;
- segredo por ambiente;
- limitação de revogação.

Não coloque e-mail, senha, inventário ou permissões dinâmicas desnecessárias.

### 4. Política de autorização, 25 min

Crie matriz de rotas:

- público;
- PLAYER;
- ADMIN;
- propriedade.

Escolha como recurso alheio responde: 404 ou 403. Defina CurrentActor/AuthenticatedAccount como abstração da aplicação.

### 5. Casos de teste, 15 min

Escreva a matriz:

- sem token;
- token válido;
- expirado;
- alterado;
- PLAYER em admin;
- A no próprio personagem;
- A no personagem B;
- body tenta enviar role/accountId.

### 6. Evidência, 10 min

Crie docs/SECURITY.md e ADR-002 atualizado. Faça commit.

## Critérios de aceite

- [ ] identidade efetiva tem fonte única;
- [ ] JWT tem claims mínimos e expiração;
- [ ] política de 404/403 está registrada;
- [ ] papel não substitui propriedade;
- [ ] ameaça possui teste correspondente;
- [ ] logs sensíveis estão proibidos;
- [ ] segredo está fora do Git;
- [ ] risco não implementado está assumido claramente.

## Teste de mesa

Classifique o controle correto:

1. A envia characterId de B.
2. A envia role ADMIN no cadastro.
3. Token muda um caractere.
4. Conta inativa usa token anterior.
5. size=100000 no ranking.
6. erro registra cabeçalho Authorization.

## Evidências

- threat model;
- matriz de autorização;
- política JWT;
- casos de teste;
- commit: docs(security): define authentication and ownership threat model.

## Perguntas de recuperação

1. JWT resolve qual problema e não resolve qual?
2. Onde propriedade é verificada?
3. Por que subject não deveria depender de nome mutável?
4. Qual diferença entre 401 e 403?
5. O que é mass assignment?

## Erros comuns

- endpoint protegido apenas por token;
- confiar em accountId do corpo;
- role vindo do cadastro;
- segredo fixo no YAML;
- logar token;
- criar algoritmo de hash;
- dizer “stateless é sempre mais seguro”.

## Extensão opcional

Faça uma revisão linha a linha do OWASP API1 e API5 e adicione um cenário específico do RPG para cada.

## Conteúdo

“JWT não é autorização: o ataque de trocar o id”.

## Correção e conferência — só depois da tentativa

Uma política coerente usa o subject do token para localizar a conta e compara com o owner persistido. characterId identifica o alvo, não o dono. Campos role e accountId não aparecem em DTO público. Token alterado ou expirado produz 401; papel insuficiente produz 403; recurso privado alheio pode produzir 404 se essa for sua política.
