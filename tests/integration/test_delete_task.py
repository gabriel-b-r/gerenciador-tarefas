def test_delete_task_returns_204(client, app, created_task):
    with app.app_context():
        created_task

    response = client.delete("/api/v1/tasks/1")

    data = response.get_json()

    assert response.status_code == 204
    assert data == None

def test_delete_task_returns_404(client):
    response = client.delete("/api/v1/tasks/1")

    data = response.get_json()

    assert response.status_code == 404
    assert data["error"] == "Task not found"