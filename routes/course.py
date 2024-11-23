from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from . import course_bp
from models.course import Course
from models.student import Student

@course_bp.route('/catalog')
@login_required
def catalog():
    courses = Course.query.all()
    return render_template('courses/course_list.html', courses=courses)

@course_bp.route('/<int:course_id>')
@login_required
def details(course_id):
    course = Course.query.get_or_404(course_id)
    return render_template('courses/course_details.html', course=course)

@course_bp.route('/enroll/<int:course_id>')
@login_required
def enroll(course_id):
    course = Course.query.get_or_404(course_id)
    student = Student.query.filter_by(user_id=current_user.id).first()
    
    if course not in student.courses:
        student.courses.append(course)
        db.session.commit()
    
    return redirect(url_for('course.details', course_id=course_id))