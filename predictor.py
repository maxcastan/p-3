import sys
import csv
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
'exec(%matplotlib inline)'



def predictor(ticker,infofile,graphfile,col,t):
    times=[]
    value=[]
    with open(infofile) as csvfile:
        csvreader =  csv.reader(csvfile,delimiter=',')
        for row in csvreader:
            if row[1]==ticker:
                times.append(datetime.strptime(row[0], "%H:%M"))
                if(col=='latestPrice'):
                    value.append(float(row[2]))
                else:
                    value.append(float(row[3]))
    print(value)
    print(times)




if __name__ =="__main__":
    predictor(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
