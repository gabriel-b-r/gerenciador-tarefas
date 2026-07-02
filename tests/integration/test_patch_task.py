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

    assert response.status_code == 404
    assert "error" in response.json


def test_patch_task_with_empty_body_returns_400(client, app, created_task):
    with app.app_context():
        created_task

    payload = {}

    response = client.patch("/api/v1/tasks/1", json=payload)

    assert response.status_code == 400
    assert "error" in response.json
