def test_create_user(client):
    data = {
        "email": "testuser@nofoobar.com",
        "password": "testing",
        "tickets": [0,]
    }
    response = client.post("/users/", json=data)
    assert response.status_code == 200 
    assert response.json()["email"] == "testuser@nofoobar.com"
    assert response.json()["is_active"] == True
    print(response.json())