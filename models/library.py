from . import db
from datetime import datetime, timedelta

class Book(db.Model):
    __tablename__ = 'books'
    
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(20), unique=True, nullable=False)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    total_copies = db.Column(db.Integer, nullable=False)
    available_copies = db.Column(db.Integer, nullable=False)
    
    loans = db.relationship('Loan', back_populates='book')
    
    def __repr__(self):
        return f'<Book {self.title} by {self.author}>'

class Loan(db.Model):
    __tablename__ = 'book_loans'
    
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    loan_date = db.Column(db.DateTime, default=datetime.utcnow)
    due_date = db.Column(db.DateTime, nullable=False)
    return_date = db.Column(db.DateTime)
    
    book = db.relationship('Book', back_populates='loans')
    student = db.relationship('Student')
    
    def __init__(self, book, student, loan_date=None):
        self.book = book
        self.student = student
        self.loan_date = loan_date or datetime.utcnow()
        self.due_date = self.loan_date + timedelta(days=14)
    
    def is_overdue(self):
        return datetime.utcnow() > self.due_date and not self.return_date
    
    def __repr__(self):
        return f'<Loan of {self.book.title} by {self.student.first_name}>'