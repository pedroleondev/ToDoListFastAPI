from fastapi import FastAPI
from app.routers import tasks


# Inicializando o servidor
app = FastAPI()

# Registrar rotas
app.include_router(tasks.router)

# Rota raiz
@app.get("/")
def root():
    return {"message": "API de Gerenciamento de Tarefas - To Do List ONLINE!"}
