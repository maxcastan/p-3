import sys
import csv

def print_query_data(infofile,ticker,time):
    with open(infofile) as csvfile:
        csvreader =  csv.reader(csvfile,delimiter=',')
        for row in csvreader:
            if (row[0]==time)and(row[1]==ticker):
                print("a match!")




if __name__ == "__main__":
    print_query_data(sys.argv[1],sys.argv[2],sys.argv[3])
