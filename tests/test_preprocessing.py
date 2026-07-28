from src.data_loader import download_data
from src.preprocessing import clean_prices, calculate_returns

prices = download_data(
    tickers=["AAPL", "MSFT", "NVDA"],
    start_date="2020-01-01",
    end_date="2025-01-01"
)

cleaned = clean_prices(prices)

returns = calculate_returns(cleaned)

print("Prices")
print(cleaned.head())

print("\nReturns")
print(returns.head())