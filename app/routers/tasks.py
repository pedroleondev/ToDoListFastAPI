from fastapi import APIRouter, HTTPException, Depends
from datetime import datetime
from app.models import Task
from app.database import get_db
from sqlalchemy.orm import Session
from app.crud import (
    create_task,
    get_tasks,
    get_task_by_id,
    update_task,
    filter_tasks_by_state,
    delete_task,
)

# Rota de tarefas, o APIRouter é utilizado para modularizar as rotas e facilitar a reutilização
router = APIRouter(prefix="/tasks", tags=["Tarefas"])

# Rotas de tarefas (CRUD)

# Cria uma nova tarefa
# status_code 201 para indicar que a tarefa foi criada com sucesso
@router.post("/", response_model=Task, status_code=201, summary="Criar nova tarefa", description="Endpoint para criar uma nova tarefa.") 
def create_task_endpoint(task: Task, db: Session = Depends(get_db)):
    return create_task(db, task)

# Lista todas as tarefas cadastradas
@router.get("/", response_model=list[Task], summary="Listar tarefas", description="Endpoint para listas todas as tarefas existentes.")
def list_tasks_endpoint(db: Session = Depends(get_db)):
    return get_tasks(db)

# Filtra tarefas por estado
@router.get("/filter", response_model=list[Task], summary="Filtrar tarefas por estados", description="Endpoint para filtrar tarefas por estado.")
def filter_tasks_by_state_endpoint(estado: str, db: Session = Depends(get_db)):
    tasks = filter_tasks_by_state(db, estado)
    if not tasks:
        raise HTTPException(status_code=404, detail="Nenhuma tarefa encontrada para o estado especificado!")
    return tasks

# Busca uma tarefa pelo ID e retorna seus detalhes
@router.get("/{task_id}", response_model=Task, summary="Buscar tarefa por ID", description="Endpoint para buscar tarefa através do ID.")
def get_task_endpoint(task_id: int, db: Session = Depends(get_db)):
    task = get_task_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada!")
    return task

# Atualiza uma tarefa pelo ID e retorna seus detalhes
@router.put("/{task_id}", response_model=Task, summary="Atualizar tarefa", description="Endpoint para atualizar info da tarefa.")
def update_task_endpoint(task_id: int, task_data: dict, db: Session = Depends(get_db)):
    task = update_task(db, task_id, task_data)
    if not task:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada!")
    return task



# Deleta uma tarefa pelo ID e retorna uma resposta vazia confirmando a exclusão
@router.delete("/{task_id}", status_code=204, summary="Deletar tarefa", description="Endpoint para deletar tarefa por ID.")
def delete_task_endpoint(task_id: int, db: Session = Depends(get_db)):
    delete_task(db, task_id)
    return





# # Cria uma nova tarefa
# @router.post("/", response_model=Task)
# def create_task(titulo: str, descricao: str = None, estado: str = "pendente"):
#     task = Task(
#         id=get_next_id(),
#         titulo=titulo,
#         descricao=descricao,
#         estado=estado,
#         data_criacao=datetime.now(),
#         data_atualizacao=datetime.now(),
#     )
#     db_tasks.append(task)
#     return task

# # Lista todas as tarefas cadastradas
# @router.get("/", response_model=list[Task])
# def list_tasks():
#     return db_tasks

# # Busca uma tarefa pelo ID e retorna seus detalhes
# @router.get("/{task_id}", response_model=Task)
# def get_task(task_id: int):
#     for task in db_tasks:
#         if task.id == task_id:
#             return task
#     raise HTTPException(status_code=404, detail="Tarefa não encontrada!")

# # Atualiza uma tarefa pelo ID e retorna seus detalhes
# @router.put("/{task_id}", response_model=Task)
# def update_task(task_id: int, titulo: str, descricao: str = None, estado: str = "pendente"):
#     for task in db_tasks:
#         if task.id == task_id:
#             if estado not in ["pendente", "em andamento", "concluída"]:
#                 raise HTTPException(status_code=400, detail="Estado inválido!")
#             task.titulo = titulo
#             task.descricao = descricao
#             task.estado = estado
#             task.data_atualizacao = datetime.now()
#             return task
#     raise HTTPException(status_code=404, detail="Tarefa não encontrada!")

# # filtrar tarefas por estado
# @router.get("/filter", response_model=list[Task])
# def filter_by_state(estado: str):
#     return [task for task in db_tasks if task.estado == estado]

# # Deleta uma tarefa pelo ID e retorna uma resposta vazia confirmando a exclusão
# @router.delete("/{task_id}", status_code=204)
# def delete_task(task_id: int):
#     global db_tasks
#     db_tasks = [task for task in db_tasks if task.id != task_id]
#     return

