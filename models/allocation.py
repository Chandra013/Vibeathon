def create_allocation(mongo, allocation_data):
    return mongo.db.allocations.insert_one(allocation_data)

def get_allocations_by_event(mongo, event_id):
    return list(mongo.db.allocations.find({'event_id': event_id}))

def release_allocation(mongo, allocation_id):
    return mongo.db.allocations.delete_one({'_id': allocation_id})
