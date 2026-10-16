from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid

app = FastAPI()

class TaskRequest(BaseModel):
    title: str
    description: str = ""

class TaskResponse(BaseModel):
    id: str
    title: str
    description: str
    status: str

tasks_db: dict = {}

@app.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskRequest):
    task_id = str(uuid.uuid4())
    new_task = {
        "id": task_id,
        "title": task.title,
        "description": task.description,
        "status": "pending"
    }
    tasks_db[task_id] = new_task
    return new_task

@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: str):
    task = tasks_db.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

def demo():
    from fastapi.testclient import TestClient
    client = TestClient(app)
    res = client.post("/tasks", json={"title": "Test Task"})
    print(f"Status: {res.status_code}")
    print(f"Body: {res.json()}")
