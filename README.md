# :clipboard: API To-Do Profissional (v1)
API REST para gerenciamento de tarefas (Tasks), permitindo operações completas de CRUD.

(gif resultado)

---
## Visão Geral

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

├── Dockerfile - Conteinerização da aplicação.

├── docker-compose.yml - Orquestração de containers.

├── requirements.txt - Requisitos para funcionamento da aplicação.

└── run.py - Ponto de entrada da aplicação.

---


## :rocket: Instalação e Execução

### Pré-Requisitos
Para testar essa aplicação, você deverá possuir o [Docker](https://www.docker.com/) instalado e algum aplicativo para testes de API como o [Postman](https://www.postman.com/).

### Execução
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

A partir desse momento o projeto estará funcionando, utilize o próximo tópico para fazer requisições e utilizá-lo.

### Utilização


### Finalização
1. Pressione as teclas **Ctrl + C** para finalizar a execução.

2. Utilize o comando abaixo para finalizar a execução do container.
```
docker compose down
```

---

## Endpoints e Métodos Disponíveis
### Post
### Get
### Get by id
### Delete
### Put
### Patch

## Modelos de Dados

## Tratamento de Erros

## Versionamento e Passos Futuros

## Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.