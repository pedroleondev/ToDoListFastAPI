from fastapi import APIRouter, HTTPException, Depends
from app.models import Task
from app.database import db_tasks, get_next_id
from datetime import datetime

# Rota de tarefas
router = APIRouter(prefix="/tasks", tags=["Tarefas"])

# Rotas de tarefas (CRUD)

# Cria uma nova tarefa
@router.post("/", response_model=Task)
def create_task(titulo: str, descricao: str = None, estado: str = "pendente"):
    task = Task(
        id=get_next_id(),
        titulo=titulo,
        descricao=descricao,
        estado=estado,
        data_criacao=datetime.now(),
        data_atualizacao=datetime.now(),
    )
    db_tasks.append(task)
    return task

# Lista todas as tarefas cadastradas
@router.get("/", response_model=list[Task])
def list_tasks():
    return db_tasks

# Busca uma tarefa pelo ID e retorna seus detalhes
@router.get("/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in db_tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Tarefa não encontrada!")

# Atualiza uma tarefa pelo ID e retorna seus detalhes
@router.put("/{task_id}", response_model=Task)
def update_task(task_id: int, titulo: str, descricao: str = None, estado: str = "pendente"):
    for task in db_tasks:
        if task.id == task_id:
            if estado not in ["pendente", "em andamento", "concluída"]:
                raise HTTPException(status_code=400, detail="Estado inválido!")
            task.titulo = titulo
            task.descricao = descricao
            task.estado = estado
            task.data_atualizacao = datetime.now()
            return task
    raise HTTPException(status_code=404, detail="Tarefa não encontrada!")

# filtrar tarefas por estado
@router.get("/filter", response_model=list[Task])
def filter_by_state(estado: str):
    return [task for task in db_tasks if task.estado == estado]

# Deleta uma tarefa pelo ID e retorna uma resposta vazia confirmando a exclusão
@router.delete("/{task_id}", status_code=204)
def delete_task(task_id: int):
    global db_tasks
    db_tasks = [task for task in db_tasks if task.id != task_id]
    return

