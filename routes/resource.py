from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models.resource import add_resource, update_resource, get_resource, get_all_resources
from extensions import mongo

resource_bp = Blueprint('resource', __name__, url_prefix='/api/resources')

@resource_bp.route('/', methods=['POST'])
@jwt_required()
def add():
    data = request.get_json()
    add_resource(mongo, data)
    return jsonify(msg='Resource added'), 201

@resource_bp.route('/<resource_id>', methods=['PUT'])
@jwt_required()
def update(resource_id):
    data = request.get_json()
    update_resource(mongo, resource_id, data)
    return jsonify(msg='Resource updated'), 200

@resource_bp.route('/<resource_id>', methods=['GET'])
@jwt_required()
def get(resource_id):
    resource = get_resource(mongo, resource_id)
    if resource:
        resource['_id'] = str(resource['_id'])
        return jsonify(resource=resource), 200
    return jsonify(msg='Resource not found'), 404

@resource_bp.route('/', methods=['GET'])
@jwt_required()
def all_resources():
    resources = get_all_resources(mongo)
    for r in resources:
        r['_id'] = str(r['_id'])
    return jsonify(resources=resources), 200
