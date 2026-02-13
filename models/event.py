def create_event(mongo, event_data):
    return mongo.db.events.insert_one(event_data)

def get_event(mongo, event_id):
    return mongo.db.events.find_one({'_id': event_id})

def update_event(mongo, event_id, update_data):
    return mongo.db.events.update_one({'_id': event_id}, {'$set': update_data})

def get_events_by_user(mongo, username):
    return list(mongo.db.events.find({'coordinator': username}))
