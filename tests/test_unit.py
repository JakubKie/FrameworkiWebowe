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
