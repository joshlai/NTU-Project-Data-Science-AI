from dagster import ScheduleDefinition
from .dagster_wrapper import upload_yfinance_job

# Run every day at 8 AM
daily_schedule = ScheduleDefinition(
    job=upload_yfinance_job,
    cron_schedule="30 16 * * *",  # ⏰ Cron format: minute hour day month weekday
    name="daily_upload_yfinance_job"
)
