from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional


# Modelo de dados para a tarefa
# id (inteiro, autoincrementado)
# titulo (string, obrigatório)
# descricao (string, opcional)
# estado (string, obrigatório, valores possíveis: "pendente", "em andamento", "concluída")
# data_criacao (datetime, gerado automaticamente)
# data_atualizacao (datetime, atualizado automaticamente)

class Task(BaseModel):
    id: int
    titulo: str = Field(..., example="Minha tarefa")
    descricao: Optional[str] = Field(None, example="Descrição opcional")
    estado: str = Field(..., example="pendente", pattern="^(pendente|em andamento|concluída)$")
    data_criacao: datetime
    data_atualizacao: datetime
