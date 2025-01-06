from fastapi import FastAPI

# Criando instancia do FastAPI
app = FastAPI(title="TO DO LIST API", version="0.1.0")


# Rota principal
@app.get("/")

def index():
    return {"status": "TO DO LIST API is running!!!"}
