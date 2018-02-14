# coding=utf-8

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import configs

db = SQLAlchemy()

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(configs[config_name])

    #components initiation
    db.init_app(app)

    #blueprints initiation

    return app
