
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models.venue import add_venue, update_venue
from models.resource import add_resource, update_resource
from extensions import mongo

admin_bp = Blueprint('admin', __name__, url_prefix='/api/admin')

@admin_bp.route('/audit_logs', methods=['GET'])
def get_audit_logs():
    logs = list(mongo.db.audit_logs.find().sort('timestamp', -1))
    for l in logs:
        l['_id'] = str(l['_id'])
    return jsonify(logs=logs), 200

@admin_bp.route('/venue', methods=['POST'])
@jwt_required()
def add_venue_admin():
    data = request.get_json()
    add_venue(mongo, data)
    return jsonify(msg='Venue added by admin'), 201

@admin_bp.route('/venue/<venue_id>', methods=['PUT'])
@jwt_required()
def update_venue_admin(venue_id):
    data = request.get_json()
    update_venue(mongo, venue_id, data)
    return jsonify(msg='Venue updated by admin'), 200

@admin_bp.route('/resource', methods=['POST'])
@jwt_required()
def add_resource_admin():
    data = request.get_json()
    add_resource(mongo, data)
    return jsonify(msg='Resource added by admin'), 201

@admin_bp.route('/resource/<resource_id>', methods=['PUT'])
@jwt_required()
def update_resource_admin(resource_id):
    data = request.get_json()
    update_resource(mongo, resource_id, data)
    return jsonify(msg='Resource updated by admin'), 200
