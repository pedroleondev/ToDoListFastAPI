from fastapi import FastAPI, HTTPException, Depends
from app.routers import tasks, auth
from app.dependencies import user_dependency, db_dependency
from starlette import status

# Inicializando o servidor
app = FastAPI()

# Registrar rotas
app.include_router(tasks.router)
app.include_router(auth.router)

# Rota raiz
@app.get("/")
def root():
    return {"message": "API de Gerenciamento de Tarefas - To Do List ONLINE!"}

# Rota para obter o usuário atual
@app.get("/user", status_code=status.HTTP_200_OK)
def get_current_user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='Autenticação falhou')
    return {"User": user}
