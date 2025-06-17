### Section here is to download fred data. Use the fred_config json to configure what you wish to pull out. 

import pandas_datareader.data as web
import datetime
from dateutil.relativedelta import relativedelta
import yfinance as yf
import pandas as pd
from google.cloud import bigquery
import json
import os


# Function to compute start_date based on period no longer need to specify end and 
def get_date_range_from_period(period_str):
    today = datetime.date.today()
    end_date = today

    if period_str.endswith("d"):
        delta = datetime.timedelta(days=int(period_str[:-1]))
    elif period_str.endswith("mo"):
        delta = relativedelta(months=int(period_str[:-2]))
    elif period_str.endswith("y"):
        delta = relativedelta(years=int(period_str[:-1]))
    else:
        raise ValueError(f"Invalid period: {period_str}. Use formats like '1mo', '3y', '7d'.")

    start_date = end_date - delta
    return datetime.datetime.combine(start_date, datetime.time.min), datetime.datetime.combine(end_date, datetime.time.min)

# Load configuration
with open("fred_config.json") as f:
    config = json.load(f)

with open("bq_config.json") as f:
    bq_config = json.load(f)




# Extract BigQuery values
project_id = bq_config["project_id"]
dataset_id = bq_config["dataset_id"]
table_id = bq_config["table_id_fred"]
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "meta-sanctum-461903-p3-e443652134f2.json"

# Load series info
series_config = config["series"]



# Compute date range from period
period = config.get("period", "1y")  # default to 1 year if not specified
start_date, end_date = get_date_range_from_period(period)



# Download and combine data
econ_data = pd.DataFrame()

for series_code, series_name in series_config.items():
    print(f"Downloading {series_name} ({series_code})...")
    data = web.DataReader(series_code, 'fred', start_date, end_date)
    data.columns = [series_name]
    econ_data = data if econ_data.empty else econ_data.join(data, how='outer')



econ_data.index.name = "date"


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
    econ_data, f"{project_id}.{dataset_id}.{table_id}", job_config=job_config
)
job.result()  # Wait for completion  # or use .history(start=..., end=...