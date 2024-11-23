from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from models import db
from models.user import User
from models.student import Student
from models.faculty import Faculty
from models.course import Course
from utils.decorators import admin_required

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/dashboard')
@login_required
@admin_required
def dashboard():
    try:
        stats = {
            'total_users': User.query.count(),
            'total_students': Student.query.count(),
            'total_faculty': Faculty.query.count(),
            'total_courses': Course.query.count()
        }
        return render_template('admin/dashboard.html', stats=stats)
    except Exception as e:
        flash('Error loading dashboard stats', 'error')
        return redirect(url_for('home.index'))

@admin_bp.route('/users')
@login_required
@admin_required
def user_management():
    try:
        users = User.query.all()
        return render_template('admin/user_management.html', users=users)
    except Exception as e:
        flash('Error loading user data', 'error')
        return redirect(url_for('admin.dashboard'))

@admin_bp.route('/users/create', methods=['GET', 'POST'])
@login_required
@admin_required
def create_user():
    form = UserCreationForm()
    if form.validate_on_submit():
        try:
            user = User(
                username=form.username.data,
                email=form.email.data,
                role=form.role.data
            )
            user.set_password(form.password.data)
            
            db.session.add(user)
            db.session.commit()
            
            flash('User created successfully', 'success')
            return redirect(url_for('admin.user_management'))
            
        except Exception as e:
            db.session.rollback()
            flash('Error creating user', 'error')
            
    return render_template('admin/create_user.html', form=form)