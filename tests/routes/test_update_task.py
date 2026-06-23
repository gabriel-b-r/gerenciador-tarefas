from app.models.task import Task
from app.extensions.database import db

def test_update_task_returns_200(client, app):
    with app.app_context():
        task_1 = Task(
            title="Task 1",
            description="Task 1",
            priority="LOW",
            status="PENDING"
        )

        db.session.add(task_1)
        db.session.commit()

    payload = {
        "title": "Test",
        "description": "Test task 1",
        "priority": "HIGH",
        "status": "COMPLETED"
    }

    response = client.put("/api/v1/tasks/1", json=payload)

    data = response.get_json()

    assert response.status_code == 200
    assert data["title"] == "Test"
    assert data["description"] == "Test task 1"
    assert data["priority"] == "HIGH"
    assert data["status"] == "COMPLETED"


def test_update_task_returns_404(client):
    payload = {
        "title": "Test"
    }
   
    response = client.put("/api/v1/tasks/1", json=payload)

    data = response.get_json()

    assert response.status_code == 404
    assert data["error"] == "Task not found"

#Add test_update_task_returns_400()