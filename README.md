# Project 2: Big Five Stocks Dashboard

## Project Objective

In this project, we will create an interactive dashboard visualizing NASDAQ stock data of tech companies known as the Big Five; Apple, Google, Amazon, Facebook and Microsoft. These five prominent American technology companies have a combined market capitalization of over $4 trillion. 

![screenshot](Images/screenshot.jpg)

## Team Members

* [Catie Clark](https://github.com/csidneyclark)
* [Jake Clifton](https://github.com/cliftjc1)
* [Masita Mohamad](https://github.com/masitamohamad)
* [Matthew O'Connor](https://github.com/oconnormatt781)

## Project Workflow

### Pre-project tasks:
- ETL (Extract, Transform, and Load): Jake

### Back-end:
- Create a database-powered API using Python Flask application: Jake
- Routes:
    * `/` : Home page (or where our dashboard will reside)
    * `/api` : Data to be used for front-end visualizations

### Front-end:
- HTML, CSS & Bootstrap: Masita
- D3.js Interactive Visualizations: Catie
    * Stock Prices: Candlestick Chart
    * Stock Volume: Bar / Bubble / Pie Chart
    * Tooltips
- Leaflet.js (Company location, total employees & company info): Masita
- Web scraping (Latest financial news): Masita

### Deployment:
- Connection to back-end: All

### Misc. Tasks:
- Stock Data Analysis: Matt

## Additional Data Analysis

![scaled-price](Images/Scaled_Open_Price.jpg)
![scaled-volume](Images/Scaled_Volume.jpg)
![total-volume](Images/Total_Volume.jpg)

***
## Data Source

The original dataset can be found [here](https://www.kaggle.com/abdullahmu/big-five-stocks)

Description:
Historical NASDAQ stock data of tech companies dubbed: 'Big Five' until August 23rd, 2019