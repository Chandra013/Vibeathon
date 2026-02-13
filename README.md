# Institutional Event Resource Management System

## Overview
A Flask-based system to manage college fest events, resources, and venues with strict approval workflows and real-time occupancy tracking.

## Folder Structure
- `models/` - MongoDB data models
- `routes/` - Flask Blueprints for API endpoints
- `services/` - Business logic (e.g., conflict detection)
- `utils/` - Utility functions (RBAC, allocation)
- `templates/` - HTML (Jinja2) templates
- `static/` - CSS and static assets
- `.env` - Environment variables
- `requirements.txt` - Python dependencies

## MongoDB Collections & Sample Documents

### users
```json
{
  "username": "coordinator1",
  "password": "<hashed>",
  "role": "Event Coordinator",
  "department": "CSE",
  "school": "Engineering"
}
```
### events
```json
{
  "name": "Tech Fest",
  "coordinator": "coordinator1",
  "venue_id": "...",
  "start_time": "2026-03-01T10:00:00",
  "end_time": "2026-03-01T18:00:00",
  "status": "pending_hod"
}
```
### approvals
```json
{
  "event_id": "...",
  "approver": "hod1",
  "role": "HOD",
  "action": "approved",
  "reason": "Looks good"
}
```
### venues
```json
{
  "name": "Main Auditorium",
  "capacity": 500,
  "type": "auditorium"
}
```
### resources
```json
{
  "name": "Projector",
  "type": "equipment",
  "quantity": 10
}
```
### allocations
```json
{
  "event_id": "...",
  "resource_id": "...",
  "quantity": 2
}
```
### audit_logs
```json
{
  "event_id": "...",
  "action": "completed",
  "timestamp": "2026-03-01T19:00:00",
  "user": "coordinator1"
}
```

## Setup Instructions
1. Install Python 3.10+ and MongoDB
2. `pip install -r requirements.txt`
3. Set up `.env` with your secrets and MongoDB URI
4. Start MongoDB server
5. `python app.py`
6. Access at `http://localhost:5000`

## API Endpoints
- `/api/auth/login` - JWT login
- `/api/events/submit` - Submit event
- `/api/events/my` - My events
- `/api/approvals/<event_id>` - Approve/reject
- `/api/venues/` - Venue CRUD
- `/api/resources/` - Resource CRUD
- `/api/occupancy/` - Occupancy by role
- `/api/admin/venue` - Admin venue management
- `/api/admin/resource` - Admin resource management

## Allocation & Role Visibility Logic
- Approval: Coordinator → HOD → Dean → Head
- No overbooking or exceeding capacity
- Conflict engine returns minimal conflicting set
- Occupancy visibility: Coordinator (own), HOD (department), Dean (school), Head/Admin (all)
- On event completion: explicit resource release, audit log entry
