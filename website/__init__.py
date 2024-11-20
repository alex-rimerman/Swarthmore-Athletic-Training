from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy() #defines new database
DB_NAME = "users.db" #names database

def create_app():
    app = Flask(__name__) # initialize Flask app, __name__ is name of file that was ran
    app.config['SECRET_KEY'] = 'ksfjdkh shkd' # secret key for session management, would want this to be well generated/hidden in production
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' #stores database in website folder
    db.init_app(app) 

    from .views import views # import views blueprint from views.py
    from .auth import auth # import auth blueprint from auth.py

    # register views/auth blueprints with app, url_prefix is the url that will be used to access these routes
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/') 

    from .models import User, Note #makes sure that we load model.py before we load our database

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db.session.remove()

    return app

def create_database(app): #checks if database exists and creates one if database does not exist
    with app.app_context():
        if not path.exists('website/' + DB_NAME):
            db.create_all()
            print('Created Database!')