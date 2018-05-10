#coding=utf-8

from flask import render_template, g, url_for
from . import main
from ..util import load_fund_hist

@main.route('/')
def index():
    table = load_fund_hist('000742', '20180502', '20180509')
    return render_template('test.html', hist_table=table)

@main.route('/fund_hist/<string:fund_code>/<string:sdate>/<string:edate>')
def fund_history(fund_hist, sdate, edate):
    return load_fund_hist(fund_code, sdate, edate)

