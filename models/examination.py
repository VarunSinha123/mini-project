from . import db

class Examination(db.Model):
    __tablename__ = 'examinations'
    
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    venue = db.Column(db.String(200), nullable=False)
    duration = db.Column(db.Integer, nullable=False)  # in minutes
    
    course = db.relationship('Course', back_populates='examinations')
    results = db.relationship('ExaminationResult', back_populates='examination')
    
    def __repr__(self):
        return f'<Examination for {self.course.name} on {self.date}>'

class ExaminationResult(db.Model):
    __tablename__ = 'examination_results'
    
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    examination_id = db.Column(db.Integer, db.ForeignKey('examinations.id'), nullable=False)
    marks_obtained = db.Column(db.Float, nullable=False)
    total_marks = db.Column(db.Float, nullable=False)
    grade = db.Column(db.String(2), nullable=False)
    
    student = db.relationship('Student')
    examination = db.relationship('Examination', back_populates='results')
    
    def __repr__(self):
        return f'<Result for {self.student.first_name} in {self.examination.course.name}>'