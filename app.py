import os
from flask import Flask
from dotenv import load_dotenv
from extensions import mongo, jwt, cors

load_dotenv()

app = Flask(__name__)
app.config['MONGO_URI'] = os.getenv('MONGO_URI')
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

cors.init_app(app)
jwt.init_app(app)
mongo.init_app(app)

from routes.auth import auth_bp
from routes.event import event_bp
from routes.approval import approval_bp
from routes.venue import venue_bp
from routes.resource import resource_bp
from routes.occupancy import occupancy_bp
from routes.admin import admin_bp

app.register_blueprint(auth_bp)
app.register_blueprint(event_bp)
app.register_blueprint(approval_bp)
app.register_blueprint(venue_bp)
app.register_blueprint(resource_bp)
app.register_blueprint(occupancy_bp)
app.register_blueprint(admin_bp)

if __name__ == '__main__':
    # --- Frontend (Jinja2) routes ---
    from flask import render_template, redirect, url_for, session, request, flash

    @app.route('/')
    def index():
        return render_template('landing.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login_page():
        if request.method == 'POST':
            # This form posts to /api/auth/login via JS or fetch
            pass
        return render_template('login.html')

    @app.route('/dashboard')
    def dashboard():
        # Placeholder: In production, fetch user info from session/JWT
        user = {'username': 'demo', 'role': 'Event Coordinator'}
        return render_template('dashboard.html', user=user)

    @app.route('/event/submit', methods=['GET'])
    def event_submit():
        return render_template('event_submit.html')

    @app.route('/approvals', methods=['GET'])
    def approvals():
        return render_template('approvals.html')

    @app.route('/calendar', methods=['GET'])
    def calendar_view():
        return render_template('calendar.html')

    @app.route('/admin', methods=['GET'])
    def admin_panel():
        return render_template('admin_panel.html')

    @app.route('/reset_password', methods=['GET'])
    def reset_password_view():
        return render_template('reset_password.html')

    @app.route('/audit_logs', methods=['GET'])
    def audit_logs_view():
        return render_template('audit_logs.html')

    @app.route('/search', methods=['GET'])
    def search_view():
        return render_template('search.html')

    @app.route('/charts', methods=['GET'])
    def charts_view():
        return render_template('charts.html')

    app.run(debug=True, use_reloader=False)
import os
from flask import Flask
from dotenv import load_dotenv
from extensions import mongo, jwt, cors

load_dotenv()

app = Flask(__name__)
app.config['MONGO_URI'] = os.getenv('MONGO_URI')
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

cors.init_app(app)
jwt.init_app(app)
mongo.init_app(app)

from routes.auth import auth_bp
from routes.event import event_bp
from routes.approval import approval_bp
from routes.venue import venue_bp
from routes.resource import resource_bp
from routes.occupancy import occupancy_bp
from routes.admin import admin_bp

app.register_blueprint(auth_bp)
app.register_blueprint(event_bp)
app.register_blueprint(approval_bp)
app.register_blueprint(venue_bp)
app.register_blueprint(resource_bp)
app.register_blueprint(occupancy_bp)
app.register_blueprint(admin_bp)

if __name__ == '__main__':
    # --- Frontend (Jinja2) routes ---
    from flask import render_template, redirect, url_for, session, request, flash

    @app.route('/')
    def index():
        return render_template('landing.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login_page():
        if request.method == 'POST':
            # This form posts to /api/auth/login via JS or fetch
            pass
        return render_template('login.html')

    @app.route('/dashboard')
    def dashboard():
        # Placeholder: In production, fetch user info from session/JWT
        user = {'username': 'demo', 'role': 'Event Coordinator'}
        return render_template('dashboard.html', user=user)

    @app.route('/event/submit', methods=['GET'])
    def event_submit():
        return render_template('event_submit.html')

    @app.route('/approvals', methods=['GET'])
    def approvals():
        return render_template('approvals.html')


    @app.route('/calendar', methods=['GET'])
    def calendar_view():
        return render_template('calendar.html')

    @app.route('/admin', methods=['GET'])
    def admin_panel():
        return render_template('admin_panel.html')

    app.run(debug=True, use_reloader=False)
