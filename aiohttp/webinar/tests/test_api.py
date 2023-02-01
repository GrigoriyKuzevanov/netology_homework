import requests

API_URL = "http://127.0.0.1:8000"


def test_root():
    assert requests.get(API_URL).status_code == 404


def test_get_user_not_exists():
    response = requests.get(f"{API_URL}/users/999999")
    assert response.status_code == 404
    assert response.json() == {"status": "error", "description": "User not found"}


def test_get_user_exitst(create_user):
    user_id = create_user["id"]
    response = requests.get(f"{API_URL}/users/{user_id}")
    assert response.status_code == 200
    user = response.json()
    assert create_user["username"] == user["username"]


def test_create_user():
    response = requests.post(
        f"{API_URL}/users/", json={"username": "test_user", "password": "1234"}
    )
    assert response.status_code == 200
    user_data = response.json()
    assert "id" in user_data
    assert isinstance(user_data["id"], int)


def test_create_user_2():
    response = requests.post(
        f"{API_URL}/users/", json={"username": "test_user", "password": "1234"}
    )
    assert response.status_code == 409
    assert response.json() == {"status": "error", "description": "user already exists"}


def test_patch_user(create_user):
    user_id = create_user["id"]
    response = requests.patch(
        f"{API_URL}/users/{user_id}", json={"username": "patched_name"}
    )
    assert response.status_code == 200
    assert response.json() == {"status": "success"}
    response = requests.get(f"{API_URL}/users/{user_id}")
    user_name = response.json()["username"]
    assert response.status_code == 200
    assert user_name == "patched_name"


def test_delete_user(create_user):
    user_id = create_user["id"]
    response = requests.delete(f"{API_URL}/users/{user_id}")
    assert response.status_code == 200
    assert response.json() == {"status": "success"}
    response = requests.get(f"{API_URL}/users/{user_id}")
    assert response.status_code == 404
    assert response.json() == {"status": "error", "description": "User not found"}
