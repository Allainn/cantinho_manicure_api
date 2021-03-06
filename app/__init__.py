from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager
from flask_cors import CORS

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

    cors = CORS(app, resources={r"/api/v1/cidades/*": {"origins": "*"}})

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    login_manager.init_app(app)

    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    return app
