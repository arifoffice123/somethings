import pandas as pd
from utility.dummyStock import DummyStock
from utility.stock import Stock

def main():
    print("starting....")
    
    watchlist = []
    with open("watchlist.txt", "r") as f:
        for line in f:
            watchlist.append(line.strip())
            
    print("getting history....")
    
    for watchCode in watchlist:
        
        dummy = DummyStock()
        history = dummy.getHistory(watchCode)
        
        #stock = Stock(watchCode, "1mo", "1d")
        #history = stock.getHistory()
        
        buyPatterns = [] # To be implemented
        #
        # buyPatterns = getBuyPatterns(history)
        #
        
        if(len(buyPatterns) > 0):
            print("BUY: " + watchCode)
        
        
    print("done")
    
if __name__ == "__main__":
    main()