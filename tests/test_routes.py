import unittest
from flask import Flask
from flask_login import login_user, current_user
from routes import auth_bp, student_bp
from models.user import User
from models.student import Student

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False
        
        self.app.register_blueprint(auth_bp)
        self.app.register_blueprint(student_bp)

        with self.app.app_context():
            db.create_all()

    def test_login_route(self):
        with self.app.test_client() as client:
            response = client.post('/login', data={
                'username': 'testuser',
                'password': 'password123'
            })
            self.assertEqual(response.status_code, 200)

    def test_student_dashboard(self):
        with self.app.test_client() as client:
            # Simulate authenticated user
            user = User(username='student', email='student@example.com')
            student = Student(user=user)
            
            with self.app.test_request_context():
                login_user(user)
                response = client.get('/student/dashboard')
                self.assertEqual(response.status_code, 200)

    def test_unauthorized_access(self):
        with self.app.test_client() as client:
            response = client.get('/student/dashboard')
            self.assertEqual(response.status_code, 401)

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

if __name__ == '__main__':
    unittest.main()