import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web
import matplotlib.pyplot as  plt
from talib import RSI, BBANDS
import datetime as dt 
import numpy as np 
start = '2015-04-22'
end = '2017-04-22'
symbol = 'MCD'
max_holding = 100
price = web.DataReader(name=symbol, data_source='quandl', start=start, end=end)
print(price.head())
price = price.iloc[::-1]
print(price.head())
price = price.dropna()
close = price['AdjClose'].values
up, mid, low = BBANDS(close, timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
rsi = RSI(close, timeperiod=14)
print("RSI (first 10 elements)\n", rsi[14:24])

