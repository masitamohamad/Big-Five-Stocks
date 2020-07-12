from flask import Flask, render_template, redirect, jsonify
from bs4 import BeautifulSoup as bs 
import requests

import numpy as np

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

# # Map the tables contained in the database
# Base = automap_base()
# # Reflect the tables into python
# Base.prepare(engine,reflect=True)

# # Make our python classes based on the SQLite database
# Stonks = Base.classes.stonks
# Amzn = Base.classes.amazn
# Fb = Base.classes.fb
# Aapl = Base.classes.aapl
# Ixic = Base.classes.ixic
# Googl = Base.classes.googl
# Msft = Base.classes.msft
# Year15 = Base.classes.year15
# Year16 = Base.classes.year16
# Year17 = Base.classes.year17
# Year18 = Base.classes.year18
# Year19 = Base.classes.year19
# Companies = Base.classes.companies
# Agg_stonks = Base.classes.agg_stonks

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
# Route to render index.html template using data from Mongo

@app.route("/")
def home():
  
    news_data = scrape_news()
    return render_template("index.html", send_to_html=news_data)
    # NOTE: is it possible to return more than one thing e.g. a print out of all our available routes?


# Let's try to return another route with the Stonks class/table in json format
@app.route("/api/v1.0/stonks")
def stonks():
    session = Session(engine)

    #results = session.query(Stonks).all()
    #results = session.query(Stonks.date,Stonks.year,Stonks.name,Stonks.open,Stonks.close,Stonks.high,Stonks.low,Stonks.volume).all()
    #results = session.query(Stonks['date'],Stonks['year'],Stonksname,Stonks.open,Stonks.close,Stonks.high,Stonks.low,Stonks.volume).all()

    data = session.query(Stonks)

    session.close()

    # Extract results into a dictionary format
    # stonks_results = []
    # for date, year, name, open, close, high, low, volume in results:
    #     stonks_dict = {}
    #     stonks_dict['date']=date
    #     stonks_dict['year']=year
    #     stonks_dict['name']=name
    #     stonks_dict['open']=open
    #     stonks_dict['close']=close
    #     stonks_dict['high']=high
    #     stonks_dict['low']=low
    #     stonks_dict['volume']=volume

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
    
    # Extract all of the individual results and store them in a list
    # stonk_results = list(np.ravel(results))
    
    # return jsonify(stonk_results)
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

    # Extract all of the individual results and store them in a list
    # fb_results = list(np.ravel(results))
    # return jsonify(fb_results)
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
    
    # Extract all of the individual results and store them in a list
    # aapl_results = list(np.ravel(results))
    # return jsonify(aapl_results)
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

    # Extract all of the individual results and store them in a list
    # amzn_results = list(np.ravel(results))
    # return jsonify(amzn_results)
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

    # Extract all of the individual results and store them in a list
    # ixic_results = list(np.ravel(results))
    # return jsonify(ixic_results)
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

    # Extract all of the individual results and store them in a list
    # googl_results = list(np.ravel(results))
    # return jsonify(googl_results)
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

    # Extract all of the individual results and store them in a list
    # msft_results = list(np.ravel(results))
    # return jsonify(msft_results)
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

    # Extract all of the individual results and store them in a list
    # companies_results = list(np.ravel(results))
    # return jsonify(companies_results)
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

    
    # Extract all of the individual results and store them in a list
    # agg_results = list(np.ravel(results))
    # return jsonify(agg_results)
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

    # Extract all of the individual results and store them in a list
    # year15_results = list(np.ravel(results))
    # return jsonify(year15_results)
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

    # Extract all of the individual results and store them in a list
    # year16_results = list(np.ravel(results))
    # return jsonify(year16_results)
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

    # Extract all of the individual results and store them in a list
    # year17_results = list(np.ravel(results))
    # return jsonify(year17_results)
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
    # Extract all of the individual results and store them in a list
    # year18_results = list(np.ravel(results))
    # return jsonify(year18_results)
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

    # Extract all of the individual results and store them in a list
    # year19_results = list(np.ravel(results))
    # return jsonify(year19_results)
    return jsonify(year19_dict)


###########################################################################################
# Main Behavior
###########################################################################################

if __name__ == "__main__":
    app.run(debug=True)