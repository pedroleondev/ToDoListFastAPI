# ToDoListFastAPI

## Descrição

Este projeto é uma API de Gerenciamento de Tarefas construída com FastAPI. Ele permite a criação, leitura, atualização e exclusão de tarefas, além de autenticação de usuários.

## Estrutura do Projeto

- `app/main.py`: Inicializa o servidor FastAPI e registra as rotas.
- `app/routers/auth.py`: Contém as rotas de autenticação, incluindo a criação de usuários e a geração de tokens.
- `app/routers/tasks.py`: Contém as rotas para operações CRUD relacionadas às tarefas.
- `app/models.py`: Define os modelos de dados para usuários e tarefas.
- `app/database.py`: Configura a conexão com o banco de dados SQLite.
- `app/crud.py`: Contém as funções CRUD para interagir com o banco de dados.
- `app/dependencies.py`: Centraliza as dependências usadas em várias partes do projeto.
- `tests/test_api.py`: Contém os testes para todos os endpoints da API.
- `alembic/versions/`: Contém os scripts de migração do banco de dados.

## Configuração do Ambiente

1. Clone o repositório:
   ```bash
   git clone https://github.com/pedroleondev/ToDoListFastAPI.git
   cd ToDoListFastAPI
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   conda create -n env_todolistfastapi python=3.10 -y
   conda activate <nome_do_ambiente>
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Configuração do Banco de Dados

1. Aplique as migrações do banco de dados:
   ```bash
   alembic upgrade head
   ```

## Executando a Aplicação

1. Inicie o servidor FastAPI:
   ```bash
   uvicorn app.main:app --reload
   ```

2. Acesse a documentação interativa da API em `http://localhost:8000/docs`.

## Endpoints

### Autenticação

- **Criar Usuário**
  - **POST** `/auth/`
  - Corpo da requisição:
    ```json
    {
      "usuario": "seu_usuario",
      "senha": "sua_senha"
    }
    ```

- **Gerar Token**
  - **POST** `/auth/token`
  - Corpo da requisição (form-data):
    - `username`: seu_usuario
    - `password`: sua_senha

- **Obter Usuário Atual**
  - **GET** `/user`
  - Cabeçalho da requisição:
    - `Authorization`: `Bearer <seu_token>`

### Tarefas

- **Criar Tarefa**
  - **POST** `/tasks/`
  - Corpo da requisição:
    ```json
    {
      "titulo": "Título da Tarefa",
      "descricao": "Descrição da Tarefa",
      "estado": "pendente"
    }
    ```

- **Listar Tarefas**
  - **GET** `/tasks/`

- **Filtrar Tarefas por Estado**
  - **GET** `/tasks/filter?estado=pendente`

- **Buscar Tarefa por ID**
  - **GET** `/tasks/{task_id}`

- **Atualizar Tarefa**
  - **PUT** `/tasks/{task_id}`
  - Corpo da requisição:
    ```json
    {
      "titulo": "Título Atualizado",
      "descricao": "Descrição Atualizada",
      "estado": "em andamento"
    }
    ```

- **Deletar Tarefa**
  - **DELETE** `/tasks/{task_id}`

## Executando os Testes

1. Execute os testes usando o pytest:
   ```bash
   pytest tests/test_api.py
   ```

## Docker

1. Construa a imagem Docker:
   ```bash
   docker build -t todolistfastapi-app .
   ```

2. Execute o container Docker:
   ```bash
   docker run -p 8000:8000 todolistfastapi-app
   ```
3. Use a imagem disponível no Docker Hub:
```bash
   docker push pedroleonpython/todolistfastapi-app:0.3
```
## Contribuição

Sinta-se à vontade para contribuir com este projeto. Abra uma issue ou envie um pull request com melhorias e correções.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
