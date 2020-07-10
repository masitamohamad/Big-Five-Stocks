from flask import Flask, render_template, redirect
from bs4 import BeautifulSoup as bs 
import requests

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
    
    news_timestamp = [item + ':' for item in news_timestamp]
    
    joined_lists = [' '.join(x) for x in zip(news_timestamp,news_headline)]

    return joined_lists

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

###########################################################################################
# Main Behavior
###########################################################################################

if __name__ == "__main__":
    app.run(debug=True)