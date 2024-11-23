# routes/faculty.py
from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from models.course import Course
from models.examination import ExaminationResult  # Removed Examination as it doesn't exist
from models.student import Student
from models.faculty import Faculty

faculty_bp = Blueprint('faculty', __name__)

@faculty_bp.route('/dashboard')
@login_required
def dashboard():
    if current_user.role != 'faculty':
        flash('Access denied. Faculty only area.', 'danger')
        return redirect(url_for('home'))
        
    faculty = Faculty.query.filter_by(user_id=current_user.id).first()
    if not faculty:
        flash('Faculty profile not found.', 'danger')
        return redirect(url_for('home'))
        
    # Get courses taught by this faculty
    courses = Course.query.filter_by(instructor_id=faculty.id).all()
    
    return render_template('faculty/dashboard.html', 
                         faculty=faculty, 
                         courses=courses)

@faculty_bp.route('/courses')
@login_required
def courses():
    if current_user.role != 'faculty':
        flash('Access denied. Faculty only area.', 'danger')
        return redirect(url_for('home'))
        
    faculty = Faculty.query.filter_by(user_id=current_user.id).first()
    courses = Course.query.filter_by(instructor_id=faculty.id).all()
    
    return render_template('faculty/courses.html', courses=courses)

@faculty_bp.route('/examination_results')
@login_required
def examination_results():
    if current_user.role != 'faculty':
        flash('Access denied. Faculty only area.', 'danger')
        return redirect(url_for('home'))
        
    faculty = Faculty.query.filter_by(user_id=current_user.id).first()
    courses = Course.query.filter_by(instructor_id=faculty.id).all()
    
    # Get all examination results for courses taught by this faculty
    results = []
    for course in courses:
        course_results = ExaminationResult.query.filter_by(course_id=course.id).all()
        results.extend(course_results)
    
    return render_template('faculty/examination_results.html', 
                         results=results)

@faculty_bp.route('/add_result', methods=['GET', 'POST'])
@login_required
def add_result():
    if current_user.role != 'faculty':
        flash('Access denied. Faculty only area.', 'danger')
        return redirect(url_for('home'))
        
    if request.method == 'POST':
        student_id = request.form.get('student_id')
        course_id = request.form.get('course_id')
        marks = request.form.get('marks')
        
        # Input validation
        if not all([student_id, course_id, marks]):
            flash('All fields are required', 'danger')
            return redirect(url_for('faculty.add_result'))
            
        try:
            marks = float(marks)
            
            # Calculate grade based on marks
            grade = calculate_grade(marks)
            
            result = ExaminationResult(
                student_id=student_id,
                course_id=course_id,
                marks=marks,
                grade=grade
            )
            
            db.session.add(result)
            db.session.commit()
            
            flash('Examination result added successfully', 'success')
            return redirect(url_for('faculty.examination_results'))
            
        except ValueError:
            flash('Invalid marks value', 'danger')
            return redirect(url_for('faculty.add_result'))
            
    faculty = Faculty.query.filter_by(user_id=current_user.id).first()
    courses = Course.query.filter_by(instructor_id=faculty.id).all()
    students = Student.query.all()
    
    return render_template('faculty/add_result.html',
                        courses=courses,
                        students=students)

def calculate_grade(marks):
    if marks >= 90:
        return 'A+'
    elif marks >= 80:
        return 'A'
    elif marks >= 70:
        return 'B+'
    elif marks >= 60:
        return 'B'
    elif marks >= 50:
        return 'C'
    else:
        return 'F'