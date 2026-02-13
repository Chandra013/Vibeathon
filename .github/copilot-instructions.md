# Copilot Instructions for Institutional Event Resource Management System

## Project Architecture
- **Backend:** Flask (Python), modularized with Blueprints in `routes/`
- **Frontend:** Jinja2 HTML templates in `templates/`, Bootstrap for styling, static assets in `static/`
- **Database:** MongoDB, models in `models/`
- **Business Logic:** `services/` (e.g., conflict detection)
- **Utilities:** `utils/` (RBAC, allocation helpers)
- **Environment:** Config via `.env` (see sample)

## Key Developer Workflows
- Install dependencies: `pip install -r requirements.txt`
- Set up MongoDB and `.env` file
- Run server: `python app.py`
- All API endpoints are under `/api/`
- Use JWT for authentication (see `/api/auth/login`)
- Use Postman or similar for API testing

## Project Conventions
- Strict MVC separation: models, routes, services, utils
- Role-based access enforced in endpoints and UI
- Approval workflow: Coordinator → HOD → Dean → Head
- No resource/venue overbooking; all allocations validated by conflict engine
- All changes and event completions logged in `audit_logs`
- Occupancy visibility is role-specific (see `routes/occupancy.py`)

## Integration Points
- MongoDB collections: users, events, approvals, venues, resources, allocations, audit_logs
- JWT tokens required for all protected endpoints
- Admin endpoints for venue/resource management: `/api/admin/`

## Examples
- See `services/conflict_engine.py` for conflict detection logic
- See `utils/rbac.py` for permission checks
- See `routes/approval.py` for multi-level approval
- See `README.md` for sample documents and setup

## Special Notes
- Do not bypass approval order or capacity constraints in code
- All resource releases must update allocations and audit logs
- Use only Flask, Bootstrap, and MongoDB (no React)
- All code must be modular and production-style
