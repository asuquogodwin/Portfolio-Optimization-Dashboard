import numpy as np
import pandas as pd

def equal_weight_portfolio(num_assets: int) -> np.ndarray:
    """
    Create an equally weighted portfolio.

    Parameters
    ----------
    num_assets : int
        Number of assets.

    Returns
    -------
    np.ndarray
        Portfolio weights.
    """

    weights = np.ones(num_assets) / num_assets

    return weights

def portfolio_return(weights, expected_returns):
    """
    Calculate the expected return of a portfolio.

    Parameters
    ----------
    weights : np.ndarray
        Portfolio weights.

    expected_returns : np.ndarray
        Expected return of each asset.

    Returns
    -------
    float
        Portfolio expected return.
    """

    return np.dot(weights, expected_returns)

def portfolio_volatility(weights, covariance_matrix):
    """
    Calculate the portfolio volatility.

    Parameters
    ----------
    weights : np.ndarray
        Portfolio weights.

    covariance_matrix : np.ndarray
        Covariance matrix of asset returns.

    Returns
    -------
    float
        Portfolio volatility.
    """

    variance = weights.T @ covariance_matrix @ weights

    volatility = np.sqrt(variance)

    return volatility

def portfolio_sharpe_ratio(
    weights,
    expected_returns,
    covariance_matrix,
    risk_free_rate=0.0,
):
    """
    Calculate the Sharpe Ratio of a portfolio.

    Parameters
    ----------
    weights : np.ndarray
        Portfolio weights.

    expected_returns : np.ndarray
        Expected returns for each asset.

    covariance_matrix : np.ndarray
        Covariance matrix of asset returns.

    risk_free_rate : float, default=0.0
        Annual risk-free rate.

    Returns
    -------
    float
        Portfolio Sharpe Ratio.
    """

    portfolio_ret = portfolio_return(
        weights,
        expected_returns,
    )

    portfolio_vol = portfolio_volatility(
        weights,
        covariance_matrix,
    )

    sharpe = (portfolio_ret - risk_free_rate) / portfolio_vol

    return sharpe

def random_weights(num_assets: int) -> np.ndarray:
    """
    Generate random portfolio weights.

    Parameters
    ----------
    num_assets : int
        Number of assets.

    Returns
    -------
    np.ndarray
        Random portfolio weights summing to one.
    """

    weights = np.random.random(num_assets)

    weights = weights / weights.sum()

    return weights

def simulate_portfolios(
    expected_returns,
    covariance_matrix,
    num_portfolios=10000,
    risk_free_rate=0.03,
):
    """
    Simulate random portfolios and compute their
    return, volatility, and Sharpe ratio.

    Parameters
    ----------
    expected_returns : np.ndarray
        Expected returns for each asset.

    covariance_matrix : np.ndarray
        Covariance matrix.

    num_portfolios : int
        Number of portfolios to simulate.

    risk_free_rate : float
        Risk-free rate.

    Returns
    -------
    pd.DataFrame
        Portfolio statistics.
    """

    num_assets = len(expected_returns)

    results = []

    for _ in range(num_portfolios):

        weights = random_weights(num_assets)

        portfolio_ret = portfolio_return(
            weights,
            expected_returns,
        )

        portfolio_vol = portfolio_volatility(
            weights,
            covariance_matrix,
        )

        sharpe = portfolio_sharpe_ratio(
            weights,
            expected_returns,
            covariance_matrix,
            risk_free_rate,
        )

        results.append({
            "Return": portfolio_ret,
            "Volatility": portfolio_vol,
            "Sharpe": sharpe,
            "Weights": weights,
        })

    return pd.DataFrame(results)

def maximum_sharpe_portfolio(results):
    """
    Return the portfolio with the highest Sharpe Ratio.

    Parameters
    ----------
    results : pd.DataFrame
        Simulated portfolio statistics.

    Returns
    -------
    pd.Series
        Portfolio with maximum Sharpe Ratio.
    """

    return results.loc[results["Sharpe"].idxmax()]

def minimum_variance_portfolio(results):
    """
    Return the portfolio with the lowest volatility.

    Parameters
    ----------
    results : pd.DataFrame
        Simulated portfolio statistics.

    Returns
    -------
    pd.Series
        Portfolio with minimum volatility.
    """

    return results.loc[results["Volatility"].idxmin()]

