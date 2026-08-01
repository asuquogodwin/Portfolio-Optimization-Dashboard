import matplotlib.pyplot as plt

def plot_risk_return(
        results,
        max_sharpe=None,
        min_variance=None,
        frontier=None,
):
    """
    Plot simulated portfolios in risk-return space.

    Parameters
    ----------
    results : pd.DataFrame
        Simulated portfolio statistics.
    """

    plt.figure(figsize=(10, 6))

    plt.scatter(
        results["volatility"],
        results["return"],
        c=results["sharpe"],
        cmap="viridis",
        s=10,
    )

    if max_sharpe is not None:
        plt.scatter(
            max_sharpe["volatility"],
            max_sharpe["return"],
            color="gold",
            marker="*",
            s=250,
            label="Maximum Sharpe",
        )

    if min_variance is not None:
        plt.scatter(
            min_variance["volatility"],
            min_variance["return"],
            color="red",
            marker="o",
            s=120,
            label="Minimum Variance",
        )

    if frontier is not None:
        plt.plot(
            frontier["volatility"],
            frontier["return"],
            color="black",
            linewidth=2,
            label="Efficient Frontier",
        )

    plt.legend()
    plt.colorbar(label="Sharpe Ratio")

    plt.xlabel("Portfolio Volatility")
    plt.ylabel("Expected Return")
    plt.title("Simulated Portfolio Risk-Return")

    plt.show()

def plot_portfolio_weights(
    portfolio,
    asset_names,
):
    """
    Plot portfolio asset allocations.
    """

    weights = portfolio["weights"]

    plt.figure(figsize=(8, 5))

    plt.bar(
        asset_names,
        weights,
    )

    plt.xlabel("Assets")

    plt.ylabel("Weight")

    plt.title("Portfolio Allocation")

    plt.show()