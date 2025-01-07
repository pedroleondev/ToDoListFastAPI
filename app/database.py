# from typing import List
# from app.models import Task
# from datetime import datetime

#################################

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Configuração do banco SQLite
DATABASE_URL = "sqlite:///./app/db.sqlite"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Criar sessão do banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependência para obter a sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



############################################################################################################

# # Simula o banco de dados em memória
# # futura implementação: substituir por um banco de dados real (sqlite)
# db_tasks: List[Task] = []
# task_id_counter = 1


# # Função para gerar o próximo ID de tarefa
# def get_next_id():
#     global task_id_counter
#     task_id_counter += 1
#     return task_id_counter
