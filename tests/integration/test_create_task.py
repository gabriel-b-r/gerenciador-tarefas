def test_create_task_returns_201(client, valid_task_payload):
    response = client.post("/api/v1/tasks", json=valid_task_payload)

    data = response.get_json()

    assert response.status_code == 201
    assert data["id"] == 1
    assert data["title"] == "Task"
    assert data["description"] == "Testing"
    assert data["priority"] == "LOW"
    assert data["status"] == "PENDING"


def test_create_task_returns_400(client):
    payload = {}

    response = client.post("/api/v1/tasks", json=payload)

    data = response.get_json()

    assert response.status_code == 400
    assert data["error"] == "Title is required"