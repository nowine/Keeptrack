#coding=utf-8

import requests
from bs4 import BeautifulSoap
import pandas as pd

hist_quote_url = 'http://api.eastmoney.com/f10/lsjz'

common_header = {
    "Content-Type": "application/json; charset=utf-8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:48.0) Gecko/20100101 Firefox/48.0",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Host": "api.fund.eastmoney.com"
}

def crawl_hist_quotes(fund_code, page_size=10, pages=1, start_date=None, end_date=None):
    payload = dict()
    payload['startDate'] = start_date
    payload['endDate'] = end_date
    payload['fundCode'] = fund_code
    payload['pageSize'] = page_size

    frames = []

    if pages <= 0:
        # If pages == 0 means load all pages.
        pass
        return


    for page in range(pages):
        payload['pageIndex'] = page + 1
        r = request.get(hist_quote_url, headers=common_header, params=payload)
        if (r.status == 200):
            df = pd.DataFame(pd.read_json())


def _parse_hist_quotes(bs):
    pass


