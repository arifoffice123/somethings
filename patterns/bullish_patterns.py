import pandas as pd
def bullish_engulfing(df:pd.DataFrame):
    open_prices = df['Open']
    close_prices = df['Close']
    high_prices = df['High']
    low_prices = df['Low']

    # Check for a bullish engulfing pattern
    bullish_engulfing = close_prices.iloc[-1] > open_prices.iloc[-1] and close_prices.iloc[-2] > open_prices.iloc[-2] \
                        and open_prices.iloc[-1] < close_prices.iloc[-2] and close_prices.iloc[-1] > open_prices.iloc[-2]
    return bullish_engulfing