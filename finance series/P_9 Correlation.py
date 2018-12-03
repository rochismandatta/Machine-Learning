import bs4 as bs
import pickle
import requests
import quandl
import datetime as dt
import os
import pandas_datareader.data as web
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

style.use('ggplot')

def save_SandP500_tickers():
    resp =requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        tickers.append(ticker)


    with open("sp500tickers.pickle","wb") as f:
        pickle.dump(tickers,f)


    print(tickers)
    return tickers

#save_SandP500_tickers()

#quandl.ApiConfig.api_key = "s_K9to9-WPCWs4fLX88v" #>>overrides the 50 calls/day

def get_data_from_quandl(reload_sp500=False):
    quandl.ApiConfig.api_key = "s_K9to9-WPCWs4fLX88v"
    if reload_sp500:
        tickers = save_SandP500_tickers()

    else:
        with open("sp500tickers.pickle","rb") as f:
            tickers = pickle.load(f)


    if not os.path.exists('stock_dfs'):
        os.makedirs('stock_dfs')


    start = dt.datetime(2000,1,1)
    end = dt.datetime(2016,12,31)

    for ticker in tickers:
        print(ticker)
        if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
            
            #df=quandl.get('WIKI/ticker', start_date="2000-1-1", end_date="2016-12-31")
            df=web.DataReader(ticker,'quandl',start,end)
            print("Code was able to fetch")
            df.to_csv('stock_dfs/{}.csv'.format(ticker))

        else:
            print('Already have {}'.format(ticker))

#get_data_from_quandl()


def compile_data():
    with open("sp500tickers.pickle", "rb") as f:
        tickers = pickle.load(f)

    main_df= pd.DataFrame() #dataframe object

    for count,ticker in enumerate(tickers):
        #enumerate returns 0, 0th element, 1 1st element
        df=pd.read_csv('stock_dfs/{}.csv'.format(ticker))
        df.set_index('Date', inplace =True)
        df.rename(columns = {'AdjClose':ticker}, inplace =True)
        
        df.drop(['Open','High','Low','Close','Volume','ExDividend','SplitRatio','AdjOpen','AdjHigh','AdjLow','AdjVolume'],1, inplace =True)

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df, how = 'outer')


        if count%10==0:
            print(count)

    print(main_df.head())
    main_df.to_csv('sp500_joined_closes.csv')


def visualize_data():
    df= pd.read_csv('sp500_joined_closes.csv')
##    df['AAPL'].plot()
##    plt.show()

    df_corr = df.corr() # new data frame creates all the correlation values between different tickers
    df_corr.to_csv('Correlation_data_SP500.csv')
    #print(df_corr.head())
    data = df_corr.values #gets inner data ie not the index etc
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1) #1*1 plot 1
    heatmap = ax.pcolor(data, cmap = plt.cm.RdYlGn) #cmap is a range of colors, red being bad to yellow neutral to green good
    fig.colorbar(heatmap)

    ## setting ticks at each mark
    ax.set_xticks(np.arange(data.shape[0]) +0.5, minor = False)
    ax.set_yticks(np.arange(data.shape[1]) +0.5, minor = False)

    ax.invert_yaxis()
    ax.xaxis.tick_top()

    column_labels = df_corr.columns
    row_labels = df_corr.index

    ax.set_xticklabels(column_labels)
    ax.set_yticklabels(row_labels)
    plt.xticks(rotation = 90)
    heatmap.set_clim(-1,1) #setting range of heatmap colors
    plt.tight_layout()
    plt.show()

visualize_data()
    
    
