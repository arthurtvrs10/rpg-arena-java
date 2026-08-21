# Manifesto do pacote completo

## Código inicial

- Maven Wrapper, Java 21 e Spring Boot 4.1.0;
- pacote base `io.github.arthurtvrs10.rpgarena`;
- aplicação e teste inicial;
- CI, templates GitHub, licença, segurança e contribuição.

## Análise de requisitos

- 96 requisitos funcionais;
- 28 requisitos não funcionais;
- 110 regras de negócio;
- 19 casos de uso;
- 19 histórias com critérios BDD;
- matriz de permissões e segurança;
- catálogo de erros e glossário;
- stakeholders, personas e jornadas;
- riscos, premissas, restrições e contingências;
- rastreabilidade entre requisito, semana, módulo e teste;
- plano de homologação e ordem de implementação;
- catálogo de eventos.

## Engenharia

- arquitetura alvo e estrutura de pacotes;
- seis diagramas Mermaid;
- dez ADRs aceitos;
- modelo e dicionário de dados;
- ordem de migrations e limites transacionais;
- contrato OpenAPI com 32 paths;
- conteúdo inicial, fórmulas e balanceamento;
- estratégia de testes baseada em riscos;
- coleção Bruno inicial;
- referências oficiais.

## Planejamento e conteúdo

- roadmap de 24 semanas;
- 144 tarefas executáveis;
- planilha única de acompanhamento;
- PDF mestre A4;
- 24 arquivos `.tarefas`;
- plano de 12 episódios e 24 Shorts;
- 12 roteiros individuais;
- metadados e materiais GitHub.

## Exclusões intencionais

O pacote não inclui `.git`, `.idea`, `target`, credenciais, `.env` real, dependências baixadas ou funcionalidades apresentadas falsamente como concluídas.

## Primeiro comando de trabalho

Leia `00-COMECE-AQUI.md`. A primeira tarefa é documental/produto; o primeiro build local usa `./mvnw test` quando a máquina possuir acesso ao Maven Central.
