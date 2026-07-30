import numpy as np

from src.optimizer import (
    equal_weight_portfolio,
    portfolio_return,
    portfolio_volatility,
    portfolio_sharpe_ratio,
    random_weights,
    simulate_portfolios,
    maximum_sharpe_portfolio,
    minimum_variance_portfolio,
)

weights = equal_weight_portfolio(3)

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

risk_free_rate = 0.03

print("Return:", portfolio_return(weights, expected_returns))

print("Volatility:", portfolio_volatility(weights, covariance_matrix))

print(
    "Sharpe Ratio:",
    portfolio_sharpe_ratio(
        weights,
        expected_returns,
        covariance_matrix,
        risk_free_rate,
    )
)

random_portfolio = random_weights(5)

print(random_portfolio)

print(random_portfolio.sum())



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
    num_portfolios=10,
    risk_free_rate=0.03,
)

print(results)

best = maximum_sharpe_portfolio(results)

lowest_risk = minimum_variance_portfolio(results)

print("\nMaximum Sharpe Portfolio")
print(best)

print("\nMinimum Variance Portfolio")
print(lowest_risk)