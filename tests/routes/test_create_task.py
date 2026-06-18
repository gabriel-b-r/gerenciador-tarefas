def test_create_task_returns_201(client):
    #arrange
    payload = {
        "title": "test"
    }

    #act
    response = client.post("/api/v1/tasks", json=payload)

    print(response.status_code)
    print(response.location)

    #assert
    assert response.status_code == 201

    data = response.get_json()

    assert data["data"]["title"] == "test"