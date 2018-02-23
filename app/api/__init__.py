# coding=utf-8

from flask import Blueprint
from flask_restful import Api
from ..resources.v1_0 import FundResource

api_v1_0 = Blueprint('api_v1_0', 'api_v1_0')

api = Api(api_v1_0)
api.add_resource(FundResource, '/funds/<string:code>')

from . import views
