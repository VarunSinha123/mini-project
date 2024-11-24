from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from utils.forms import LoginForm, RegistrationForm, ForgotPasswordForm
from extensions import db
from models.user import User

auth_bp = Blueprint('auth', __name__)  # Correct Blueprint definition

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home.index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('home.index'))
        flash('Invalid username or password', 'error')
    
    return render_template('auth/login.html', form=form)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home.index'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            # Create the user instance with the role field
            user = User(
                username=form.username.data,
                email=form.email.data,
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                role=form.role.data  # Added role here
            )
            user.set_password(form.password.data)  # Hash the password
            
            db.session.add(user)
            db.session.commit()
            
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('auth.login'))
        except Exception as e:
            db.session.rollback()  # Rollback if something goes wrong
            flash('Registration failed. Please try again.', 'error')
            print(f"Error during registration: {e}")  # Log for debugging purposes
            
    return render_template('auth/register.html', form=form)



@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out successfully', 'info')
    return redirect(url_for('auth.login'))

@auth_bp.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    # Check the token and proceed to reset the password
    user = User.verify_reset_password_token(token)  # You'll need to define this method in your User model
    if not user:
        flash('Invalid or expired token', 'error')
        return redirect(url_for('auth.login'))
    
    form = ForgotPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset!', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('auth/reset_password.html', form=form)

@auth_bp.route('/forgot-password', methods=['GET', 'POST'])  # Corrected route
def forgot_password():
    form = ForgotPasswordForm()
    if form.validate_on_submit():
        # Add logic to send reset password email or link
        flash('If an account with that email exists, you will receive a reset link.', 'info')
        return redirect(url_for('auth.login'))
    return render_template('auth/forgot_password.html', form=form)
