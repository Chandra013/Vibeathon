from app import mongo

def allocate_resources(event_id, resources):
    # Allocate resources for event
    for res in resources:
        mongo.db.allocations.insert_one({'event_id': event_id, 'resource_id': res['id'], 'quantity': res['quantity']})
    return True

def release_resources(event_id):
    mongo.db.allocations.delete_many({'event_id': event_id})
    return True
