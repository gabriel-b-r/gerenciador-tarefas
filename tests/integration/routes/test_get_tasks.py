from app.models.task import Task
from app.extensions.database import db

def test_get_tasks_returns_200(client, app):
    with app.app_context():
        task_1 = Task(title="Task 1")
        task_2 = Task(title="Task 2")

        db.session.add(task_1)
        db.session.add(task_2)
        db.session.commit()

    response = client.get("/api/v1/tasks")

    data = response.get_json()    

    assert response.status_code == 200
    assert len(data) == 2
    assert data[0]["id"] == 1
    assert data[0]["title"] == "Task 1"
    assert data[1]["id"] == 2
    assert data[1]["title"] == "Task 2"


def test_get_tasks_returns_empty_list_200(client):
    response = client.get("/api/v1/tasks")

    data = response.get_json()

    assert response.status_code == 200
    assert len(data) == 0
    assert data == []
    
