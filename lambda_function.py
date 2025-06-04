import yfinance as yf

def lambda_handler(event, context):
    # Fetch list of ticker data from Yahoo Finance
    tickers = ["MSFT", "GOOG", "META"]
    tickersData = yf.download(tickers, start="2025-01-01", end="2025-05-30")

    # Return the tickers data
    return {
        "statusCode": 200,
        "body": tickersData
    }

# Simulate Lambda event and context
if __name__ == "__main__":
    event = {}  # Mock event data
    context = None  # Mock context (optional)
    result = lambda_handler(event, context)
    print(result)