from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from . import library_bp
from models.library import Book, Loan
from models.student import Student
from datetime import datetime

@library_bp.route('/catalog')
@login_required
def catalog():
    books = Book.query.all()
    return render_template('library/book_catalog.html', books=books)

@library_bp.route('/borrow/<int:book_id>')
@login_required
def borrow_book(book_id):
    book = Book.query.get_or_404(book_id)
    student = Student.query.filter_by(user_id=current_user.id).first()
    
    if book.available_copies > 0:
        loan = Loan(book=book, student=student)
        book.available_copies -= 1
        
        db.session.add(loan)
        db.session.commit()
        
        flash(f'Successfully borrowed {book.title}', 'success')
    else:
        flash('Book is not available', 'error')
    
    return redirect(url_for('library.catalog'))

@library_bp.route('/loans')
@login_required
def my_loans():
    student = Student.query.filter_by(user_id=current_user.id).first()
    loans = Loan.query.filter_by(student_id=student.id, return_date=None).all()
    return render_template('library/my_loans.html', loans=loans)