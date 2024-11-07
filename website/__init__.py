from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "users.db"

def create_app():
    app = Flask(__name__) # initialize Flask app, __name__ is name of file that was ran
    app.config['SECRET_KEY'] = 'ksfjdkh shkd' # secret key for session management, would want this to be well generated/hidden in production
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views # import views blueprint from views.py
    from .auth import auth # import auth blueprint from auth.py

    # register views/auth blueprints with app, url_prefix is the url that will be used to access these routes
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/') 

    from .models import User, Note

    create_database(app)

    return app

def create_database(app):
    with app.app_context():
        if not path.exists('website/' + DB_NAME):
            db.create_all()
            print('Created Database!')