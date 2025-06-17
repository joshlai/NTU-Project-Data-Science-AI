from dagster import Definitions
from .dagster_wrapper import upload_yfinance_job,dbt_job,ta_compute,dbt_test

defs = Definitions(
    jobs=[upload_yfinance_job,dbt_job,ta_compute,dbt_test]
)
