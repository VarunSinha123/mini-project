import unittest
from models import db
from models.user import User
from models.student import Student
from models.course import Course
from models.faculty import Faculty
from datetime import date

class TestModels(unittest.TestCase):
    def setUp(self):
        # Configure test database
        db.create_all()

    def test_user_creation(self):
        user = User(username='testuser', email='test@example.com')
        user.set_password('password123')
        db.session.add(user)
        db.session.commit()

        self.assertIsNotNone(user.id)
        self.assertTrue(user.check_password('password123'))

    def test_student_creation(self):
        user = User(username='student', email='student@example.com')
        user.set_password('studentpass')
        
        student = Student(
            user=user,
            first_name='John',
            last_name='Doe',
            date_of_birth=date(2000, 1, 1),
            enrollment_date=date.today(),
            department='Computer Science'
        )
        
        db.session.add(user)
        db.session.add(student)
        db.session.commit()

        self.assertIsNotNone(student.id)
        self.assertEqual(student.first_name, 'John')

    def test_course_creation(self):
        faculty = Faculty(
            user=User(username='prof', email='prof@example.com'),
            first_name='Prof',
            last_name='Smith',
            department='Computer Science',
            designation='Assistant Professor'
        )

        course = Course(
            code='CS101',
            name='Introduction to Programming',
            description='Basic programming concepts',
            credits=3,
            department='Computer Science',
            semester='Fall 2024',
            instructor=faculty
        )

        db.session.add(faculty)
        db.session.add(course)
        db.session.commit()

        self.assertIsNotNone(course.id)
        self.assertEqual(course.code, 'CS101')

    def tearDown(self):
        # Clear database after tests
        db.session.remove()
        db.drop_all()

if __name__ == '__main__':
    unittest.main()