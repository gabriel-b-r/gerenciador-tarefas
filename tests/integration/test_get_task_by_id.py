from app.models.task import Task
from app.extensions.database import db

def test_get_task_by_id_returns_200(client, app):
    with app.app_context():
        task_1 = Task(title="Task 1")

        db.session.add(task_1)
        db.session.commit()

    response = client.get("api/v1/tasks/1")

    data = response.get_json()

    assert response.status_code == 200
    assert data["id"] == 1
    assert data["title"] == "Task 1"


def test_get_task_by_id_returns_404(client):
    
    response = client.get("api/v1/tasks/1")

    data = response.get_json()

    assert response.status_code == 404
    assert data["error"] == "Task not found"
