import pandas as pd

def clean_prices(prices: pd.DataFrame)  -> pd.DataFrame:
    """
    Clean price data by sorting dates and removing missing values.
    """

    prices = prices.sort_index()
    prices = prices.dropna()

    return prices

def calculate_returns(prices: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate daily percentage returns.
    """

    returns = prices.pct_change().dropna()

    return returns
    