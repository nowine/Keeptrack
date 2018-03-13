# coding=utf-8

import tushare as ts
import pandas as pd

from ..models.dbmodels import Funds

def load_Fund_hist(fund_code, start_date=None, end_date=None):
    fund = Funds.query.filter_by(code=fund_code)
    if not fund:
        #get fund detail from Sina
        pass

    if end_date is None:
        #if end date is not provided, set it as today
        pass

    if start_date is None:
        #if Start date is not provided, set it as the fund's creation date
        pass

    # ts.get_nav_hist(xxxx) to get funds nav, save the date into db. USe Mongo
    # DB?? Or use SQL DB? Seems Mongo DB loads easier.



