# Dia 8 — Cadastro, login e JWT

**Data:** 25/08/2026  
**Sprint:** 2  
**Tempo núcleo:** 2h  
**Extensão:** 90 min  
**Resultado:** identidade autenticada com senha protegida, token validado e erros seguros.

## Antes de começar

- [ ] A matriz de segurança do Dia 7 está concluída.
- [ ] Escolha e documente a biblioteca JWT compatível com sua versão.
- [ ] Crie branch feat/AU-01-register-login.
- [ ] Prepare dois usuários de teste, sem dados reais.

## O que você precisa compreender

- PasswordEncoder recebe senha bruta apenas no limite necessário.
- E-mail deve ser normalizado de forma consistente antes da unicidade.
- Token deve ser emitido por componente isolado e testável.
- Filtro autentica; caso de uso continua responsável por propriedade.
- Erro de login não deve permitir enumeração.
- Configuração de segurança deve declarar rotas e ordem com clareza.

## Fontes oficiais

- Spring Security password storage: https://docs.spring.io/spring-security/reference/features/authentication/password-storage.html
- Authentication password flow: https://docs.spring.io/spring-security/reference/servlet/authentication/passwords/index.html
- JWT: https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/jwt.html
- Authorization requests: https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html

## Exemplo neutro — portal de cursos

Cadastro transforma senha, salva papel STUDENT definido no servidor e devolve perfil público. Login válido emite token; inválido responde igual para e-mail inexistente e senha errada. A área /admin exige papel separado.

## Tarefa prática

### 1. Contratos, 15 min

Defina DTOs distintos:

- RegisterRequest;
- RegisterResponse;
- LoginRequest;
- TokenResponse.

Liste campos proibidos nas respostas: password, passwordHash, token secret, role arbitrária.

### 2. Cadastro, 30 min

Implemente:

- validação de formato;
- trim/normalização de e-mail;
- verificação de conflito;
- hash via PasswordEncoder;
- papel PLAYER no servidor;
- conta ACTIVE;
- persistência;
- resposta segura.

Trate corrida de unicidade também pela constraint do banco.

### 3. Login e emissão, 30 min

Implemente comparação segura, estado da conta e emissão. Separe TokenIssuer para testar relógio/expiração. Não registre credenciais.

### 4. Filtro e rotas, 25 min

Configure:

- /auth e health conforme política pública;
- /admin para ADMIN;
- demais APIs para autenticado;
- sessão conforme escolha;
- CSRF conforme tipo de cliente e mecanismo, registrando decisão;
- tratamento 401/403 padronizado.

Não desabilite controles sem explicar o contexto.

### 5. Testes, 25 min

Automatize:

- cadastro válido;
- e-mail inválido;
- duplicado;
- hash não igual à senha;
- login válido;
- senha errada;
- token expirado/alterado;
- rota protegida;
- PLAYER em admin.

### 6. Bruno e evidência, 15 min

Crie pasta 01-auth, salve token em variável de ambiente local e assertions. Nunca versione token real.

## Critérios de aceite

- [ ] senha bruta não é persistida ou logada;
- [ ] e-mail normalizado é único;
- [ ] role vem do servidor;
- [ ] login inválido não enumera;
- [ ] token expira e assinatura é validada;
- [ ] rotas públicas são allowlist;
- [ ] 401 e 403 têm formato padronizado;
- [ ] Bruno possui cenários válidos e inválidos.

## Testes obrigatórios

- cadastrar “A@EXEMPLO.COM” e depois “a@exemplo.com”;
- procurar senha literal no banco e log;
- alterar payload sem nova assinatura;
- expirar usando clock controlado ou token de teste;
- enviar role ADMIN no cadastro;
- acessar /admin como PLAYER.

## Evidências

- diff de security config;
- testes;
- coleção Bruno;
- resposta sem hash;
- commit: feat(auth): add secure registration login and token validation.

## Perguntas de recuperação

1. Por que constraint ainda é necessária após existsByEmail?
2. Qual componente conhece o segredo?
3. Por que token não deve levar inventário?
4. O que 401 significa?
5. Como testou expiração sem esperar?

## Erros comuns

- Base64 como proteção de senha;
- role no request;
- catch genérico devolvendo stack;
- filtro buscando recurso de negócio;
- token infinito;
- secret curto no Git;
- teste que só verifica “token não nulo”.

## Extensão opcional

Documente estratégia futura de refresh/revogação sem implementar. Explique o limite do MVP.

## Conteúdo

“O que realmente acontece entre login e uma rota protegida”.

## Correção e conferência — só depois da tentativa

O fluxo esperado é: DTO valida forma → aplicação normaliza → constraint garante unicidade → PasswordEncoder gera hash → TokenIssuer emite claims mínimas → filtro valida → CurrentActor expõe subject. Propriedade ainda não está resolvida até consultar o recurso.

Se o cadastro aceita role, o filtro registra Authorization ou a senha aparece em qualquer resposta, a história falhou mesmo que o login funcione.
