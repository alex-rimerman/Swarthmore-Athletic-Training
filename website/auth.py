from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash #secures the password
from . import db
from flask_login import login_user, login_required, logout_user, current_user

# define a blueprint for views
# means we have a collection of routes/urls that are related to each other
# allows us to organize these in separate files
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST']) # defines url for where to login
def login():
    if request.method == 'POST': #post request sends information to server
        email = request.form.get('email')
        password = request.form.get('password')

        # check if user exists
        user = User.query.filter_by(email=email).first()
        if user: # if we found a user
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                if (user.role == "trainer"):
                    return redirect(url_for('views.trainerHome'))
                else:
                    return redirect(url_for('views.home')) #redirects the user to the home page after they sign in
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/logout') # defines url for where to logout
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST']) # defines url for where to sign up
def sign_up():
    if request.method == 'POST': #post request sends information to server
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        role = request.form.get('role')

        user = User.query.filter_by(email=email).first()
        
        # check for problems with signing up, if none, add user to DB
        if user:
            flash('Email already exists.', category='error') #flashes an error message on the screen
        elif len(email) < 4:
            flash('Email must be greater than 3 characters', category='error')
        elif len(first_name) < 2:
            flash('First Name must be greater than 1 character', category='error')
        elif len(last_name) < 2:
            flash('Last Name must be greater than 1 character', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match', category='error')
        elif len(password1) < 7:
            flash('Password must be greater than 6 character', category='error')
        elif len(role) < 1:
            flash('Role is incorrectly inputted', category='error')
        else:
            # add user to DB  
            new_user = User(email=email, first_name=first_name, last_name=last_name,
                            password=generate_password_hash(password1, method='pbkdf2:sha256'), role = role)
            db.session.add(new_user) #adds user to database
            db.session.commit() #updates the database
            login_user(new_user, remember=True)
            flash('Account created!', category='success') #flashes a success message on the screen
            if (role == "trainer"):
                return redirect(url_for('views.trainerHome'))
            else:
                return redirect(url_for('views.home'))
            
    return render_template("sign_up.html", user=current_user)
