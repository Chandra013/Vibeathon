from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from extensions import mongo

occupancy_bp = Blueprint('occupancy', __name__, url_prefix='/api/occupancy')

@occupancy_bp.route('/', methods=['GET'])
@jwt_required()
def get_occupancy():
    user = get_jwt_identity()
    role = user['role']
    department = user.get('department')
    school = user.get('school')
    query = {}
    if role == 'Event Coordinator':
        query['coordinator'] = user['username']
    elif role == 'HOD':
        query['department'] = department
    elif role == 'Dean':
        query['school'] = school
    # Institutional Head and Admin see all
    events = list(mongo.db.events.find(query))
    for e in events:
        e['_id'] = str(e['_id'])
    return jsonify(occupancy=events), 200
