from typing import List
from app.models import Task
from datetime import datetime

# Simula o banco de dados em memória
db_tasks: List[Task] = []
task_id_counter = 1

def get_next_id():
    global task_id_counter
    task_id_counter += 1
    return task_id_counter
