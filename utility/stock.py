import yfinance as yf

class Stock:
    def __init__(self, ticker, period="1mo", interval="1d"):
        self.ticker = ticker
        self.tickerObj = yf.Ticker(ticker)
        self.period = period
        self.interval = interval
        
    def getHistory(self):
        return self.tickerObj.history(period=self.period, interval=self.interval)