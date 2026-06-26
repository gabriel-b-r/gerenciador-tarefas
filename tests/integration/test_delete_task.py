from app.models.task import Task
from app.extensions.database import db

def test_delete_task_returns_204(client, app):
    with app.app_context():
        task_1 = Task(title="Task 1")

        db.session.add(task_1)
        db.session.commit()

    response = client.delete("/api/v1/tasks/1")

    data = response.get_json()

    assert response.status_code == 204
    assert data == None

def test_delete_task_returns_404(client):
    response = client.delete("/api/v1/tasks/1")

    data = response.get_json()

    assert response.status_code == 404
    assert data["error"] == "Task not found"