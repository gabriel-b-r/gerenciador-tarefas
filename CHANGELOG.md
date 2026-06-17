# :scroll: Changelog
Todas as mudanças notáveis neste projeto serão documentadas aqui.

O formato segue as recomendações do [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/)  
e este projeto adota [Semantic Versioning](https://semver.org/lang/pt-BR/).

---

## [1.0.0] - 2026-06-12
### Added
- CRUD completo de tarefas (`/api/v1/tasks`):
  - Criar tarefa (`POST /tasks`)
  - Listar tarefas (`GET /tasks`)
  - Buscar tarefa por ID (`GET /tasks/{id}`)
  - Atualizar tarefa completa (`PUT /tasks/{id}`)
  - Atualizar parcialmente (`PATCH /tasks/{id}`)
  - Remover tarefa (`DELETE /tasks/{id}`)
- Estrutura de diretórios organizada em camadas (Routes, Services, Models, Database).
- Configuração com Docker e Docker Compose.
- Documentação inicial com endpoints, exemplos de requisição e resposta.
- Tratamento básico de erros (400, 404, 500).

---

## [Futuro]
### Planned
- Endpoint de usuários e sistema de login.
- Autenticação JWT para rotas protegidas.
- Paginação e filtros de tarefas.
- Implementação de rate limits.