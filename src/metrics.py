import pandas as pd
import numpy as np


TRADING_DAYS = 252


def calculate_mean_returns(returns: pd.DataFrame) -> pd.Series:
    """
    Calculate the average daily return for each asset.
    """
    return returns.mean()


def calculate_volatility(returns: pd.DataFrame) -> pd.Series:
    """
    Calculate the daily volatility (standard deviation).
    """
    return returns.std()


def calculate_covariance_matrix(returns: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate the covariance matrix.
    """
    return returns.cov()


def calculate_correlation_matrix(returns: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate the correlation matrix.
    """
    return returns.corr()


def calculate_annualized_returns(
    returns: pd.DataFrame,
    trading_days: int = TRADING_DAYS,
    ) -> pd.Series:
    """
    Calculate annualized returns.
    """
    return returns.mean() * trading_days


def calculate_annualized_volatility(
    returns: pd.DataFrame,
    trading_days: int = TRADING_DAYS,
    ) -> pd.Series:
    """
    Calculate annualized volatility.
    """
    return returns.std() * np.sqrt(trading_days)


def calculate_sharpe_ratio(
    returns: pd.DataFrame,
    risk_free_rate: float = 0.02,
    trading_days: int = TRADING_DAYS,
    ) -> pd.Series:
    """
    Calculate annualized Sharpe Ratio.
    """
    annual_return = calculate_annualized_returns(returns, trading_days)
    annual_volatility = calculate_annualized_volatility(returns, trading_days)

    return (annual_return - risk_free_rate) / annual_volatility


def calculate_cumulative_returns(returns: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate cumulative returns.
    """
    return (1 + returns).cumprod()


def calculate_drawdown(returns: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate drawdown series.
    """
    cumulative = calculate_cumulative_returns(returns)
    running_max = cumulative.cummax()

    return (cumulative - running_max) / running_max


def calculate_max_drawdown(returns: pd.DataFrame) -> pd.Series:
    """
    Calculate maximum drawdown.
    """
    drawdown = calculate_drawdown(returns)

    return drawdown.min()


def calculate_rolling_volatility(
    returns: pd.DataFrame,
    window: int = 30,
    trading_days: int = TRADING_DAYS,
    ) -> pd.DataFrame:
    """
    Calculate rolling annualized volatility.
    """
    return returns.rolling(window).std() * np.sqrt(trading_days)