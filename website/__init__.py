from flask import Flask

def create_app():
    app = Flask(__name__) # initialize Flask app, __name__ is name of file that was ran
    app.config['SECRET_KEY'] = 'ksfjdkh shkd' # secret key for session management, would want this to be well generated/hidden in production

    from .views import views # import views blueprint from views.py
    from .auth import auth # import auth blueprint from auth.py

    # register views/auth blueprints with app, url_prefix is the url that will be used to access these routes
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/') 

    return app