# coding=utf-8

import tushare as ts
import pandas as pd

def load_fund_hist(fund_code, start_date=None, end_date=None):
    #fund = Funds.query.filter_by(code=fund_code)
    #if not fund:
        #get fund detail from Sina
        #pass

    df = ts.get_nav_history(fund_code, start_date, end_date)
    return df.to_html()



