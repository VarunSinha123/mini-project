from extensions import db
from datetime import datetime

class ExaminationResult(db.Model):
    __tablename__ = 'examination_results'
    
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    exam_date = db.Column(db.DateTime, default=datetime.utcnow)
    marks = db.Column(db.Float, nullable=False)
    grade = db.Column(db.String(2))
    
    # Relationships
    student = db.relationship('Student', back_populates='examination_results')
    course = db.relationship('Course', backref='examination_results')
    
    def __repr__(self):
        return f'<ExaminationResult {self.student_id} - {self.course_id}>'