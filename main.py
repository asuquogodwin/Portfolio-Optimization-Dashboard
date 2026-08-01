from src.data_loader import download_data

from src.preprocessing import (
    clean_prices,
    calculate_returns,
)

from src.optimizer import (
    simulate_portfolios,
    maximum_sharpe_portfolio,
    minimum_variance_portfolio,
    efficient_frontier,
)

from src.visualization import (
    plot_risk_return,
    plot_portfolio_weights,
)


# Configuration


TICKERS = [
    "AAPL",
    "AMZN",
    "JPM",
    "MSFT",
    "NVDA",
]

START_DATE = "2019-01-01"
END_DATE = "2025-12-31"

RISK_FREE_RATE = 0.03
NUM_PORTFOLIOS = 10000


# Main Application


def main():

    
    # Download market data
    
    raw_prices = download_data(
        tickers=TICKERS,
        start_date=START_DATE,
        end_date=END_DATE,
    )

    

  
    # Clean the data
    
    cleaned_prices = clean_prices(raw_prices)

    
    # Calculate daily returns
    
    returns = calculate_returns(cleaned_prices)


    # Portfolio statistics
   
    expected_returns = returns.mean() * 252


    covariance_matrix = returns.cov() * 252


    asset_names = returns.columns.tolist()


    # Portfolio Optimization
    
    results = simulate_portfolios(
        expected_returns,
        covariance_matrix,
        num_portfolios=NUM_PORTFOLIOS,
        risk_free_rate=RISK_FREE_RATE,
    )

    max_sharpe = maximum_sharpe_portfolio(results)
    min_variance = minimum_variance_portfolio(results)
    frontier = efficient_frontier(results)


    # Visualizations

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



# Program Entry Point

if __name__ == "__main__":
    main()