import re
from email_validator import validate_email as email_validate, EmailNotValidError

def validate_email(email):
    try:
        # Validate and get info
        valid = email_validate(email)
        return True
    except EmailNotValidError:
        return False

def validate_password(password):
    # Password requirements:
    # - At least 8 characters
    # - Contains at least one uppercase letter
    # - Contains at least one lowercase letter
    # - Contains at least one number
    # - Contains at least one special character
    if len(password) < 8:
        return False
    
    if not re.search(r'[A-Z]', password):
        return False
    
    if not re.search(r'[a-z]', password):
        return False
    
    if not re.search(r'\d', password):
        return False
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    
    return True

def validate_phone_number(phone):
    # Basic phone number validation (adjust regex as needed)
    phone_pattern = r'^\+?1?\d{10,14}$'
    return re.match(phone_pattern, phone) is not None