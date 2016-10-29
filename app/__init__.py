from flask import Flask

def create_app():
    flask = Flask(__name__)

    from .main.views import main as main_blueprint
    flask.register_blueprint(main_blueprint)
    return flask
