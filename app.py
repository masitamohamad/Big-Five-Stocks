from flask import Flask, render_template, redirect, jsonify
from bs4 import BeautifulSoup as bs 
import requests

import numpy as np
import pandas as pd
import json

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from sqlalchemy import MetaData

###########################################################################################
# This function called `scrape_news` will scrape the latest news headlines from CNBC.com

def scrape_news():

    response = requests.get("https://www.cnbc.com/").text
    soup = bs(response, 'html.parser')
    news_parent = soup.find_all('div', class_='LatestNews-headline')
    news_headline = []
    for news in news_parent:
        news_headline.append(news.text)

    timestamp_parent = soup.find_all('div', class_='LatestNews-timestamp')
    news_timestamp = []
    for time in timestamp_parent:
        news_timestamp.append(time.text)
    
    joined_lists = [' '.join(x) for x in zip(news_timestamp,news_headline)]

    return joined_lists

###########################################################################################
# Database Setup - first thing's first, we need to connect to our stonks database
###########################################################################################
# Create an engine to connect to our database
engine = create_engine("sqlite:///stonks.sqlite")

meta = MetaData()
meta.reflect(bind=engine)

Stonks = meta.tables['stonks']
Fb = meta.tables['fb']
Aapl = meta.tables['aapl']
Amzn = meta.tables['amazn']
Ixic = meta.tables['ixic']
Googl = meta.tables['googl']
Msft = meta.tables['msft']
Year15 = meta.tables['year15']
Year16 = meta.tables['year16']
Year17 = meta.tables['year17']
Year18 = meta.tables['year18']
Year19 = meta.tables['year19']
Companies = meta.tables['companies']
Agg_stonks = meta.tables['agg_stonks']

###########################################################################################
# Flask Setup
###########################################################################################

app = Flask(__name__)

###########################################################################################
# Flask Routes
###########################################################################################
# Route to render index.html template

@app.route("/")
def home():
  
    news_data = scrape_news()
    return render_template("index.html", send_to_html=news_data)

# Let's try to return another route with the Stonks class/table in json format
@app.route("/api/v1.0/stonks")
def stonks():
    session = Session(engine)

    data = session.query(Stonks)

    session.close()

    name_date = []
    date = []
    year = []
    name = []
    open = []
    close = []
    high = []
    low = []
    volume = []
    for data in data:
        name_date.append(data.name_date)
        date.append(data.date)
        year.append(data.year)
        name.append(data.name)
        open.append(data.open)
        close.append(data.close)
        high.append(data.high)
        low.append(data.low)
        volume.append(data.volume)
    stonks_dict = {'name_date':name_date,
                    'date':date,
                    'year':year,
                    'name':name,
                    'open':open,
                    'close':close,
                    'high':high,
                    'low':low,
                    'volume':volume}
    
    return jsonify(stonks_dict)

@app.route("/api/v1.0/fb")
def fb():
    session = Session(engine)

    data = session.query(Fb).all()

    session.close()
    
    date = []
    year = []
    open = []
    close = []
    high = []
    low = []
    volume = []
    for data in data:
        date.append(data.date)
        year.append(data.year)
        open.append(data.open)
        close.append(data.close)
        high.append(data.high)
        low.append(data.low)
        volume.append(data.volume)
    fb_dict = {'date':date,
                    'year':year,
                    'open':open,
                    'close':close,
                    'high':high,
                    'low':low,
                    'volume':volume}

    return jsonify(fb_dict)

@app.route("/api/v1.0/aapl")
def aapl():
    session = Session(engine)

    data = session.query(Aapl).all()

    session.close()

    date = []
    year = []
    open = []
    close = []
    high = []
    low = []
    volume = []
    for data in data:
        date.append(data.date)
        year.append(data.year)
        open.append(data.open)
        close.append(data.close)
        high.append(data.high)
        low.append(data.low)
        volume.append(data.volume)
    aapl_dict = {'date':date,
                    'year':year,
                    'open':open,
                    'close':close,
                    'high':high,
                    'low':low,
                    'volume':volume}
    
    return jsonify(aapl_dict)

@app.route("/api/v1.0/amzn")
def amzn():
    session = Session(engine)

    data = session.query(Amzn).all()

    session.close()
    
    date = []
    year = []
    open = []
    close = []
    high = []
    low = []
    volume = []
    for data in data:
        date.append(data.date)
        year.append(data.year)
        open.append(data.open)
        close.append(data.close)
        high.append(data.high)
        low.append(data.low)
        volume.append(data.volume)
    amzn_dict = {'date':date,
                    'year':year,
                    'open':open,
                    'close':close,
                    'high':high,
                    'low':low,
                    'volume':volume}

    return jsonify(amzn_dict)

@app.route("/api/v1.0/ixic")
def ixic():
    session = Session(engine)

    data = session.query(Ixic).all()

    session.close()
    
    date = []
    year = []
    open = []
    close = []
    high = []
    low = []
    volume = []
    for data in data:
        date.append(data.date)
        year.append(data.year)
        open.append(data.open)
        close.append(data.close)
        high.append(data.high)
        low.append(data.low)
        volume.append(data.volume)
    ixic_dict = {'date':date,
                    'year':year,
                    'open':open,
                    'close':close,
                    'high':high,
                    'low':low,
                    'volume':volume}

    return jsonify(ixic_dict)

@app.route("/api/v1.0/googl")
def googl():
    session = Session(engine)

    data = session.query(Googl).all()

    session.close()
    
    date = []
    year = []
    open = []
    close = []
    high = []
    low = []
    volume = []
    for data in data:
        date.append(data.date)
        year.append(data.year)
        open.append(data.open)
        close.append(data.close)
        high.append(data.high)
        low.append(data.low)
        volume.append(data.volume)
    googl_dict = {'date':date,
                    'year':year,
                    'open':open,
                    'close':close,
                    'high':high,
                    'low':low,
                    'volume':volume}

    return jsonify(googl_dict)

@app.route("/api/v1.0/msft")
def msft():
    session = Session(engine)

    data = session.query(Msft).all()

    session.close()
    
    date = []
    year = []
    open = []
    close = []
    high = []
    low = []
    volume = []
    for data in data:
        date.append(data.date)
        year.append(data.year)
        open.append(data.open)
        close.append(data.close)
        high.append(data.high)
        low.append(data.low)
        volume.append(data.volume)
    msft_dict = {'date':date,
                    'year':year,
                    'open':open,
                    'close':close,
                    'high':high,
                    'low':low,
                    'volume':volume}

    return jsonify(msft_dict)

@app.route("/api/v1.0/companies")
def companies():
    session = Session(engine)

    data = session.query(Companies).all()

    session.close()
    
    ticker_symbol = []
    company = []
    founded = []
    revenue_2019 = []
    op_income_2019 = []
    net_income_2019 = []
    total_assets_2019 = []
    total_equity_2019 = []
    num_employees = []
    for data in data:
        ticker_symbol.append(data.ticker_symbol)
        company.append(data.company)
        founded.append(data.founded)
        revenue_2019.append(data.revenue_2019)
        op_income_2019.append(data.operating_income_2019)
        net_income_2019.append(data.net_income_2019)
        total_assets_2019.append(data.total_assets_2019)
        total_equity_2019.append(data.total_equity_2019)
        num_employees.append(data.num_employees)
    companies_dict = {'ticker_symbol':ticker_symbol,
                    'company':company,
                    'founded':founded,
                    'revenue_2019':revenue_2019,
                    'op_income_2019':op_income_2019,
                    'net_income_2019':net_income_2019,
                    'total_assets_2019':total_assets_2019,
                    'total_equity_2019':total_equity_2019,
                    'num_employees':num_employees}

    return jsonify(companies_dict)

@app.route("/api/v1.0/agg_stonks")
def agg_stonks():
    session = Session(engine)

    data = session.query(Agg_stonks).all()

    session.close()

    name_year = []
    year = []
    name = []
    avg_open = []
    avg_close = []
    avg_high = []
    avg_low = []
    total_volume = []
    for data in data:
        name_year.append(data.name_year)
        year.append(data.year)
        name.append(data.name)
        avg_open.append(data.avg_open)
        avg_close.append(data.avg_close)
        avg_high.append(data.avg_high)
        avg_low.append(data.avg_low)
        total_volume.append(data.total_volume)
    agg_stonks_dict = {'name_year':name_year,
                    'year':year,
                    'name':name,
                    'avg_open':avg_open,
                    'avg_close':avg_close,
                    'avg_high':avg_high,
                    'avg_low':avg_low,
                    'total_volume':total_volume}

    return jsonify(agg_stonks_dict)

@app.route("/api/v1.0/year15")
def year15():
    session = Session(engine)

    data = session.query(Year15).all()

    session.close()
    
    date = []
    name = []
    open = []
    close = []
    high = []
    low = []
    volume = []
    for data in data:
        date.append(data.date)
        name.append(data.name)
        open.append(data.open)
        close.append(data.close)
        high.append(data.high)
        low.append(data.low)
        volume.append(data.volume)
    year15_dict = {'date':date,
                    'name':name,
                    'open':open,
                    'close':close,
                    'high':high,
                    'low':low,
                    'volume':volume}

    return jsonify(year15_dict)

@app.route("/api/v1.0/year16")
def year16():
    session = Session(engine)

    data = session.query(Year16).all()

    session.close()
    
    date = []
    name = []
    open = []
    close = []
    high = []
    low = []
    volume = []
    for data in data:
        date.append(data.date)
        name.append(data.name)
        open.append(data.open)
        close.append(data.close)
        high.append(data.high)
        low.append(data.low)
        volume.append(data.volume)
    year16_dict = {'date':date,
                    'name':name,
                    'open':open,
                    'close':close,
                    'high':high,
                    'low':low,
                    'volume':volume}

    return jsonify(year16_dict)

@app.route("/api/v1.0/year17")
def year17():
    session = Session(engine)

    data = session.query(Year17).all()

    session.close()
    
    date = []
    name = []
    open = []
    close = []
    high = []
    low = []
    volume = []
    for data in data:
        date.append(data.date)
        name.append(data.name)
        open.append(data.open)
        close.append(data.close)
        high.append(data.high)
        low.append(data.low)
        volume.append(data.volume)
    year17_dict = {'date':date,
                    'name':name,
                    'open':open,
                    'close':close,
                    'high':high,
                    'low':low,
                    'volume':volume}

    return jsonify(year17_dict)

@app.route("/api/v1.0/year18")
def year18():
    session = Session(engine)

    data = session.query(Year18).all()

    session.close()
    
    date = []
    name = []
    open = []
    close = []
    high = []
    low = []
    volume = []
    for data in data:
        date.append(data.date)
        name.append(data.name)
        open.append(data.open)
        close.append(data.close)
        high.append(data.high)
        low.append(data.low)
        volume.append(data.volume)
    year18_dict = {'date':date,
                    'name':name,
                    'open':open,
                    'close':close,
                    'high':high,
                    'low':low,
                    'volume':volume}
    return jsonify(year18_dict)

@app.route("/api/v1.0/year19")
def year19():
    session = Session(engine)

    data = session.query(Year19).all()

    session.close()
    
    date = []
    name = []
    open = []
    close = []
    high = []
    low = []
    volume = []
    for data in data:
        date.append(data.date)
        name.append(data.name)
        open.append(data.open)
        close.append(data.close)
        high.append(data.high)
        low.append(data.low)
        volume.append(data.volume)
    year19_dict = {'date':date,
                    'name':name,
                    'open':open,
                    'close':close,
                    'high':high,
                    'low':low,
                    'volume':volume}

    return jsonify(year19_dict)

# Additional view routes

@app.route("/amznview")
def amznview():

    return render_template('amzn.html')

@app.route("/aaplview")
def aaplview():

    news_data = scrape_news()
    return render_template('aapl.html', send_to_html=news_data)

@app.route("/googlview")
def googlview():

    return render_template('googl.html')

@app.route("/msftview")
def msftview():

    return render_template('msft.html')


###########################################################################################
# Main Behavior
###########################################################################################

if __name__ == "__main__":
    app.run(debug=True)
