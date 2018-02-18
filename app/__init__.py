# coding=utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from config import configs

db = SQLAlchemy()
api = Api()

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(configs[config_name])

    #components initiation
    db.init_app(app)
    api.init_app(app)

    #simple restful registration
    from .resources import v1_0
    api.add_resource(v1_0.FundResource, '/api/v1_0/funds/<string:code>' )

    #blueprints initiation

    return app
