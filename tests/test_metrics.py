from src.data_loader import download_data
from src.preprocessing import clean_prices, calculate_returns
from src.metrics import (
    calculate_mean_returns,
    calculate_volatility,
    calculate_covariance_matrix,
    calculate_correlation_matrix,
    calculate_annualized_returns,
    calculate_annualized_volatility,
    calculate_sharpe_ratio,
    calculate_cumulative_returns,
    calculate_drawdown,
    calculate_max_drawdown,
    calculate_rolling_volatility,
)

prices = download_data(
    tickers=["AAPL", "MSFT", "NVDA"],
    start_date="2020-01-01",
    end_date="2025-01-01",
)

prices = clean_prices(prices)
returns = calculate_returns(prices)

print("\nMean Returns")
print(calculate_mean_returns(returns))

print("\nVolatility")
print(calculate_volatility(returns))

print("\nCovariance Matrix")
print(calculate_covariance_matrix(returns))

print("\nCorrelation Matrix")
print(calculate_correlation_matrix(returns))

print("\nAnnualized Returns")
print(calculate_annualized_returns(returns))

print("\nAnnualized Volatility")
print(calculate_annualized_volatility(returns))

print("\nSharpe Ratio")
print(calculate_sharpe_ratio(returns))

print("\nCumulative Returns")
print(calculate_cumulative_returns(returns).tail())

print("\nDrawdown")
print(calculate_drawdown(returns).tail())

print("\nMaximum Drawdown")
print(calculate_max_drawdown(returns))

print("\nRolling Volatility")
print(calculate_rolling_volatility(returns).tail())