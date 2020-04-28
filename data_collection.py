import yfinance as yf
from bs4 import BeautifulSoup
import requests

#-----Get values for Tickers-------
def is_valid(ticker):
    try: 
        yf.Ticker(ticker).info
        return True
    except:
        return False

def get_price(ticker):
    try:
        stock = yf.Ticker(ticker)
        #print(stock.info["regularMarketPrice"])
        return stock.info["regularMarketPrice"]
    except:
        return 0

#-----Scrape implied volatility values from McMillan Analysis Corp. -------
def get_vol(ticker):
    URL = "https://www.optionstrategist.com/calculators/free-volatility-data"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        content = soup.find("pre")
        text = content.text.strip()
        rows = text.splitlines()
        del rows[0:25] #remove header rows
        for row in rows:
            split = row.split()
            if split[0] == ticker:
                info = row.split()
                vol = float(info[5])
                #print(vol)
                return round(vol * 0.01, 4) #convert percentage to decimal
    except:
        return 0

#-----Scrape US Treasury for 10-Year Bonds-----

def get_risk_free():
    URL = "https://www.treasury.gov/resource-center/data-chart-center/interest-rates/pages/textview.aspx?data=yield"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        #scrape US Treasury for 10-year gov bond
        table = soup.find("table", attrs={'class' : 't-chart'})
        rows = table.find_all("tr")
        rate = float(rows[len(rows)-1].find_all("td")[10].get_text())
        rate = rate * 0.01 #convert % to decimal
        #print(type(rate))
        #print(rate)
        return rate

    except: 
        rate = 0.02 #2% if scraping fails
        return rate



