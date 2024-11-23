# routes/student.py
from flask import Blueprint, render_template, flash, redirect, url_for, request, jsonify
from flask_login import login_required, current_user
from models.student import Student
from models.course import Course
from models.examination import ExaminationResult
from extensions import db

# Create the blueprint
student_bp = Blueprint('student', __name__)

@student_bp.route('/dashboard')
@login_required
def dashboard():
    # Check if user is a student
    if current_user.role != 'student':
        flash('Access denied. Student privileges required.', 'danger')
        return redirect(url_for('home'))
    
    student = Student.query.filter_by(user_id=current_user.id).first()
    if not student:
        flash('Student profile not found.', 'danger')
        return redirect(url_for('home'))
        
    enrolled_courses = student.courses
    return render_template('students/dashboard.html', 
                         student=student, 
                         courses=enrolled_courses)

@student_bp.route('/profile')
@login_required
def profile():
    if current_user.role != 'student':
        flash('Access denied. Student privileges required.', 'danger')
        return redirect(url_for('home'))
        
    student = Student.query.filter_by(user_id=current_user.id).first()
    if not student:
        flash('Student profile not found.', 'danger')
        return redirect(url_for('home'))
        
    return render_template('students/profile.html', student=student)

@student_bp.route('/courses')
@login_required
def courses():
    if current_user.role != 'student':
        flash('Access denied. Student privileges required.', 'danger')
        return redirect(url_for('home'))
        
    student = Student.query.filter_by(user_id=current_user.id).first()
    if not student:
        flash('Student profile not found.', 'danger')
        return redirect(url_for('home'))
        
    return render_template('students/courses.html', courses=student.courses)

@student_bp.route('/results')
@login_required
def results():
    if current_user.role != 'student':
        flash('Access denied. Student privileges required.', 'danger')
        return redirect(url_for('home'))
        
    student = Student.query.filter_by(user_id=current_user.id).first()
    if not student:
        flash('Student profile not found.', 'danger')
        return redirect(url_for('home'))
        
    results = ExaminationResult.query.filter_by(student_id=student.id).all()
    return render_template('students/results.html', results=results)

# Add API endpoints if needed
@student_bp.route('/api/courses')
@login_required
def api_courses():
    if current_user.role != 'student':
        return jsonify({'error': 'Access denied'}), 403
        
    student = Student.query.filter_by(user_id=current_user.id).first()
    if not student:
        return jsonify({'error': 'Student not found'}), 404
        
    courses = [{
        'id': course.id,
        'name': course.name,
        'code': course.code,
        'instructor': course.instructor.name if course.instructor else None
    } for course in student.courses]
    
    return jsonify(courses)