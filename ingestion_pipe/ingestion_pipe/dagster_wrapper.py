from dagster import op, job
import subprocess

@op
def run_yfinance_script():
    try:
        subprocess.run(
            ["python", "/home/biscuit/NTU-Project-Data-Science-AI/ingestion_pipe/ingestion_yfinance.py"],
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Error running ingestion_yfinance.py: {e}")
        raise

@op
def run_stock_info_script():
    try:
        subprocess.run(
            ["python", "/home/biscuit/NTU-Project-Data-Science-AI/ingestion_pipe/ingestion_stock_info.py"],
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Error running injestion_stock_info.py: {e}")
        raise

@op
def run_fred_script():
    try:
        subprocess.run(
            ["python", "/home/biscuit/NTU-Project-Data-Science-AI/ingestion_pipe/ingestion_fred.py"],
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Error running ingestion_fred.py: {e}")
        raise

@op
def run_dbt_yfinance():
    try:
        subprocess.run(
            [
                "dbt",
                "run",
                "--project-dir", "/home/biscuit/NTU-Project-Data-Science-AI/dbt_yfinance",
                "--profiles-dir", "/home/biscuit/NTU-Project-Data-Science-AI/dbt_yfinance",
            ],
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Error running dbt: {e}")
        raise

@job
def upload_yfinance_job():
    run_yfinance_script()
    run_stock_info_script()
    run_fred_script()

@job
def dbt_job():
    run_dbt_yfinance()
