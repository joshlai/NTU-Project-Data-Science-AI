from dagster import Definitions
from .dagster_wrapper import upload_yfinance_job,dbt_job

defs = Definitions(
    jobs=[upload_yfinance_job,dbt_job]
)
