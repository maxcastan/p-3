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
    table = doc.xpath('//div[@class = "genTable thin"]')[0]
    h3 = table.xpath('.//h3')
    ticks = h3.xpath('.//a[@href]/text()')
    total_ticks =[]
    for tick in ticks:
        total_ticks.append(ticks.text_content())
    print(total_ticks)
    #for i in  range(0,n+1):
    #    print(ticks[i])
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
