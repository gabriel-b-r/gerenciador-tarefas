# :clipboard: API To-Do Profissional (v1)
API REST para gerenciamento de tarefas (Tasks), permitindo operações completas de CRUD.

(gif resultado)

---
## :mag_right:  Visão Geral

### :toolbox: Principais Funcionalidades
Tasks:

- Criar tarefa
- Listar tarefas
- Buscar tarefa por ID
- Atualizar tarefa completa
- Atualizar tarefa parcialmente
- Remover tarefa
  
---

### :dart: Problemas resolvidos
Permitir que aplicações web, mobile ou sistemas externos possam:

- Criar tarefas
- Consultar tarefas
- Atualizar tarefas
- Remover tarefas

através de uma interface REST padronizada.

---

### :hammer: Tecnologias Utilizadas
- **Python** - Linguagem principal.
- **Flask** - Framework web.
- **SQLAlchemy** - ORM (Object Relational Mapper).
- **PostgreSQL** - Banco de dados relacional.
- **Docker** - Containerização.
- **Docker Compose** - Orquestração.
- **python-dotenv** - Gerenciamento de variáveis de ambiente.
- **psycopg2-binary** - Driver PostgreSQL.

---

### :triangular_ruler: Arquitetura da Aplicação
Arquitetura em camadas (Layered Architecture)

Separação entre:
**Routes -> Services -> Models -> Database**

**Routes**
- Recebe requisições HTTP
- Valida entrada básica
- Chama Services
- Retorna Responses

**Services**
- Regras de negócio
- Manipulação de entidades
- Operações de banco

**Models**
- Representação das entidades do sistema (Tabelas).

**Database**
- Persistência dos dados.
  
---

### :file_folder: Estrutura de Diretórios
├── project/

├── app/ - Núcleo da aplicação.

│ ├── routes/ - Endpoints da API.

│ ├── services/ - Regras de negócio.

│ ├── models/ - Entidades do sistema.

│ ├── extensions/ - Objetos compartilhados.

│ ├── init.py - Inicialização e estrutura básica do Flask.

├── config/ - Configurações da aplicação.

├── .env - Variáveis de ambiente.

├── .env.example - Exemplo de variáveis do ambiente para utilização local.

├── Dockerfile - Containerização da aplicação.

├── docker-compose.yml - Orquestração de containers.

├── requirements.txt - Requisitos para funcionamento da aplicação.

└── run.py - Ponto de entrada da aplicação.

---


## :rocket: Primeiros Passos

### :pencil: Pré-Requisitos
Para testar essa aplicação, você deverá possuir o [Docker](https://www.docker.com/) instalado e algum aplicativo para testes de API como o [Postman](https://www.postman.com/).

### :up: Execução
1. **Clonar o Repositório**
   ```
   git clone https://github.com/gabriel-b-r/gerenciador-tarefas.git
   ```
   - **Importante:** Antes de prosseguir, confira se está na pasta "gerenciador-tarefas". Caso não esteja, utilize o seguinte comando:
        ```
        cd gerenciador-tarefas
        ```
  
2. **Criar um .env a partir do exemplo**
   - **Windows:**
        ```
        copy .env.example .env
        ```

   - **Linux/MacOS:**
        ```
        cp .env.example .env
        ```
3. **Criar o container Docker do projeto**
```
docker compose build
```

4. **Executar o container**
```
docker compose up
```

A partir desse momento a API estará disponível em http://localhost:5000/api/v1/tasks, utilize o tópico [Endpoints e Métodos Disponíveis](#endpoints-e-metodos-disponíveis) para fazer requisições e utilizá-lo.


### :stop_sign: Finalização
1. Pressione as teclas **Ctrl + C** para finalizar a execução.

2. Utilize o comando abaixo para parar e remover o container.
```
docker compose down
```

---

## :key: Autenticação
Atualmente a API é pública.

Passo futuro: implementação de autenticação JWT para endpoints protegidos.

---

## :globe_with_meridians: Endpoints e Métodos Disponíveis
A seguir, serão descritos os endpoints e métodos que você pode utilizar para interagir com as tarefas.

### Tasks
Este endpoint tem a finalidade de criar, consultar, atualizar e deletar tarefas no banco de dados.

Prefixo global:
```
/api/v1/tasks
```

---

**POST**

Criar uma nova tarefa.

Endpoint:
```
POST /api/v1/tasks
```

Request:
```
{
  "title": "Estudar Flask",
  "description": "Aprender a construir API RESTful com Flask",
  "priority": "ALTA",
  "status": "PENDENTE"
}
```

Response:
```
{
    "success": true,
    "data": {
          "id": 1,
          "title": "Estudar Flask",
          "description": "Aprender a construir API RESTful com Flask",
          "priority": "ALTA",
          "status": "PENDENTE"
    }
}
```

Códigos de retorno:
```
201	Criado
400	Dados inválidos
500	Erro interno
```

---

**GET**

Retornar todas as tarefas.

Endpoint:
```
GET /api/v1/tasks
```

Response:
```
{
     "success": true,
     "count": 1,
     "data": [
          {
               "id": 1,
               "title": "Estudar Flask",
               "description": "Aprender a construir API RESTful com Flask",
               "priority": "ALTA",
               "status": "PENDENTE"
          }
     ]
}
```
Códigos de retorno:
```
200 Ok
500 Erro interno
```

---

**GET BY ID**

Retornar uma tarefa específica.

Endpoint:
```
GET /api/v1/tasks/<id>
```

Exemplo:
```
GET /api/v1/tasks/1
```

Response:
```
{
    "success": true,
    "data": {
          "id": 1,
          "title": "Estudar Flask",
          "description": "Aprender a construir API RESTful com Flask",
          "priority": "ALTA",
          "status": "PENDENTE"
    }
}
```

Códigos de retorno:
```
200 Ok
404 Não encontrado
500 Erro interno
```

---

**PUT**

Substituir completamente os dados da tarefa.

Endpoint:
```
PUT /api/v1/tasks/<id>
```

Exemplo:
```
PUT /api/v1/tasks/1
```

Request:
```
{
    "title": "Aprender PostgreSQL",
    "description": "Aprendendo PostgreSQL para persistência dos dados",
    "priority": "ALTA",
    "status": "PENDENTE"
}
```

Response:
```
{
    "success": true,
    "data": {
          "id": 1,
          "title": "Aprender PostgreSQL",
          "description": "Aprendendo PostgreSQL para persistência dos dados",
          "priority": "ALTA",
          "status": "PENDENTE"
    }
}

```

Códigos de retorno:
```
200 Ok
404 Não encontrado
500 Erro interno
```

---

**PATCH**

Atualizar apenas campos enviados.

Endpoint:
```
PATCH /api/v1/tasks/<id>
```

Exemplo:
```
PATCH /api/v1/tasks/1
```

Request:
```
{
    "status": "FINALIZADO"
}
```

Response:
```
{
    "success": true,
    "data": {
          "id": 1,
          "title": "Aprender PostgreSQL",
          "description": "Aprendendo PostgreSQL para persistência dos dados",
          "priority": "ALTA",
          "status": "FINALIZADO"
    }
}
```

Códigos de retorno:
```
200 Ok
404 Não encontrado
500 Erro interno
```

---

**DELETE**

Apaga uma tarefa do banco de dados.

Endpoint:

```
DELETE /api/v1/tasks/<id>
```

Exemplo:
```
DELETE /api/v1/tasks/1
```

Response:
```
204 No content
```

Códigos de retorno:
```
204 Sem conteúdo
404 Não encontrado
500 Erro interno
```

---

## :warning: Tratamento de Erros
Lista de erros comuns:
- 400 Bad Request → Parâmetros inválidos
- 404 Not Found → Recurso não encontrado
- 500 Internal Server Error → Erro inesperado


---
## :computer: Exemplos de Consumo
- cURL
  ```
     curl -X GET http://localhost:5000/api/v1/tasks
  ```
- Python (requests)
  ```
     import requests
     r = requests.get("http://localhost:5000/api/v1/tasks")
     print(r.json())
  ```
- JavaScript (fetch)
  ```
  fetch("http://localhost:5000/api/v1/tasks")
  .then(res => res.json())
  .then(data => console.log(data))
  ```

---

## :bar_chart: Limites e Restrições
- Payload máximo: 2MB
- Rate limit: não implementado (planejado para versões futuras)

---

## :seedling: Versionamento e Passos Futuros
- Versão atual: v1
- Passos Futuros:
  - Endpoint Users e login
  - Autenticação JWT
  - Paginação e Filtro de tarefas
  
---

## :scroll: Licença
Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## :memo: Changelog
Consulte o arquivo [CHANGELOG](CHANGELOG.md) para acompanhar alterações entre versões.