### section here is to download technical analysis data from Peihan/Norman.

import yfinance as yf
import pandas as pd
import ta
from google.cloud import bigquery
from datetime import datetime
import json
import os

####Note that the stock_config.json must be in the same directory is your py file

# Load stock config
with open("stock_config.json") as f:
    stock_config = json.load(f)

# Load BigQuery config
with open("bq_config.json") as f:
    bq_config = json.load(f)

##extract ticker values
period = stock_config["period"]
tickers = stock_config["ticker"]

# Extract BigQuery values
project_id = bq_config["project_id"]
dataset_id = bq_config["dataset_id"]
table_id = bq_config["table_id_ta"]
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "meta-sanctum-461903-p3-e443652134f2.json"  # service account private key 


# === SET UP BIGQUERY CLIENT ===
client = bigquery.Client(project=project_id)
table_ref = f"{project_id}.{dataset_id}.{table_id}"

job_config = bigquery.LoadJobConfig(
    write_disposition=bigquery.WriteDisposition.WRITE_APPEND,
    schema=[
        bigquery.SchemaField("date", "DATE"),
        bigquery.SchemaField("ticker_symbol", "STRING"),
        bigquery.SchemaField("rsi_14", "FLOAT"),
        bigquery.SchemaField("sma_50", "FLOAT"),
        bigquery.SchemaField("ema_50", "FLOAT"),
    ],
)

# === PROCESS EACH TICKER ===
for ticker in tickers:
    try:
        print(f"⏱️ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Downloading and processing: {ticker}")

        df = yf.download(ticker, period=period, auto_adjust=True)
        df.reset_index(inplace=True)

        close_prices = df['Close']
        if isinstance(close_prices, pd.DataFrame) or len(close_prices.shape) > 1:
            close_prices = close_prices.squeeze()

        # Calculate indicators
        df['rsi_14'] = ta.momentum.RSIIndicator(close=close_prices, window=14).rsi()
        df['sma_50'] = ta.trend.SMAIndicator(close=close_prices, window=50).sma_indicator()
        df['ema_50'] = ta.trend.EMAIndicator(close=close_prices, window=50).ema_indicator()

        # Add ticker column
        df['ticker_symbol'] = ticker

        # Flatten MultiIndex columns if present
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = ['_'.join(map(str, col)).strip('_') for col in df.columns.values]

        # Select columns and rename for BigQuery
        df_bq = df[['Date', 'ticker_symbol', 'rsi_14', 'sma_50', 'ema_50']].copy()
        df_bq.rename(columns={'Date': 'date'}, inplace=True)

        # Remove rows with missing indicator values
        df_bq.dropna(inplace=True)

        # Upload to BigQuery
        job = client.load_table_from_dataframe(df_bq, table_ref, job_config=job_config)
        job.result()

        print(f"✅ Uploaded {len(df_bq)} rows for {ticker} to {table_ref}.")

    except Exception as e:
        print(f"❌ Error processing {ticker}: {e}")

print("🎉 All tickers uploaded successfully.")