#!/usr/bin/env/python3
'''
    py file to extract valid tickers from nasdaq website
'''
import requests
import sys
import time
from iex import Stock
import lxml.html
from  lxml import html

def save_tickers(n):
    '''
    Args:
        n: number of tickers to print to file
    '''
    fopen=open(sys.argv[2],'w+') #open the file in write mode
    page = requests.get('http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQrender=download') #saves all url info
    doc = lxml.html.fromstring(page.content)
    table = doc.xpath('//div[@class = "genTable thin"]')[0] #grabs first instance of genTable, which stores tickers
    unparsed_ticks = []
    for i in range(0,n):
        h3 = table.xpath('.//h3')[i]    #grabs all h3 headers
        ticks = h3.xpath('.//a')        #grabs a headers under h3
        for tick in ticks:
            unparsed_ticks.append(tick.text_content())      #includes a bunch of tabs?
    total_ticks =[]
    for x in unparsed_ticks:
        total_ticks.append(x[-5:])      #removes tabs
    for x in total_ticks:
        print(x.strip(),file =fopen)        #prints list of tickers to file tickers.txt



    fopen.close()

def check_if_valid(ticker):
    '''
    uses iex-api-python to check if ticker has valid price function
    Args:
        ticker: fetched ticker from NASDAQ website
    '''
    price = Stock(ticker).price()
    #print(price)
    if price: #how to know if price function didnt work?
        return True
    else:
        return False

if __name__ ==  "__main__":
    save_tickers(int(sys.argv[1]))
