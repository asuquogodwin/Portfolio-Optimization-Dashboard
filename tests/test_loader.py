from src.data_loader import download_data

prices = download_data(
    tickers=["AAPL", "MSFT", "NVDA"],
    start_date="2020-01-01",
    end_date="2025-01-01",
)

print(prices.head())