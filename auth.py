import json
from flask import  session

def register_user(username, password):
    users = load_users()
    if username in users:
        return False  
    users[username] = password
    with open('users.json', 'w') as file:
        json.dump(users, file)
    return True

def load_users():
    try:
        with open('users.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def login_user(username, password):
    users = load_users()
    if username in users and users[username] == password:
        session['username'] = username
        return True
    return False

def is_authenticated():
    return 'username' in session

def logout_user():
    session.pop('username', None)