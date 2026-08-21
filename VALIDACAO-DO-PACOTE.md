# Validação do pacote

Data: 20/08/2026.

## Aprovado

- `pom.xml` bem-formado;
- `bruno.json` válido;
- OpenAPI YAML válido, com 32 paths e referências internas resolvidas;
- links internos dos documentos principais resolvidos;
- 24 arquivos semanais e 12 roteiros de episódios presentes;
- 96 RF, 28 RNF, 110 regras, 19 casos e 19 histórias identificados;
- nenhum arquivo vazio;
- nenhum `.git`, `.idea`, `target` ou segredo incluído;
- pacote base Java alinhado a `io.github.arthurtvrs10.rpgarena`;
- Maven Wrapper marcado como executável.

## Validação local pendente

O ambiente de montagem não conseguiu acessar o Maven Central por restrição de DNS, portanto não baixou o parent/dependências para executar o build. A estrutura Maven foi validada, e os módulos de teste usados estão documentados pelo Spring Boot 4.1.

Execute em uma máquina com internet:

```bash
./mvnw test
```

No Windows PowerShell:

```powershell
.\mvnw.cmd test
```

Quando PostgreSQL/Flyway/Testcontainers forem adicionados nas semanas planejadas, o comando de gate passa a ser `./mvnw clean verify`.
