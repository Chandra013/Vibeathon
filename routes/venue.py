from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models.venue import add_venue, update_venue, get_venue, get_all_venues
from extensions import mongo

venue_bp = Blueprint('venue', __name__, url_prefix='/api/venues')

@venue_bp.route('/', methods=['POST'])
@jwt_required()
def add():
    data = request.get_json()
    add_venue(mongo, data)
    return jsonify(msg='Venue added'), 201

@venue_bp.route('/<venue_id>', methods=['PUT'])
@jwt_required()
def update(venue_id):
    data = request.get_json()
    update_venue(mongo, venue_id, data)
    return jsonify(msg='Venue updated'), 200

@venue_bp.route('/<venue_id>', methods=['GET'])
@jwt_required()
def get(venue_id):
    venue = get_venue(mongo, venue_id)
    if venue:
        venue['_id'] = str(venue['_id'])
        return jsonify(venue=venue), 200
    return jsonify(msg='Venue not found'), 404

@venue_bp.route('/', methods=['GET'])
@jwt_required()
def all_venues():
    venues = get_all_venues(mongo)
    for v in venues:
        v['_id'] = str(v['_id'])
    return jsonify(venues=venues), 200
