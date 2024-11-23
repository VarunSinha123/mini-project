from flask import render_template, request, redirect, url_for
from flask_login import login_required
from . import admin_bp
from models import db
from models.user import User
from models.student import Student
from models.faculty import Faculty
from models.course import Course

@admin_bp.route('/dashboard')
@login_required
def dashboard():
    stats = {
        'total_users': User.query.count(),
        'total_students': Student.query.count(),
        'total_faculty': Faculty.query.count(),
        'total_courses': Course.query.count()
    }
    return render_template('admin/dashboard.html', stats=stats)

@admin_bp.route('/users')
@login_required
def user_management():
    users = User.query.all()
    return render_template('admin/user_management.html', users=users)

@admin_bp.route('/users/create', methods=['GET', 'POST'])
@login_required
def create_user():
    if request.method == 'POST':
        # User creation logic
        pass
    return render_template('admin/create_user.html')