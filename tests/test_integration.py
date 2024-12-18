from app.app import *
import pytest

@pytest.fixture
def client():
    return app.test_client()

def test_get_users(client):
    response = client.get("/users")
    assert response.status_code == 200

def test_get_users_by_id(client):
    response = client.get("/users/1")
    assert response.status_code == 200

def test_create_user(client):
    response = client.post("/users", json={"name": "Marcin", "lastname": "Dublej"})
    assert response.status_code == 201

def test_update_user(client):
    response = client.patch("/users/1", json={"name": "Michał"})
    assert response.status_code == 204

def test_update_or_add_user_updating(client):
    response = client.put("/users/1", json={"name": "Michał"})
    assert response.status_code == 204

def test_update_or_add_user_adding(client):
    response = client.put("/users/a", json={"name": "Michał", "lastname": "Anioł"})
    assert response.status_code == 204