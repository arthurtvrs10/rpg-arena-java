# Contributing

## Workflow

1. Choose or create an issue with acceptance criteria.
2. Create a branch: `feat/123-short-name`, `fix/123-short-name`, or `docs/123-short-name`.
3. Implement the smallest complete change.
4. Run `./mvnw clean verify`.
5. Update documentation, OpenAPI, Bruno, or migrations when required.
6. Open a pull request using the template.
7. Address review feedback and squash merge after all checks pass.

## Definition of done

- Acceptance criteria are demonstrated.
- Relevant tests pass.
- No secret is committed.
- Architecture rules pass.
- Documentation and API collections match the change.
- The PR links its issue.

## Commit examples

- `feat(combat): enforce turn ownership`
- `fix(inventory): prevent duplicate quest reward`
- `test(security): cover cross-account character access`
- `docs(architecture): record optimistic locking decision`
