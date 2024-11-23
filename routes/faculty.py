from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from . import faculty_bp
from models.faculty import Faculty
from models.course import Course
from models.examination import Examination, ExaminationResult

@faculty_bp.route('/dashboard')
@login_required
def dashboard():
    faculty = Faculty.query.filter_by(user_id=current_user.id).first()
    courses = faculty.courses
    return render_template('faculty/dashboard.html', faculty=faculty, courses=courses)

@faculty_bp.route('/courses')
@login_required
def courses():
    faculty = Faculty.query.filter_by(user_id=current_user.id).first()
    return render_template('faculty/courses.html', courses=faculty.courses)

@faculty_bp.route('/course/<int:course_id>/students')
@login_required
def course_students(course_id):
    course = Course.query.get_or_404(course_id)
    return render_template('faculty/course_students.html', course=course)

@faculty_bp.route('/examinations/create', methods=['GET', 'POST'])
@login_required
def create_examination():
    if request.method == 'POST':
        # Logic to create examination
        pass
    return render_template('faculty/create_examination.html')