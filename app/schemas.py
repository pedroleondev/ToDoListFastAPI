from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Esquema para criação de uma nova tarefa
class TarefaCreate(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    estado: str

# Esquema para resposta de uma tarefa
class TarefaResponse(BaseModel):
    id: int
    titulo: str
    descricao: Optional[str] = None
    estado: str
    data_criacao: datetime
    data_atualizacao: datetime

    class Config:
        orm_mode = True  # Permite que os esquemas usem objetos do SQLAlchemy
