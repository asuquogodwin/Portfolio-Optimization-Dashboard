import numpy as np

from src.optimizer import (
    simulate_portfolios,
    maximum_sharpe_portfolio,
    minimum_variance_portfolio,
    efficient_frontier,
)

asset_names = [
    "Asset 1",
    "Asset 2",
    "Asset 3",
]

from src.visualization import plot_risk_return
from src.visualization import plot_portfolio_weights

expected_returns = np.array([
    0.12,
    0.10,
    0.18
])

covariance_matrix = np.array([
    [0.040, 0.018, 0.022],
    [0.018, 0.030, 0.020],
    [0.022, 0.020, 0.090]
])

results = simulate_portfolios(
    expected_returns,
    covariance_matrix,
    num_portfolios=10000,
    risk_free_rate=0.03,
)

max_sharpe = maximum_sharpe_portfolio(results)
min_variance = minimum_variance_portfolio(results)
frontier = efficient_frontier(results)

plot_risk_return(
    results,
    max_sharpe=max_sharpe,
    min_variance=min_variance,
    frontier=frontier,
)

plot_portfolio_weights(
    max_sharpe,
    asset_names,
)