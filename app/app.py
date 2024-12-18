from flask import Flask, request
from saved_users import users

app = Flask(__name__)

@app.get('/users')
def get_users():
    return users, 200

@app.get('/users/<id>')
def get_user_by_id(id):
    for user in users:
        if str(user['id']) == str(id):
            wanted_user = user
            return wanted_user, 200
    else:
        return 404

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
        if str(user['id']) == str(id):
            user.update(data)
            break
    return users, 204

@app.put('/users/<id>')
def update_or_add_user(id):
    data = request.get_json()
    for user in users:
        if str(user['id']) == str(id):
            user.update(data)
            return users, 204
    a = 0
    for user in users:
        a+=1
        if user['id'] != a:
            users.append({"id": a, "name": data['name'], "lastname": data['lastname']})
            return users, 204

@app.delete('/users/<id>')
def delete_user(id):
    for user in users:
        if str(user['id']) == str(id):
            users.remove(user)
            return users, 204
    else:
        return users, 400
