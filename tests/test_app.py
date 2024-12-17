from flask import Flask

from app import app

def test_flask_app_exists():
    assert isinstance(app, Flask)