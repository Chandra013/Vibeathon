from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app

def create_user(mongo, username, password, role, department=None, school=None):
    user = {
        'username': username,
        'password': generate_password_hash(password),
        'role': role,
        'department': department,
        'school': school
    }
    mongo.db.users.insert_one(user)
    return user

def verify_user(mongo, username, password):
    user = mongo.db.users.find_one({'username': username})
    if user and check_password_hash(user['password'], password):
        return user
    return None
