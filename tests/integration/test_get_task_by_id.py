def test_get_task_by_id_returns_200(client, app, created_task):
    with app.app_context():
        created_task

    response = client.get("api/v1/tasks/1")

    data = response.get_json()

    assert response.status_code == 200
    assert data["id"] == 1
    assert data["title"] == "Task"
    assert data["description"] == "Testing"
    assert data["priority"] == "LOW"
    assert data["status"] == "PENDING"


def test_get_task_by_id_returns_404(client):
    
    response = client.get("api/v1/tasks/1")

    data = response.get_json()

    assert response.status_code == 404
    assert data["error"] == "Task not found"
