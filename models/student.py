from extensions import db
from datetime import datetime

student_courses = db.Table('student_courses',
    db.Column('student_id', db.Integer, db.ForeignKey('students.id'), primary_key=True),
    db.Column('course_id', db.Integer, db.ForeignKey('courses.id'), primary_key=True)
)

class Student(db.Model):
    __tablename__ = 'students'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) 
    roll_number = db.Column(db.String(20), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    date_of_birth = db.Column(db.Date)
    admission_date = db.Column(db.DateTime, default=datetime.utcnow)
    department = db.Column(db.String(100))
    semester = db.Column(db.Integer)
    
    # Relationships
    user = db.relationship('User', backref=db.backref('student', uselist=False))
    courses = db.relationship('Course', secondary=student_courses, backref=db.backref('students', lazy='dynamic'))
    
    # Modified relationship to match ExaminationResult
    examination_results = db.relationship('ExaminationResult', back_populates='student', lazy=True)
    
    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __repr__(self):
        return f"<Student {self.roll_number}: {self.name}>"
    
    def to_dict(self):
        return {
            'id': self.id,
            'roll_number': self.roll_number,
            'name': self.name,
            'department': self.department,
            'semester': self.semester,
            'admission_date': self.admission_date.isoformat() if self.admission_date else None,
            'courses': [{'id': c.id, 'name': c.name} for c in self.courses]
        }