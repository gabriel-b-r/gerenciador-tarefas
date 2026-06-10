# API To-Do Profissional
API REST para gerenciamento de tarefas (Tasks), permitindo operações completas de CRUD.

# Problemas resolvidos
Permitir que aplicações web, mobile ou sistemas externos possam:

- Criar tarefas
- Consultar tarefas
- Atualizar tarefas
- Remover tarefas

através de uma interface REST padronizada.

# Principais Funcionalidades
Tasks:

- Criar tarefa
- Listar tarefas
- Buscar tarefa por ID
- Atualizar tarefa completa
- Atualizar tarefa parcialmente
- Remover tarefa

# Arquitetura da Aplicação
Arquitetura em camadas (Layered Architecture)

Separação entre:
Routes -> Services -> Models -> Database

## Routes

Responsáveis por:
- Receber requisições HTTP
- Validar entrada básica
- Chamar Services
- Retornar Responses

## Services

Responsáveis por:

- Regras de negócio
- Manipulação de entidades
- Operações de banco

## Models

Responsável por:
- Representação das entidades do sistema (Tabelas).

## Database

Responsável por:
- Persistência dos dados.

# Tecnologias Utilizadas
- *Python* - Linguagem principal da aplicação: Implementa a lógica da API.
- *Flask* - Framework web: Rotas, requests, responses, blueprints.
- *SQLAlchemy* - ORM (Object Relational Mapper): Mapeia objetos Python para tabelas SQL.
- *PostgreSQL* - Banco de dados relacional: Persistência das Tasks.
- *Docker* - Containerização: Executa a API em ambiente isolado.
- *Docker Compose* - Orquestração: Executa API e PostgreSQL simultaneamente.
- *python-dotenv* - Gerenciamento de variáveis de ambiente: Carrega informações do arquivo .env.
- *psycopg2-binary* - Driver PostgreSQL: Permite a comunicação entre Python e PostgreSQL

# Estrutura de Diretórios
├── project/

├── app/ - Núcleo da aplicação.

│ ├── routes/ - Contém os endpoints da API.

│ ├── services/ - Regras de negócio.

│ ├── models/ - Entidades do sistema.

│ ├── extensions/ - Objetos compartilhados.

│ ├── __init__.py - Inicialização e estrutura básica do Flask.

├── config/ - Configurações da aplicação.

├── .env - Variáveis de ambiente.

├── .env.example - Exemplo de variáveis do ambiente para utilização local.

├── Dockerfile - Conteinerização da aplicação.

├── docker-compose.yml - Orquestração de containers.

├── requirements.txt - Requisitos para funcionamento da aplicação.

└── run.py - Ponto de entrada da aplicação.

# Configuração do Ambiente

## Pré-Requisitos
- Python: 