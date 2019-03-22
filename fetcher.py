'''
    python3 fetcher.py time_lim ticker.txt info.csv
    this module updates stock information from a given ticker symbol

'''
import sys,os
from iex import Stock
import datetime

def update_stock_info(ticker):
    now=datetime.datetime.now()

    sys.stdout = open(os.devnull,"w")
    print(now.strftime("%H:%M"), file=outfile, end=',')
    print(ticker,file = outfile,end =',')
    print(Stock(ticker).quote().get('latestPrice'),file =outfile,end=',')
    print(Stock(ticker).quote().get('latestVolume'),file =outfile,end=',')
    print(Stock(ticker).quote().get('Close'),file =outfile,end=',')
    print(Stock(ticker).quote().get('Open'),file =outfile,end=',')
    print(Stock(ticker).quote().get('low'),file =outfile,end=',')
    print(Stock(ticker).quote().get('high'),file =outfile)
    sys.stdout = sys.__stdout__

if __name__ == "__main__":
    outfile = open(sys.argv[3],"w")
    with open(sys.argv[2],"r") as f:
        for tick in f:
            update_stock_info(tick.strip())
    outfile.close()
