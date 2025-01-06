from fastapi import FastAPI


app = FastAPI()

@app.get("/")

def index():
    return {"status": "TO DO LIST API is running!"}
