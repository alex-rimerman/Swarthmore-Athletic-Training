from flask import Blueprint

# define a blueprint for views
# means we have a collection of routes/urls that are related to each other
# allows us to organize these in separate files
views = Blueprint('views', __name__)

# define a route for home page
@views.route('/') # defines url to where this next function takes us (function runs when we go to this url)
def home():
    return "<h1>Test</h1>"