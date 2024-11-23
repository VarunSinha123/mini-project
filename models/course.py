from extensions import db  # Fixed import
from datetime import datetime

class Course(db.Model):
    __tablename__ = 'courses'
    
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    credits = db.Column(db.Integer)
    semester = db.Column(db.Integer)
    department = db.Column(db.String(50))
    instructor_id = db.Column(db.Integer, db.ForeignKey('faculty.id'))
    
    # Add relationship to Faculty
    instructor = db.relationship('Faculty', backref='courses')
    
    def __repr__(self):
        return f'<Course {self.code}: {self.name}>'

class CourseEnrollment(db.Model):
    __tablename__ = 'course_enrollments'
    
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))  # Changed to match Student tablename
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    enrollment_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='enrolled')
    
    # Add relationships
    student = db.relationship('Student', backref='enrollments')