def create_approval(mongo, approval_data):
    return mongo.db.approvals.insert_one(approval_data)

def get_approvals_by_event(mongo, event_id):
    return list(mongo.db.approvals.find({'event_id': event_id}))

def update_approval(mongo, approval_id, update_data):
    return mongo.db.approvals.update_one({'_id': approval_id}, {'$set': update_data})
