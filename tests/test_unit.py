from app.app import *
import pytest

@pytest.fixture
def client():
    return app.test_client()

def test_get_users():
    assert get_users() == [{"id": 1, "name": "Wojciech", "lastname": "Oczkowski"}]

def test_get_user_by_id():
    assert get_user_by_id(1) == {"id": 1, "name": "Wojciech", "lastname": "Oczkowski"}

def test_create_user(client):
    response = client.post("/users", json={"name": "Marcin", "lastname": "Dublej"})
    data = response.get_json()
    assert data == [{"id": 1, "name": "Wojciech", "lastname": "Oczkowski"}, {"id":2, "name": "Marcin", "lastname": "Dublej"}]

def test_update_user(client):
    client.patch("/users/1", json={"name": "Michał"})
    assert get_user_by_id(1) == {"id": 1, "name": "Michał", "lastname": "Oczkowski"}

def test_update_or_add_user_updating(client):
    client.put("/users/1", json={"name": "Michał"})
    assert get_user_by_id(1) == {"id": 1, "name": "Michał", "lastname": "Oczkowski"}

def test_update_or_add_user_adding(client):
    client.put("/users/a", json={"name": "Michał", "lastname": "Anioł"})
    assert get_user_by_id(2) == {"id": 2, "name": "Michał", "lastname": "Anioł"}

def test_remove_user(client):
    client.delete("/users/1")
    assert get_users() == []

def test_remove_user_not_existing(client):
    client.delete("/users/5")
    assert get_users() == [{"id": 1, "name": "Wojciech", "lastname": "Oczkowski"}]