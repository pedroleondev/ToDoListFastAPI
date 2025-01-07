from fastapi import APIRouter, HTTPException, Depends
from app.models import Task
from app.database import db_tasks, get_next_id
from datetime import datetime

router = APIRouter(prefix="/tasks", tags=["Tarefas"])

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

@router.get("/", response_model=list[Task])
def list_tasks():
    return db_tasks

@router.get("/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in db_tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@router.put("/{task_id}", response_model=Task)
def update_task(task_id: int, titulo: str, descricao: str = None, estado: str = "pendente"):
    for task in db_tasks:
        if task.id == task_id:
            task.titulo = titulo
            task.descricao = descricao
            task.estado = estado
            task.data_atualizacao = datetime.now()
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@router.delete("/{task_id}", status_code=204)
def delete_task(task_id: int):
    global db_tasks
    db_tasks = [task for task in db_tasks if task.id != task_id]
    return
