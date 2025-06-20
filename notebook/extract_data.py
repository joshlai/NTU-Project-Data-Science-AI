import yfinance as yf
import pandas as pd
import os
import pandas_datareader.data as web
import datetime
from pandas_datareader import data as pdr

def many_tickers(tickers, start_date, end_date):

    df = yf.download(tickers, start=start_date, end=end_date)
    # df.columns = ['{}_{}'.format(col[0], col[1]) for col in df.columns]  # flatten columns
    # df = df.reset_index()
    # df = (
    #     pd.melt(df, id_vars='Date', var_name='Price_Ticker', value_name='Value')
    #     .assign(Price_Type=lambda x: x.Price_Ticker.str.split('_').str[0],
    #             Ticker=lambda x: x.Price_Ticker.str.split('_').str[1])
    #     .drop(columns='Price_Ticker')
    #     .pivot_table(index=['Date', 'Ticker'], columns='Price_Type', values='Value')
    #     .reset_index()
    # )

    return df;

def many_fred_data(data_codes, column_names, source, start_date, end_date):
    if source != 'fred':
        raise ValueError("Currently, only 'fred' source is supported.")
    
    all_data = []
    
    for code, name in zip(data_codes, column_names):
        try:
            df = pdr.get_data_fred(code, start=start_date, end=end_date)
            df.rename(columns={code: name}, inplace=True)
            all_data.append(df)
        except Exception as e:
            print(f"Error fetching data for {code}: {e}")
    
    # Merge all data on the 'DATE' index
    if all_data:
        merged_data = pd.concat(all_data, axis=1)
        merged_data.index.name = 'DATE'
        return merged_data.reset_index()
    else:
        return pd.DataFrame();  # Return an empty DataFrame if no data fetched