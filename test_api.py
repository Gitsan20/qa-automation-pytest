import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_posts():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_single_post():
    response = requests.get(f"{BASE_URL}/posts/1")
    data = response.json()
    
    assert response.status_code == 200
    assert data["id"] == 1
    assert "title" in data

def test_create_post():
    payload = {
        "title": "test",
        "body": "automation",
        "userId": 1
    }

    response = requests.post(f"{BASE_URL}/posts", json=payload)
    
    assert response.status_code == 201
    assert response.json()["title"] == "test"

def test_invalid_endpoint():
    response = requests.get(f"{BASE_URL}/invalid")
    assert response.status_code == 404
