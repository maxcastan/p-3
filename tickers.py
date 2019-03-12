#!/usr/bin/env/python3
'''
    py file to extract valid tickers from nasdaq website
'''
import requests
import sys
import time
import urllib.request
from bs4 import BeautifulSoup

def save_tickers(n):
    '''
    uses beautifulsoup to organize pulled data
    searches for <a></a> with parent <h3> which indicates /symbol
    '''
    fopen=open(sys.argv[2],'w+')
    page = requests.get('http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQrender=download')
    soup = BeautifulSoup(page.text,"html.parser")
    for link in soup.find_all('a'):
        if(link.find_parent("h3")):
            tik = link.get('href')
            print(tik[30:].upper(),file=fopen)
    fopen.close()
if __name__ ==  "__main__":
    save_tickers(int(sys.argv[1]))
