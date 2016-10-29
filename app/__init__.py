from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
from .models import db


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)

    from .main.views import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
