
# This script shows live stock prices and automatically refreshes
# Run the following command to install Yahoo Finance:
# pip install yfinance

import time
import yfinance as yf


def get_live_price(ticker):
    """Retrieves live price data for the given ticker symbol"""
    stock = yf.Ticker(ticker)
    try:
        price = stock.fast_info.get("lastPrice", "No data price is available")
        return price
    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    ticker = input("Please enter a stock symbol: ").upper()
    REFRESH_INTERVAL = 5  # Refresh interval in seconds

    while True:
        price = get_live_price(ticker)
        print(f"Live price of {ticker}: {price}")
        time.sleep(REFRESH_INTERVAL)  # See refresh_interval above
