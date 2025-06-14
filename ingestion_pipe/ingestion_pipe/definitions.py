from dagster import Definitions, load_assets_from_modules
from ingestion_pipe import assets, dagster_wrapper, schedules

all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=all_assets,
    jobs=[dagster_wrapper.upload_yfinance_job],### still calling the same job
    schedules=[schedules.daily_schedule]  # ✅ This must be here!
)
