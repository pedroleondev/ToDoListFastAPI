from app.main import app
import uvicorn


# Inicializando o servidor
if __name__ == "__main__":
     uvicorn.run("app.main:app", reload=True, host="127.0.0.1", port=8000)
