# p-3
# Python Programming Project
## Execution Instructions
+ Includes tickers.py fetchers.py query.py and predictor.py
+ Commands to run __tickers.py__-> python3 tickers.py #ofargs tickers.txt
+ Commands to run __fetcher.py__-> python3 fetcher.py #time tickers.txt info.csv
+ Commands to run __query.py__-> python3 query.py True/False info.csv (ticker) (time HH:MM)
+ Commands to run __predictor.py__-> python3 predictor.py ticker info.csv graph.png col(latestPrice/latestVolume) time
## Needed Libraries
+ sys,os,requests
+ csv
+ pandas
+ numpy
+ datetime
+ matplotlib
+ sklearn
+ iex
+ lxml
+ datetime

********
# Documentation/Notes
+ In __tickers.py__, many attempts were made to navigate to the next page by manipulating the html.
Both attempts were included in the file but not used. The next_page() function successfully switches
to the next page but I was unable to integrate it into the code correctly. We tried!!!
Instead, we set the url as the NASDAQ website with '200 items per page' already selected
+ Max's virtual machine was unreliable the first few days we worked on the project, resulting on him not being able to push any of his work, therefore the GitHub commit data is skewed.
We each contributed to the project an equal amount.
