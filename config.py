# config.py
import os
from datetime import timedelta

class Config:
    # Secret key for sessions and CSRF protection
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here')

    # Database Configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///college_management.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Session Configuration
    PERMANENT_SESSION_LIFETIME = timedelta(days=1)
    SESSION_COOKIE_SECURE = os.environ.get('SESSION_COOKIE_SECURE', 'True').lower() in ['true', '1']
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'

    # File Upload Configuration
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file upload
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', 'uploads/')

    # Email Configuration
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 587))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'True').lower() in ['true', '1']
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    MAIL_DEFAULT_SENDER = os.environ.get('EMAIL_DEFAULT_SENDER', MAIL_USERNAME)

    # Logging Configuration
    LOGGING_LEVEL = os.environ.get('LOGGING_LEVEL', 'INFO').upper()