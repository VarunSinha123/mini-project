# app.py
from flask import Flask, render_template
from flask_login import current_user
from extensions import db, migrate, login_manager
from models import User  # Import after extensions

def create_app():
    app = Flask(__name__)
    
    # Config
    app.config['SECRET_KEY'] = 'your-secret-key-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///college_management.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    
    # Login manager setup
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    with app.app_context():
        # Register blueprints
        from routes.auth import auth_bp
        from routes.student import student_bp
        from routes.faculty import faculty_bp
        from routes.admin import admin_bp
        
        app.register_blueprint(auth_bp, url_prefix='/auth')
        app.register_blueprint(student_bp, url_prefix='/student')
        app.register_blueprint(faculty_bp, url_prefix='/faculty')
        app.register_blueprint(admin_bp, url_prefix='/admin')
        
        # Create database tables
        db.create_all()
        
        @app.route('/')
        def home():
            return render_template('home.html')
            
        return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)