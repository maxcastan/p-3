import sys
import csv
def predictor(ticker,infofile,graphfile,col,t):
    with open(infofile) as csvfile:
        csvreader =  csv.reader(csvfile,delimiter=',')
        for row in csvreader:
            if row[1]==ticker:
                latestPrice = row[2]
                latestVolume = row[3]
    print(latestPrice,latestVolume)



if __name__ =="__main__":
    predictor(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
