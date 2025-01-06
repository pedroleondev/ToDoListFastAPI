from pydantic import BaseModel, Field
from datetime import datetime, timezone
from enum import Enum


# Criando o modelo de dados para a tarefa

''' 
id (inteiro, autoincrementado)
titulo (string, obrigatório)
descricao (string, opcional)
estado (string, obrigatório, valores possíveis: "pendente", "em andamento", "concluída")
data_criacao (datetime, gerado automaticamente)
data_atualizacao (datetime, atualizado automaticamente)

'''

# Enum para os estados permitidos  "pendente", "em andamento", "concluída"

class TaskState(str, Enum):
    pending = "pendente"
    in_progress = "em andamento"
    completed = "concluída"

class Task(BaseModel):
    id: int = Field(default=None, alias="_id")
    title: str = Field(...)
    description: str = Field(None, max_length=100)
    state: str = Field(...)
    created_at: datetime = Field(default_factory=datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=datetime.now(timezone.utc))

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True