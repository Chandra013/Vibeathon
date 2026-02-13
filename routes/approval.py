from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.approval import create_approval, get_approvals_by_event, update_approval
from extensions import mongo

approval_bp = Blueprint('approval', __name__, url_prefix='/api/approvals')

@approval_bp.route('/<event_id>', methods=['POST'])
@jwt_required()
def approve_event(event_id):
    user = get_jwt_identity()
    data = request.get_json()
    approval_data = {
        'event_id': event_id,
        'approver': user['username'],
        'role': user['role'],
        'action': data['action'],
        'reason': data.get('reason'),
    }
    create_approval(mongo, approval_data)
    return jsonify(msg='Approval action recorded'), 200

@approval_bp.route('/event/<event_id>', methods=['GET'])
@jwt_required()
def get_event_approvals(event_id):
    approvals = get_approvals_by_event(mongo, event_id)
    for a in approvals:
        a['_id'] = str(a['_id'])
    return jsonify(approvals=approvals), 200
