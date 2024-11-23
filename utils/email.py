# utils/email.py

from flask_mail import Message
from extensions import mail  # Assuming `mail` is initialized in extensions.py
from flask import current_app

def send_email(subject, recipient, body, sender=None, html_body=None):
    """
    Send an email using Flask-Mail.
    
    Args:
        subject (str): The subject of the email.
        recipient (str): The recipient's email address.
        body (str): The plain-text body of the email.
        sender (str, optional): The sender's email address. Defaults to app's MAIL_DEFAULT_SENDER.
        html_body (str, optional): The HTML body of the email. Defaults to None.
    """
    if sender is None:
        sender = current_app.config.get("MAIL_DEFAULT_SENDER", "no-reply@example.com")

    msg = Message(subject, sender=sender, recipients=[recipient])
    msg.body = body
    if html_body:
        msg.html = html_body

    try:
        mail.send(msg)
        current_app.logger.info(f"Email sent to {recipient}")
    except Exception as e:
        current_app.logger.error(f"Failed to send email to {recipient}: {str(e)}")
        raise e

def send_reset_password_email(user_email, token):
    """
    Send an email with a password reset link.
    
    Args:
        user_email (str): The email address of the user.
        token (str): The password reset token.
    """
    subject = "Reset Your Password"
    body = f"Click the link to reset your password: /reset_password/{token}"
    send_email(subject, user_email, body)
