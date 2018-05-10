# coding=utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import configs

db = SQLAlchemy()

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(configs[config_name])
    #app.debug = configs[config_name].DEBUG

    app.jinja_env.variable_start_string = "{|"
    app.jinja_env.variable_end_string = "|}"

    #components initiation
    db.init_app(app)

    #blueprints initiation
    from .main import main
    app.register_blueprint(main)

    from .api import api_v1_0
    app.register_blueprint(api_v1_0, url_prefix='/api/v1_0')
    
    return app
