from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from . import auth_bp
from models import db
from models.user import User
from utils.forms import LoginForm, RegistrationForm

# Login route
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home.index'))  # Redirect to home if already logged in
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):  # Check if user exists and password matches
            login_user(user)
            return redirect(url_for('home.index'))  # Redirect to home page after login
        else:
            flash('Invalid username or password', 'error')  # Show error if credentials are incorrect
    
    return render_template('auth/login.html', form=form)

# Registration route
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():  # Process the form data after it's submitted and valid
        flash('Registration successful! You can now log in.', 'success')
        user = User(
            username=form.username.data, 
            email=form.email.data,
            role=form.role.data
        )
        user.set_password(form.password.data)  # Hash the password using the set_password method
        
        db.session.add(user)
        db.session.commit()  # Save the user to the database
        
        flash('Registration successful', 'success')  # Show success message
        return redirect(url_for('auth_bp.login'))  # Redirect to login page
    
    return render_template('auth/register.html', form=form)

# Logout route
@auth_bp.route('/logout')
@login_required  # Ensures that only logged-in users can access this route
def logout():
    logout_user()  # Logs out the user
    flash('You have been logged out', 'info')  # Show logout success message
    return redirect(url_for('auth_bp.login'))  # Redirect to login page

# Forgot password route
@auth_bp.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    # Logic for handling forgot password, such as sending a reset link
    # This could involve generating a token and sending it via email to the user
    return render_template('auth/forgot_password.html')
