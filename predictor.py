'''
The command to run this program is:
python3 predictor.py ticker info.csv graphfile.png latestPrice/Volume minutes


Authors: Max Castaneda and Paulina Scarlata


This module takes a ticker name, csv file, a graph filename, a selection of latestPrice/Volume and the next
t minutes. The module then creates a plot of actual data as well as a plot of predicted data and
plots the regresssion line onto a graph and exports the graph to the passed filename

'''
import sys
import csv
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plot
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
'exec(%matplotlib inline)'



def predictor(ticker,infofile,graphfile,col,t):

    now=datetime.now()
    timeMinutes=int(now.hour)*60+int(now.minute)
    predictTime=timeMinutes+int(t)

    new=[]
    for x in range(timeMinutes, predictTime):
        new.append(x)

    print(new)

    dataset=pd.read_csv(infofile)
    df=dataset.loc[dataset[' Ticker']==ticker]
    newCol=' '+col
    Y=df[[newCol]]
    X=df['Time'].str.split(':').apply([lambda x: int(x[0])*60+int(x[1])])


    X_train, X_test, y_train, y_test=train_test_split(X, Y, test_size=1/3, random_state=0)

    regressor=LinearRegression()
    regressor.fit(X_train, y_train)
    yprediction=regressor.predict(X_test)


    plot.scatter(X_train, y_train, color= 'purple')
    plot.plot(X_train, regressor.predict(X_train), color='green')
    plot.title(col+' vs Time')
    plot.ylabel(col)
    plot.xlabel('Time')
    plot.savefig(graphfile)



if __name__ =="__main__":
    predictor(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
