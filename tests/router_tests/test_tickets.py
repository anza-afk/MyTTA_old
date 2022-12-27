DATA = {
    "title": "test ticket",
    "description": "test ticket description",
    "created_at": "2022-12-22T09:28:04.255Z",
    "resolved_at": None,
    "superuser": None
}

def test_create_ticket(client):
    # user_id = 0
    response = client.post("/users/0/tickets/", json=DATA)
    print(response.json())
    assert response.status_code == 200 
    assert response.json()["title"] == "test ticket"


def test_get_ticket(client):
    response = client.post("/users/0/tickets/",json=DATA)
    response = client.get("/tickets/1/")
    assert response.status_code == 200
    assert response.json()['title'] == "test ticket"