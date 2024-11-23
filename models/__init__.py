from extensions import db
# Import all models to ensure they are registered with SQLAlchemy
from .user import User
from .student import Student
from .faculty import Faculty
from .course import Course
from .examination import ExaminationResult
from .library import Book, Loan

__all__ = ['User', 'Student', 'Faculty', 'Course', 'ExaminationResult', 'Book', 'Loan']