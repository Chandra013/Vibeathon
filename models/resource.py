def add_resource(mongo, resource_data):
    return mongo.db.resources.insert_one(resource_data)

def update_resource(mongo, resource_id, update_data):
    return mongo.db.resources.update_one({'_id': resource_id}, {'$set': update_data})

def get_resource(mongo, resource_id):
    return mongo.db.resources.find_one({'_id': resource_id})

def get_all_resources(mongo):
    return list(mongo.db.resources.find())
