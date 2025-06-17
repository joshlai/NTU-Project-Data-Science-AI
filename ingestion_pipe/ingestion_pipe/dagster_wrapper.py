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


##@op
##def run_dbt():
##    subprocess.run(["dbt", "run"], cwd="/home/biscuit/NTU-Project-Data-Science-AI/dbt_yfinance", check=True)

@op
def run_dbt_yfinance():
    subprocess.run(
        [
            "dbt", 
            "run", 
            "--project-dir", "/home/biscuit/NTU-Project-Data-Science-AI/dbt_yfinance",
            "--profiles-dir", "/home/biscuit/NTU-Project-Data-Science-AI/dbt_yfinance"
        ],
        check=True
    )




@job
def upload_yfinance_job():
    run_yfinance_script()
    run_stock_info_script()
    run_fred_script()
    

@job
def dbt_job():
    run_dbt()