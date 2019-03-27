import sys
import csv

def print_query_data(infofile,ticker,time, verbose):
    with open(infofile) as csvfile:
        csvreader =  csv.reader(csvfile,delimiter=',')
        for row in csvreader:
            if (row[0]==time)and(row[1]==ticker):
                if(verbose=='True'):
                    print("Time: "+time)
                    print("File: "+infofile)
                    print("Ticker: "+ ticker)
                print("Latest Price: "+row[2])
                print("Latest Volume: "+row[3])
                print("Close: "+row[4])
                print("Open: "+row[5])
                print("Low: "+row[6])
                print("High: "+row[7]+"\n\n")




if __name__ == "__main__":
    print_query_data(sys.argv[2],sys.argv[3],sys.argv[4], sys.argv[1])
