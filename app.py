import streamlit as st
from datetime import date
import pandas as pd

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
    create_risk_return_plot,
    create_portfolio_weights_plot,
    create_correlation_heatmap,
    create_portfolio_growth_plot,
)

AVAILABLE_ASSETS = [
    "AAPL",
    "AMZN",
    "JPM",
    "MSFT",
    "NVDA",
]

@st.cache_data
def load_market_data(
    tickers,
    start_date,
    end_date,
):
    return download_data(
        tickers=tickers,
        start_date=start_date,
        end_date=end_date,
    )

st.set_page_config(
    page_title="Portfolio Optimization Dashboard",
    page_icon="📈",
    layout="wide",
)

st.title("📈 Portfolio Optimization Dashboard")

st.markdown(
    """
    Optimize a portfolio using Modern Portfolio Theory,
    Monte Carlo simulation, and the Sharpe Ratio.
    """
)

# Sidebar

st.sidebar.header("Portfolio Settings")

selected_assets = st.sidebar.multiselect(
    "Select Assets",
    options=AVAILABLE_ASSETS,
    default=AVAILABLE_ASSETS,
)

start_date = st.sidebar.date_input(
    "Start Date",
    value=date(2019, 1, 1),
)

end_date = st.sidebar.date_input(
    "End Date",
    value=date(2025, 12, 31),
)

risk_free_rate = st.sidebar.number_input(
    "Risk-Free Rate",
    min_value=0.0,
    max_value=1.0,
    value=0.03,
    step=0.01,
)

num_portfolios = st.sidebar.slider(
    "Number of Simulated Portfolios",
    min_value=1000,
    max_value=50000,
    value=10000,
    step=1000,
)

run_button = st.sidebar.button(
    "Run Optimization",
    use_container_width=True,
)

if run_button:

    try:

        with st.spinner("Running portfolio optimization..."):

            # Download market data
            raw_prices = load_market_data(
                selected_assets,
                start_date,
                end_date,
            )

            # Clean the data
            cleaned_prices = clean_prices(raw_prices)

            # Calculate returns
            returns = calculate_returns(cleaned_prices)

            #correlation matrix
            correlation_matrix = returns.corr()

            # Portfolio statistics
            expected_returns = returns.mean() * 252

            covariance_matrix = returns.cov() * 252

            asset_names = returns.columns.tolist()

            # Portfolio Optimization

            results = simulate_portfolios(
                expected_returns,
                covariance_matrix,
                num_portfolios=num_portfolios,
                risk_free_rate=risk_free_rate,
            )

            max_sharpe = maximum_sharpe_portfolio(results)
            portfolio_returns = returns.dot(max_sharpe["weights"])

            portfolio_growth = (
                (1 + portfolio_returns)
                .cumprod()
                * 100
            ).to_frame(name="Portfolio Value")
            min_variance = minimum_variance_portfolio(results)

            frontier = efficient_frontier(results)

            # Create Visualizations
        

            risk_return_fig = create_risk_return_plot(
                results,
                max_sharpe=max_sharpe,
                min_variance=min_variance,
                frontier=frontier,
            )

            weights_fig = create_portfolio_weights_plot(
            max_sharpe,
            asset_names,
            )

            correlation_fig = create_correlation_heatmap(
                correlation_matrix
            )

            growth_fig = create_portfolio_growth_plot(
                portfolio_growth
            )

            # Display Visualizations

            st.success("Portfolio optimization completed successfully!")

            st.header("Portfolio Analytics")

            metric1, metric2, metric3, metric4, metric5 = st.columns(5)

            metric1.metric(
                "Expected Return",
                f"{max_sharpe['return']:.2%}",
            )

            metric2.metric(
                "Volatility",
                f"{max_sharpe['volatility']:.2%}",
            )

            metric3.metric(
                "Sharpe Ratio",
                f"{max_sharpe['sharpe']:.2f}",
            )

            metric4.metric(
                "Assets",
                len(asset_names),
            )

            metric5.metric(
                "Simulations",
                f"{num_portfolios:,}",
            )

            st.divider()

            row1_left, row1_right = st.columns(2)

            with row1_left:

                st.subheader("Correlation Matrix")

                st.plotly_chart(
                    correlation_fig,
                    use_container_width=True,
                )

            with row1_right:

                st.subheader("Risk vs Return")

                st.plotly_chart(
                    risk_return_fig,
                    use_container_width=True,
                )

            st.divider()

            row2_left, row2_right = st.columns(2)

            with row2_left:

                st.subheader("Portfolio Growth")

                st.plotly_chart(
                    growth_fig,
                    use_container_width=True,
                )

            with row2_right:

                st.subheader("Portfolio Allocation")

                st.plotly_chart(
                    weights_fig,
                    use_container_width=True,
                )
            weights_df = pd.DataFrame(
                {
                    "Asset": asset_names,
                    "Weight": max_sharpe["weights"],
                }
            )

            weights_df["Weight"] = (
                weights_df["Weight"] * 100
            ).round(2)

            st.divider()

            st.subheader("Optimal Portfolio Weights")

            st.dataframe(
                weights_df,
                use_container_width=True,
                hide_index=True,
            )

            csv = weights_df.to_csv(index=False)

            st.download_button(
                label="📥 Download Portfolio Weights",
                data=csv,
                file_name="optimal_portfolio.csv",
                mime="text/csv",
            )
    except Exception as e:
        st.error(f"An error occurred: {e}")
    