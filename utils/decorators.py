from functools import wraps
from flask import flash, redirect, url_for
from flask_login import current_user

def role_required(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated or current_user.role != role:
                flash(f'Access denied. {role.capitalize()} privileges required.', 'danger')
                return redirect(url_for('home.index'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def admin_required(f):
    return role_required('admin')(f)

def faculty_required(f):
    return role_required('faculty')(f)

def student_required(f):
    return role_required('student')(f)