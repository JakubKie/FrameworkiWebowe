from flask import Flask
from app.saved_users import users

app = Flask(__name__)

@app.get('/users')
def get_users():
    return users
