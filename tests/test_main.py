import pytest
from fastapi.testclient import TestClient
from main import app, tasks_db

@pytest.fixture
def client():
    tasks_db.clear()
    return TestClient(app)

def test_create_task(client):
    res = client.post("/tasks", json={"title": "New Task"})
    assert res.status_code == 200
    data = res.json()
    assert data["title"] == "New Task"
    assert data["status"] == "pending"
    assert "id" in data

def test_get_task(client):
    res = client.post("/tasks", json={"title": "Existing Task"})
    task_id = res.json()["id"]
    res = client.get(f"/tasks/{task_id}")
    assert res.status_code == 200
    assert res.json()["title"] == "Existing Task"

def test_get_task_not_found(client):
    res = client.get("/tasks/non-existent-id")
    assert res.status_code == 404
