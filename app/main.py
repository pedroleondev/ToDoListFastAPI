from fastapi import FastAPI
from app.routers import tasks, auth


# Inicializando o servidor
app = FastAPI()

# Registrar rotas
app.include_router(tasks.router)
app.include_router(auth.router)

# Rota raiz
@app.get("/")
def root():
    return {"message": "API de Gerenciamento de Tarefas - To Do List ONLINE!"}
