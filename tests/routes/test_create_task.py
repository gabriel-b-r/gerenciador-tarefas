def test_create_task_returns_201(client):
    payload = {
        "title": "test"
    }

    response = client.post("/api/v1/tasks", json=payload)

    print(response.status_code)
    print(response.location)

    assert response.status_code == 201

    data = response.get_json()

    assert data["success"] == True
    assert data["data"]["title"] == "test"
    assert data["data"]["priority"] == "LOW"
    assert data["data"]["status"] == "PENDING"


def test_create_task_returns_400(client):
    payload = {}

    response = client.post("/api/v1/tasks", json=payload)

    print(response.status_code)
    print(response.location)

    assert response.status_code == 400
    
    data = response.get_json()

    assert data["sucess"] == False
    assert data["message"] == "Title is required"