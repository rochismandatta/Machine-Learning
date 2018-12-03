import pandas as pd
import pandas_datareader.data as web
import datetime as dt
import quandl
from nsepy import get_history

start = dt.datetime(2000,1,1)
end = dt.datetime(2015,12,12)
symbol = 'RELIANCE'
df = get_history(symbol,start,end)
#df = web.DataReader('GOOGL', 'quandl', authtoken="s_K9to9-WPCWs4fLX88v" ,start, end)
print(df.head())
