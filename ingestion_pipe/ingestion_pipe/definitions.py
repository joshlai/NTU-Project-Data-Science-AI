from dagster import Definitions, load_assets_from_modules
from ingestion_pipe import assets, dagster_wrapper, schedules

all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=all_assets,
    jobs=[dagster_wrapper.upload_yfinance_job,dagster_wrapper.dbt_job,dagster_wrapper.dbt_test],### still calling the same job
    schedules=[schedules.daily_schedule,schedules.daily_dbt_schedule,schedules.daily_dbt_test_schedule]  # ✅ This must be here!
)
