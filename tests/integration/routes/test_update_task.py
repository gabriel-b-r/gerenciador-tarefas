from app.models.task import Task
from app.extensions.database import db

def test_update_task_returns_200(client, app, created_task):
    with app.app_context():
        created_task

    payload = {
        "title": "Test",
        "description": "Test task 1",
        "priority": "HIGH",
        "status": "COMPLETED"
    }

    response = client.put("/api/v1/tasks/1", json=payload)

    data = response.get_json()
    assert response.status_code == 200
    assert data["id"] == 1
    assert data["title"] == "Test"
    assert data["description"] == "Test task 1"
    assert data["priority"] == "HIGH"
    assert data["status"] == "COMPLETED"


def test_update_task_returns_404(client, valid_task_payload):
    response = client.put("/api/v1/tasks/1", json=valid_task_payload)

    assert response.status_code == 404
    assert "error" in response.json


def test_update_task_with_invalid_body_returns_400(client, app, created_task):
    with app.app_context():
        created_task

    payload = {
        "description": "Test",
        "priority": "HIGH",
        "status": "COMPLETED"
    }

    response = client.put("/api/v1/tasks/1", json=payload)

    assert response.status_code == 400
    assert "error" in response.json
