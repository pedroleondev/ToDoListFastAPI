from datetime import datetime
#from pydantic import BaseModel, Field (alteração para o SQLModel, que é compatível com Pydantic)
from sqlmodel import SQLModel, Field
from typing import Optional


# Modelo de dados para a tarefa
# id (inteiro, autoincrementado)
# titulo (string, obrigatório)
# descricao (string, opcional)
# estado (string, obrigatório, valores possíveis: "pendente", "em andamento", "concluída")
# data_criacao (datetime, gerado automaticamente)
# data_atualizacao (datetime, atualizado automaticamente)

# class Task(BaseModel):
#     id: int
#     titulo: str = Field(..., example="Minha tarefa")
#     descricao: Optional[str] = Field(None, example="Descrição opcional")
#     estado: str = Field(..., example="pendente", pattern="^(pendente|em andamento|concluída)$")
#     data_criacao: datetime
#     data_atualizacao: datetime

# criar o objeto Task para armazenar os dados das tarefas
class Task(SQLModel, table=True):
    __tablename__ = "tarefas"  # Nome da tabela no banco de dados
    
    id: Optional[int] = Field(default=None, primary_key=True)
    titulo: str = Field(...)
    descricao: Optional[str] = Field(None)
    estado: str = Field(..., regex="^(pendente|em andamento|concluída)$")
    data_criacao: datetime = Field(default_factory=datetime.now)
    data_atualizacao: datetime = Field(default_factory=datetime.now)

# criar o objeto users para armazenar os dados de usuários e fazer autenticação
class User(SQLModel, table=True):
    __tablename__ = "usuarios"  # Nome da tabela no banco de dados
    
    id: Optional[int] = Field(default=None, primary_key=True)
    usuario: str = Field(...)
    senha: str = Field(...)
    senha_criptografada: str = Field(...)
    data_criacao: datetime = Field(default_factory=datetime.now)
    data_atualizacao: datetime = Field(default_factory=datetime.now)

# criar o objeto Criar Requisição do usuário para armazenar os dados de requisição

class CreateUserRequest(SQLModel):
    usuario: str = Field(...)
    senha: str = Field(...)

# criar o objeto Token para armazenar os dados do token de autenticação
class Token(SQLModel):
    access_token: str
    token_type: str