from fastapi import FastAPI
from app.routers import tasks

app = FastAPI()

# Registrar rotas
app.include_router(tasks.router)

@app.get("/")
def root():
    return {"message": "API de Gerenciamento de Tarefas"}
