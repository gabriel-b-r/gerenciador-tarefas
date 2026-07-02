def test_create_task_returns_201(client, valid_task_payload):
    response = client.post("/api/v1/tasks", json=valid_task_payload)

    data = response.get_json()

    assert response.status_code == 201
    assert data["id"] == 1
    assert data["title"] == "Task"
    assert data["description"] == "Testing"
    assert data["priority"] == "LOW"
    assert data["status"] == "PENDING"


def test_create_task_with_invalid_content_type_returns_415(client):
    payload = """<?xml version="1.0" encoding="UTF-8"?>
    <task>
        <title>Task</title>
        <description>Testing</description>
    </task>
"""

    response = client.post("/api/v1/tasks", data=payload, content_type="application/xml")

    assert response.status_code == 415
    assert "error" in response.json



def test_create_task_with_empty_body_returns_400(client):
    payload = {}

    response = client.post("/api/v1/tasks", json=payload)

    assert response.status_code == 400
    assert "error" in response.json


def test_create_task_with_unknown_field_returns_400(client):
    payload = {
        "unknown_field": "test"
    }

    response = client.post("/api/v1/tasks", json=payload)

    assert response.status_code == 400
    assert "error" in response.json
