### section here is to download yfinance

import yfinance as yf
import pandas as pd
from google.cloud import bigquery
import json
import os



### Importanting Service account json 
### note that your service account Json needs to be in the same folder as the py file you are using or you need to specify the file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "meta-sanctum-461903-p3-e443652134f2.json"


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


########## Peihan code section################################33
df = yf.download(ticker_symbols, period=period)
df.columns = ['{}_{}'.format(col[0], col[1]) for col in df.columns]  # flatten columns
df = df.reset_index()

df = (
    pd.melt(df, id_vars='Date', var_name='Price_Ticker', value_name='Value')
      .assign(Price_Type=lambda x: x.Price_Ticker.str.split('_').str[0],
              Ticker=lambda x: x.Price_Ticker.str.split('_').str[1])
      .drop(columns='Price_Ticker')
      .pivot_table(index=['Date', 'Ticker'], columns='Price_Type', values='Value')
      .reset_index()
)


##### Perhan Code Section ########################################


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
    df, f"{project_id}.{dataset_id}.{table_id}", job_config=job_config
)
job.result()  # Wait for completion  # or use .history(start=..., end=...
