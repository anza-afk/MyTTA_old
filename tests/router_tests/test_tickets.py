def test_create_ticket(client):
    # user_id = 0
    data = {
        "title": "test ticket",
        "description": "test ticket description",
        "created_at": "2022-12-22T09:28:04.255Z",
        "resolved_at": None,
        "superuser": None
    }
    response = client.post("/users/0/tickets/", json=data)
    print(response.json())
    assert response.status_code == 200 
    assert response.json()["title"] == "test ticket"
