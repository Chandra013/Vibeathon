def log_action(mongo, log_data):
    return mongo.db.audit_logs.insert_one(log_data)

def get_logs_by_event(mongo, event_id):
    return list(mongo.db.audit_logs.find({'event_id': event_id}))
