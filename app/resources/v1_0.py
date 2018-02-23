# coding=utf-8

from flask import jsonify
from flask_restful import Resource
from ..models.dbmodels import Funds

class FundResource(Resource):
    def get(self, code):
        print(code)
        fund = Funds.query.filter_by(code=code).first()
        if fund:
            return jsonify(fund.to_dict())
        
class Test(Resource):
    def get(self):
        return {'hello':'world'}
