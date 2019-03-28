import sys
import csv
import pandas as pd
import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plot
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
'exec(%matplotlib inline)'



def predictor(ticker,infofile,graphfile,col,t):

    dataset=pd.read_csv(infofile)
    df=dataset.loc[dataset[' Ticker']==ticker]
    print(df)
    newCol=' '+col
    X=df[[newCol]]
    Y=df['Time'].str.split(':').apply(lambda x: int(x[0])*60+int(x[1]))

    print(X)
    print(Y)

    X_train, X_test, y_train, y_test=train_test_split(X, Y, test_size=0.2, random_state=0)

    regressor=LinearRegression()
    regressor.fit(X_train, y_train)
    yprediction=regressor.predict(X_test)


    plot.scatter(X_train, y_train, color= 'purple')
    plot.plot(X_train, regressor.predict(X_train), color='green')
    plot.title('Time vs '+col)
    plot.xlabel(col)
    plot.ylabel('Time')
    plot.show()



if __name__ =="__main__":
    predictor(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
