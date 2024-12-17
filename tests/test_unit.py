from app.app import *

def test_get_users():
    assert get_users() == [{"id": 1, "name": "Wojciech", "lastname": "Oczkowski"}]

def test_get_user_by_id():
    assert get_user_by_id(1) == {"id": 1, "name": "Wojciech", "lastname": "Oczkowski"}