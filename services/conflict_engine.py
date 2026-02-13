from app import mongo
from datetime import datetime

def detect_conflicts(event_data):
    # Check for venue overbooking and time-slot collision
    venue_id = event_data['venue_id']
    start = datetime.fromisoformat(event_data['start_time'])
    end = datetime.fromisoformat(event_data['end_time'])
    conflicts = []
    overlapping_events = mongo.db.events.find({
        'venue_id': venue_id,
        '$or': [
            {'start_time': {'$lt': event_data['end_time'], '$gte': event_data['start_time']}},
            {'end_time': {'$gt': event_data['start_time'], '$lte': event_data['end_time']}}
        ]
    })
    for e in overlapping_events:
        conflicts.append({'event_id': str(e['_id']), 'name': e.get('name')})
    # Check for resource shortage
    # ... (implement resource checks as needed)
    if conflicts:
        return {
            'status': 'rejected',
            'reason': 'Venue/time conflict',
            'conflicting_entities': conflicts
        }
    return {'status': 'ok'}
