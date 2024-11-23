import uuid
from datetime import datetime

def generate_unique_id():
    """Generate a unique identifier"""
    return str(uuid.uuid4())

def format_date(date, format='%Y-%m-%d'):
    """Format date to specified string format"""
    return date.strftime(format) if date else None

def calculate_age(birthdate):
    """Calculate age from birthdate"""
    today = datetime.today()
    age = today.year - birthdate.year
    
    # Adjust age if birthday hasn't occurred this year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
    
    return age

def generate_student_id():
    """Generate a student ID with specific format"""
    prefix = datetime.now().strftime('%Y')
    unique_suffix = str(uuid.uuid4().hex)[:6].upper()
    return f"{prefix}-{unique_suffix}"

def sanitize_input(input_string):
    """Basic input sanitization"""
    # Remove potentially dangerous characters
    return re.sub(r'[<>&\'"()]', '', input_string)