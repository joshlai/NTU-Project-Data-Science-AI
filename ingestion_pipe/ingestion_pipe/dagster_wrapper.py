from dagster import op, job
import subprocess

@op
def run_yfinance_script():
    subprocess.run(["python", "injestion_yfinance.py"], check=True)

@op
def run_stock_info_script():
    subprocess.run(["python", "injestion_stock_info.py"], check=True)

@op
def run_fred_script():
    subprocess.run(["python", "injestion_fred.py"], check=True)

@job
def upload_yfinance_job():
    run_yfinance_script()
    run_stock_info_script()
    run_fred_script()
