from flask import Blueprint, render_template, request, flash

# define a blueprint for views
# means we have a collection of routes/urls that are related to each other
# allows us to organize these in separate files
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST']) # defines url for where to login
def login():
    data = request.form
    print(data)
    return render_template("login.html")

@auth.route('/logout') # defines url for where to logout
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST']) # defines url for where to sign up
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 4:
            flash('Email must be greater than 3 characters', category='error')
        elif len(firstName) < 2:
            flash('First Name must be greater than 1 character', category='error')
        elif len(lastName) < 2:
            flash('Last Name must be greater than 1 character', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match', category='error')
        elif len(password1) < 7:
            flash('Password must be greater than 6 character', category='error')
        else:
            flash('Account created!', category='success')
            # add user to DB    
            

   
    return render_template("sign_up.html")
