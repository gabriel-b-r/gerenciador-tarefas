from app.models.task import Task
from app.extensions.database import db

def test_patch_task_returns_200(client, app, created_task):
    with app.app_context():
        created_task

    payload = {
        "title": "Test"
    }

    response = client.patch("/api/v1/tasks/1", json=payload)

    data = response.get_json()

    assert response.status_code == 200
    assert data["title"] == "Test"


def test_patch_task_returns_404(client, valid_task_payload):
    response = client.patch("/api/v1/tasks/1", json=valid_task_payload)

    data = response.get_json()

    assert response.status_code == 404
    assert data["error"] == "Task not found"


def test_patch_task_returns_400_empty_body(client, app, created_task):
    with app.app_context():
        created_task

    payload = {}

    response = client.patch("/api/v1/tasks/1", json=payload)

    data = response.get_json()

    assert response.status_code == 400
    assert data["error"] == "Request body cannot be empty"


def test_patch_task_returns_400_required_valid_field(client, app, created_task):
    with app.app_context():
        created_task

    payload = {
        "test": "test"
    }

    response = client.patch("/api/v1/tasks/1", json=payload)

    data = response.get_json()

    assert response.status_code == 400
    assert data["error"] == "At least one valid field must be provided"
