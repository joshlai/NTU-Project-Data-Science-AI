from dagster import ScheduleDefinition
from .dagster_wrapper import upload_yfinance_job,dbt_job,dbt_test

# Run every day at 8 AM
daily_schedule = ScheduleDefinition(
    job=upload_yfinance_job,
    cron_schedule="30 7 * * *",  # ⏰ Cron format: minute hour day month weekday
    name="daily_upload_yfinance_job"
)
daily_dbt_schedule = ScheduleDefinition(
    job=dbt_job,
    cron_schedule="45 7 * * *",
    name="daily_dbt_job"
)

daily_dbt_test_schedule = ScheduleDefinition(
    job=dbt_test,
    cron_schedule="0 8 * * *",
    name="daily_dbt_test"
)
