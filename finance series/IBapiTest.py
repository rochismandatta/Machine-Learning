import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
from ibapi_grease import patch_all
patch_all()

style.use('ggplot')

start = dt.datetime(2000,1,1)
end = dt.datetime(2016,12,31)

df = web.DataReader("TSLA", 'IBApi.EWrapper ', start, end) 
##print(df.head())
#df.to_csv('tsla.csv')

#df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)
##print(df.head())
df['AdjClose'].plot()
plt.show()
