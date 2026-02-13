def add_venue(mongo, venue_data):
    return mongo.db.venues.insert_one(venue_data)

def update_venue(mongo, venue_id, update_data):
    return mongo.db.venues.update_one({'_id': venue_id}, {'$set': update_data})

def get_venue(mongo, venue_id):
    return mongo.db.venues.find_one({'_id': venue_id})

def get_all_venues(mongo):
    return list(mongo.db.venues.find())
