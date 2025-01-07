from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models import Task
from datetime import datetime

# Função para criar uma nova tarefa
def create_task(db: Session, task: Task) -> Task:
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

# Função para listar todas as tarefas
def get_tasks(db: Session):
    return db.query(Task).all()

# Função para buscar uma tarefa pelo ID
def get_task_by_id(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

# Função para atualizar uma tarefa pelo ID
def update_task(db: Session, task_id: int, task_data: dict):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        # atualização dos campos permitidos
        for key, value in task_data.items():
            if key == "data_criacao": # alteração para que seja ignorado o campo data_criacao
                continue
            setattr(task, key, value)
            # Atualiza apenas o campo 'data_atualizacao'
        task.data_atualizacao = datetime.now()
        try:
            db.commit()
            db.refresh(task)
        except IntegrityError:
            db.rollback()
            return None
    return task

# Função para filtrar tarefas por estado
def filter_tasks_by_state(db: Session, estado: str):
    return db.query(Task).filter(Task.estado == estado).all()


# Função para deletar uma tarefa pelo ID
def delete_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
        return task
    return None