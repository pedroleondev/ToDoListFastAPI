from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_task():
    response = client.post("/tasks/", json={"titulo": "Teste", "descricao": "Teste descrição", "estado": "pendente"})
    assert response.status_code == 201
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
    # Crie a tarefa antes de atualizá-la
    response_create = client.post("/tasks/", json={"titulo": "Inicial", "descricao": "Inicial", "estado": "novo"})
    assert response_create.status_code == 201  # Verifique se a criação foi bem-sucedida
    task_id = response_create.json()["id"]    # Extraia o ID da tarefa criada

    # Atualize a tarefa recém-criada
    response_update = client.put(f"/tasks/{task_id}", json={"titulo": "Atualizado", "descricao": "Atualizado", "estado": "em andamento"})
    assert response_update.status_code == 200
    assert response_update.json()["estado"] == "em andamento"

def test_delete_task():
    # Crie a tarefa antes de excluí-la
    response_create = client.post("/tasks/", json={"titulo": "Inicial", "descricao": "Inicial", "estado": "novo"})
    assert response_create.status_code == 201  # Verifique se a criação foi bem-sucedida
    task_id = response_create.json()["id"]    # Extraia o ID da tarefa criada

    # Exclua a tarefa recém-criada
    response_delete = client.delete(f"/tasks/{task_id}")
    assert response_delete.status_code == 204