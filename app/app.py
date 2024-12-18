from flask import Flask, request
from saved_users import users

app = Flask(__name__)

@app.get('/users')
def get_users():
    return users

@app.get('/users/<id>')
def get_user_by_id(id):
    wanted_user = 0
    for user in users:
        if user['id'] == int(id):
            wanted_user = user
            break
    return wanted_user

@app.post('/users')
def create_user():
    data = request.get_json()
    id = 0
    for user in users:
        id+=1
        if user['id'] != id:
            users.insert(id-1, {"id": id, "name": data['name'], "lastname": data['lastname']})
            break
    else:
        id+=1
        users.append({"id": id, "name": data['name'], "lastname": data['lastname']})
    return users, 201

@app.patch('/users/<id>')
def update_user(id):
    data = request.get_json()
    for user in users:
        if user['id'] == int(id):
            user.update(data)
            break
    return users, 204