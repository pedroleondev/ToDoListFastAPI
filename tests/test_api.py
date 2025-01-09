from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
token = None

def test_create_user():
    response = client.post("/auth/", json={"usuario": "usuario_test", "senha": "senh@teste"})
    assert response.status_code == 201
    assert response.json()["message"] == "Usuário criado com sucesso!"

def test_login():
    global token
    response = client.post("/auth/token", data={"username": "testuser", "password": "testpassword"})
    assert response.status_code == 200
    assert "access_token" in response.json()
    token = response.json()["access_token"]

def test_create_task():
    global token
    response = client.post("/tasks/", json={"titulo": "Teste", "descricao": "Teste descrição", "estado": "pendente"},
                           headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 201
    assert response.json()["titulo"] == "Teste"

def test_list_tasks():
    global token
    response = client.get("/tasks/", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_filter_tasks():
    global token
    response = client.get("/tasks/filter?estado=pendente", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_task():
    global token
    # Crie a tarefa antes de atualizá-la
    response_create = client.post("/tasks/", json={"titulo": "Inicial", "descricao": "Inicial", "estado": "novo"},
                                  headers={"Authorization": f"Bearer {token}"})
    assert response_create.status_code == 201  # Verifique se a criação foi bem-sucedida
    task_id = response_create.json()["id"]    # Extraia o ID da tarefa criada

    # Atualize a tarefa recém-criada
    response_update = client.put(f"/tasks/{task_id}", json={"titulo": "Atualizado", "descricao": "Atualizado", "estado": "em andamento"},
                                 headers={"Authorization": f"Bearer {token}"})
    assert response_update.status_code == 200
    assert response_update.json()["estado"] == "em andamento"

def test_delete_task():
    global token
    # Crie a tarefa antes de excluí-la
    response_create = client.post("/tasks/", json={"titulo": "Inicial", "descricao": "Inicial", "estado": "novo"},
                                  headers={"Authorization": f"Bearer {token}"})
    assert response_create.status_code == 201  # Verifique se a criação foi bem-sucedida
    task_id = response_create.json()["id"]    # Extraia o ID da tarefa criada

    # Exclua a tarefa recém-criada
    response_delete = client.delete(f"/tasks/{task_id}", headers={"Authorization": f"Bearer {token}"})
    assert response_delete.status_code == 204

def test_get_current_user():
    global token
    response = client.get("/user", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json()["User"]["username"] == "testuser"
