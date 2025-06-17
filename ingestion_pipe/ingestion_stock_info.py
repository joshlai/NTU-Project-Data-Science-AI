#### this code pulls all yfinance stock info which includes dividends and stuff sector

import pandas_datareader.data as web
import datetime
from dateutil.relativedelta import relativedelta
import yfinance as yf
import pandas as pd
from google.cloud import bigquery
import json
import os



### Importanting Service account json 
### note that your service account Json needs to be in the same folder as the py file you are using or you need to specify the file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "meta-sanctum-461903-p3-e443652134f2.json"



# Load configuration
with open("stock_config.json") as f:
    config = json.load(f)

with open("bq_config.json") as f:
    bq_config = json.load(f)


tickers = config.get("ticker", [])


# Extract BigQuery values
project_id = bq_config["project_id"]
dataset_id = bq_config["dataset_id"]
table_id = bq_config["table_id_stock_info"]



# List to collect info dicts
data = []

# Loop through each ticker
for symbol in tickers:
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.get_info()

        if info:
            # Extract only selected fields
            entry = {
                "ticker_symbol": symbol,
                "company_name": info.get("longName"),
                "company_description": info.get("longBusinessSummary"),
                "country":info.get("country"),
                "sector": info.get("sector"),
                "industry": info.get("industry"),
                "market_cap": info.get("marketCap"),
                "country": info.get("country"),
                "trailing_pe":info.get("trailingPE"),
                "forward_pe":info.get("forwardPE"),
                "trailing_EPS": info.get("trailingEps"),
                "forward_EPS":info.get("forwardEps"),    
                "dividendYield": info.get("dividendYield")  



            }
            data.append(entry)
        else:
            print(f"No data found for {symbol}")
    except Exception as e:
        print(f"Error retrieving {symbol}: {e}")

# Combine into one DataFrame
df_stock_info = pd.DataFrame(data)

# Combine into one DataFrame
df_stock_info = pd.DataFrame(data)

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
    df_stock_info, f"{project_id}.{dataset_id}.{table_id}", job_config=job_config
)
job.result()  # Wait for completion  # or use .history(start=..., end=...
