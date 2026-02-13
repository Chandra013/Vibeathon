from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models.user import verify_user
from extensions import mongo
from flask_bcrypt import Bcrypt

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')
bcrypt = Bcrypt()

@auth_bp.route('/reset_password', methods=['POST'])
def reset_password():
    data = request.get_json()
    username = data.get('username')
    new_password = data.get('new_password')
    if not username or not new_password or len(new_password) < 8:
        return jsonify(msg='Invalid input or password too short'), 400
    user = mongo.db.users.find_one({'username': username})
    if not user:
        return jsonify(msg='User not found'), 404
    hashed = bcrypt.generate_password_hash(new_password).decode('utf-8')
    mongo.db.users.update_one({'username': username}, {'$set': {'password': hashed}})
    return jsonify(msg='Password reset successful'), 200

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = verify_user(mongo, username, password)
    if user:
        access_token = create_access_token(identity={
            'username': user['username'],
            'role': user['role'],
            'department': user.get('department'),
            'school': user.get('school')
        })
        return jsonify(access_token=access_token), 200
    return jsonify(msg='Invalid credentials'), 401
