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
    fopen=open(sys.argv[2],'w+') #open the file in write mode
    page = requests.get('http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQrender=download') #saves all url info
    soup = BeautifulSoup(page.text,"html.parser") #organizes all data from url for easy access
    for link in soup.find_all('a'): #finds all headers that start with <a>
        if(link.find_parent("h3")): #finds the a with h3 as the parent
            tik = link.get('href') #grabs the value of href
            print(tik[30:].upper(),file=fopen) #print only the ticker symbol to the file
    fopen.close()
if __name__ ==  "__main__":
    save_tickers(int(sys.argv[1]))
