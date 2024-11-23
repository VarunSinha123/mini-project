from functools import wraps
from flask import abort
from flask_login import current_user

def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            return abort(401)
        return func(*args, **kwargs)
    return decorated_function

def role_required(roles):
    def decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated or current_user.role not in roles:
                return abort(403)
            return func(*args, **kwargs)
        return decorated_function
    return decorator