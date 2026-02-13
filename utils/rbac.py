def has_permission(user, action, resource):
    # Implement RBAC logic based on user role and action
    role = user['role']
    if role == 'Admin':
        return True
    # Add more rules as needed
    return False
