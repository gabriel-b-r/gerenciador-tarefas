def test_create_task_returns_201(client):
    payload = {
        "title": "test"
    }

    response = client.post("/api/v1/tasks", json=payload)

    data = response.get_json()

    assert response.status_code == 201
    assert data["title"] == "test"
    assert data["priority"] == "LOW"
    assert data["status"] == "PENDING"


def test_create_task_returns_400(client):
    payload = {}

    response = client.post("/api/v1/tasks", json=payload)

    data = response.get_json()

    assert response.status_code == 400
    assert data["error"] == "Title is required"