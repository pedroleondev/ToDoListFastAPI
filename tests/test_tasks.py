from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_task():
    response = client.post("/tasks/", json={"titulo": "Teste", "descricao": "Descrição", "estado": "pendente"})
    assert response.status_code == 200
    assert response.json()["titulo"] == "Teste"
