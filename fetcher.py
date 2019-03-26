'''
    python3 fetcher.py time_lim ticker.txt info.csv
    this module updates stock information from a given ticker symbol

'''
import sys,os
from iex import Stock
import datetime

def addSecs(tm, secs):
    date=datetime.datetime(100, 1, 1, tm.hour, tm.minute, tm.second)
    date=date+datetime.timedelta(seconds=secs)
    return date.time()

def update_stock_info(ticker, stop):
    now=datetime.datetime.now()

    if(now.time()>stop):
        sys.exit()
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
    present=datetime.datetime.now()
    stopTime=addSecs(present, int(sys.argv[1]))
    print("Time, Ticker, latestPrice, latestVolume, Close, Open, low, high", file=outfile)
    with open(sys.argv[2],"r") as f:
        for tick in f:
            update_stock_info(tick.strip(), stopTime)
    outfile.close()
