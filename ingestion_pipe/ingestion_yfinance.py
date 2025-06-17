### section here is to download yfinance

import yfinance as yf
import pandas as pd### section here is to download yfinance jacob's code this is usable. Includes Peihan's orginal code.
import yfinance as yf
import pandas as pd
from google.cloud import bigquery
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
ticker_symbols = stock_config["ticker"] 
period = stock_config["period"]



# Extract BigQuery values
project_id = bq_config["project_id"]
dataset_id = bq_config["dataset_id"]
table_id = bq_config["table_id"]
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "meta-sanctum-461903-p3-e443652134f2.json" # service account private key 


# Collect data for each ticker
all_data = []

for symbol in ticker_symbols:
    df = yf.Ticker(symbol).history(period=period)
    df["ticker_symbol"] = symbol  # Add a column to identify the ticker
    all_data.append(df)

# Combine all into one DataFrame
combined_df = pd.concat(all_data)

# Optional: Reset index if needed
combined_df = combined_df.reset_index()

combined_df = combined_df.rename(columns={
    "Open": "open_price",
    "Close": "close_price",
    "High": "high_price",
    "Low": "low_price",
    "Volume": "volume_traded",
    "Dividends":"dividend",
    "Stock Splits":"stock_splits",
    "Date":"date"
})


# 3. Initialize BigQuery client
client = bigquery.Client(project=project_id)

# 4. Load data into BigQuery
job_config = bigquery.LoadJobConfig(
    ## section here is set to over ride the data. Using append complicates the code
    write_disposition="WRITE_TRUNCATE",  # or WRITE_TRUNCATE or # "Write_Append"
    autodetect=True,
    source_format=bigquery.SourceFormat.PARQUET
)

# Load DataFrame to BigQuery
job = client.load_table_from_dataframe(
    combined_df, f"{project_id}.{dataset_id}.{table_id}", job_config=job_config
)
job.result()  # Wait for completion  # or use .history(start=..., end=...

