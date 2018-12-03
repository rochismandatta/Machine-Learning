import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web


style.use('ggplot')

df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)
df['100ma'] = df['AdjClose'].rolling(window=100).mean()

df.dropna(inplace=True) #inplace = True essentially replaces df =df.dropna()
print(df.head())


# the subplots are called axes
# subplot 1st parameter is the grid size in this case its 6rows * 1 column
# starting point 00
ax1 = plt.subplot2grid((6,1),(0,0), rowspan =5, colspan =1)
#similarly ax2
ax2 = plt.subplot2grid((6,1),(5,0), rowspan =1, colspan =1, sharex=ax1)

ax1.plot(df.index, df['AdjClose'])
ax1.plot(df.index, df['100ma'])
ax2.bar(df.index, df['Volume'])


plt.show()
