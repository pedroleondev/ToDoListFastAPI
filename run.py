from app.main import app
import uvicorn
from app.database import engine
from app.models import SQLModel

# Inicializando o banco de dados
def create_db_and_tables():
    SQLModel.metadata.create_all(bind=engine)

# Inicializando o servidor
if __name__ == "__main__":
     create_db_and_tables()
     uvicorn.run("app.main:app", reload=True, host="127.0.0.1", port=8000)
