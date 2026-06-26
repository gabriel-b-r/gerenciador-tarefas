from app.models.task import Task
from app.extensions.database import db

def test_patch_task_returns_200(client, app):
    with app.app_context():
        task_1 = Task(
            title="Task 1",
            description="Testing task 1",
            priority="HIGH",
            status="PENDING"
        )

        db.session.add(task_1)
        db.session.commit()

    payload = {
        "title": "Test"
    }

    response = client.patch("/api/v1/tasks/1", json=payload)

    data = response.get_json()

    assert response.status_code == 200
    assert data["title"] == "Test"


def test_patch_task_returns_404(client):
    payload = {
        "title": "Test"
    }

    response = client.patch("/api/v1/tasks/1", json=payload)

    data = response.get_json()

    assert response.status_code == 404
    assert data["error"] == "Task not found"


def test_patch_task_returns_400_empty_body(client, app):
    with app.app_context():
        task_1 = Task(
            title="Task 1",
            description="testing task 1",
            priority="HIGH",
            status="PENDING"
        )

        db.session.add(task_1)
        db.session.commit()

    payload = {}

    response = client.patch("/api/v1/tasks/1", json=payload)

    data = response.get_json()

    assert response.status_code == 400
    assert data["error"] == "Request body cannot be empty"


def test_patch_task_returns_400_required_valid_field(client, app):
    with app.app_context():
        task_1 = Task(
            title="Task 1",
            description="testing task 1",
            priority="HIGH",
            status="PENDING"
        )

        db.session.add(task_1)
        db.session.commit()

    payload = {
        "test": "test"
    }

    response = client.patch("/api/v1/tasks/1", json=payload)

    data = response.get_json()

    assert response.status_code == 400
    assert data["error"] == "At least one valid field must be provided"
