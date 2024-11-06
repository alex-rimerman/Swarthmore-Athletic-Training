from flask import Flask

def create_app():
    app = Flask(__name__) # initialize Flask app, __name__ is name of file that was ran
    app.config['SECRET_KEY'] = 'ksfjdkh shkd' # secret key for session management, would want this to be well generated/hidden in production

    return app