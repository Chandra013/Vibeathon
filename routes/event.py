
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.event import create_event, get_events_by_user
from extensions import mongo

event_bp = Blueprint('event', __name__, url_prefix='/api/events')

@event_bp.route('/search', methods=['GET'])
def search_events():
    query = {}
    name = request.args.get('name')
    venue_id = request.args.get('venue_id')
    status = request.args.get('status')
    if name:
        query['name'] = {'$regex': name, '$options': 'i'}
    if venue_id:
        query['venue_id'] = venue_id
    if status:
        query['status'] = status
    events = list(mongo.db.events.find(query))
    for e in events:
        e['_id'] = str(e['_id'])
    return jsonify(events=events), 200

@event_bp.route('/submit', methods=['POST'])
@jwt_required()
def submit_event():
    user = get_jwt_identity()
    data = request.get_json()
    data['coordinator'] = user['username']
    data['status'] = 'pending_hod'
    event_id = create_event(mongo, data)
    return jsonify(msg='Event submitted', event_id=str(event_id.inserted_id)), 201

@event_bp.route('/my', methods=['GET'])
@jwt_required()
def my_events():
    user = get_jwt_identity()
    events = get_events_by_user(mongo, user['username'])
    for e in events:
        e['_id'] = str(e['_id'])
    return jsonify(events=events), 200
