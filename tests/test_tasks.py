from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_task():
    response = client.post("/tasks/", json={"titulo": "Teste", "descricao": "Teste descrição", "estado": "pendente"})
    assert response.status_code == 200
    assert response.json()["titulo"] == "Teste"

def test_list_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_filter_tasks():
    response = client.get("/tasks/filter?estado=pendente")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_task():
    response = client.put("/tasks/1", json={"titulo": "Atualizado", "descricao": "Atualizado", "estado": "em andamento"})
    assert response.status_code == 200
    assert response.json()["estado"] == "em andamento"

def test_delete_task():
    response = client.delete("/tasks/1")
    assert response.status_code == 204
