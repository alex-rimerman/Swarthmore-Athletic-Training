from flask import Blueprint, render_template

# define a blueprint for views
# means we have a collection of routes/urls that are related to each other
# allows us to organize these in separate files
auth = Blueprint('auth', __name__)


@auth.route('/login') # defines url for where to login
def login():
    return render_template("login.html")

@auth.route('/logout') # defines url for where to logout
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up') # defines url for where to sign up
def sign_up():
    return render_template("sign_up.html")
