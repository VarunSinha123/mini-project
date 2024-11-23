# This file can remain empty or can be used for route registration
from flask import Blueprint

# Example of creating route blueprints
auth_bp = Blueprint('auth', __name__)
student_bp = Blueprint('student', __name__)
faculty_bp = Blueprint('faculty', __name__)
admin_bp = Blueprint('admin', __name__)
course_bp = Blueprint('course', __name__)
library_bp = Blueprint('library', __name__)