import plotly.express as px
import plotly.graph_objects as go


def create_risk_return_plot(
    results,
    max_sharpe=None,
    min_variance=None,
    frontier=None,
):
    """
    Create an interactive Plotly risk-return scatter plot.
    """

    fig = px.scatter(
        results,
        x="volatility",
        y="return",
        color="sharpe",
        color_continuous_scale="Viridis",
        opacity=0.75,
        title="Portfolio Risk vs Return",
        labels={
            "volatility": "Portfolio Volatility",
            "return": "Expected Annual Return",
            "sharpe": "Sharpe Ratio",
        },
        hover_data={
            "return": ":.4f",
            "volatility": ":.4f",
            "sharpe": ":.4f",
        },
    )

    
    # Maximum Sharpe Portfolio
    

    if max_sharpe is not None:
        fig.add_trace(
            go.Scatter(
                x=[max_sharpe["volatility"]],
                y=[max_sharpe["return"]],
                mode="markers",
                name="Maximum Sharpe",
                marker=dict(
                    color="red",
                    size=18,
                    symbol="star",
                    line=dict(
                        color="black",
                        width=2,
                    ),
                ),
                hovertemplate=(
                    "<b>Maximum Sharpe Portfolio</b><br>"
                    "Expected Return: %{y:.2%}<br>"
                    "Volatility: %{x:.2%}<br>"
                    f"Sharpe Ratio: {max_sharpe['sharpe']:.2f}"
                    "<extra></extra>"
                ),
            )
        )

   
    # Minimum Variance Portfolio
    

    if min_variance is not None:
        fig.add_trace(
            go.Scatter(
                x=[min_variance["volatility"]],
                y=[min_variance["return"]],
                mode="markers",
                name="Minimum Variance",
                marker=dict(
                    color="green",
                    size=18,
                    symbol="diamond",
                    line=dict(
                        color="black",
                        width=2,
                    ),
                ),
                hovertemplate=(
                    "<b>Minimum Variance Portfolio</b><br>"
                    "Expected Return: %{y:.2%}<br>"
                    "Volatility: %{x:.2%}<br>"
                    f"Sharpe Ratio: {min_variance['sharpe']:.2f}"
                    "<extra></extra>"
                ),
            )
        )

    
    # Efficient Frontier
    

    if frontier is not None:
        fig.add_trace(
            go.Scatter(
                x=frontier["volatility"],
                y=frontier["return"],
                mode="lines",
                name="Efficient Frontier",
                line=dict(
                    color="black",
                    width=4,
                ),
            )
        )

    
    # Layout
    

    fig.update_layout(
        template="plotly_white",
        title=dict(
            text="Portfolio Risk vs Return",
            x=0.5,
            xanchor="center",
        ),
        xaxis_title="Portfolio Volatility",
        yaxis_title="Expected Annual Return",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
        ),
        height=700,
        width=1000,
        hovermode="closest",
        margin=dict(
            l=60,
            r=40,
            t=80,
            b=60,
        ),
    )

    return fig


def create_portfolio_weights_plot(
    portfolio,
    asset_names,
):
    """
    Create an interactive Plotly bar chart
    showing the optimal portfolio allocation.
    """

    weights = portfolio["weights"]

    fig = px.bar(
        x=asset_names,
        y=weights,
        text=[f"{weight:.2%}" for weight in weights],
        labels={
            "x": "Assets",
            "y": "Portfolio Weight",
        },
        title="Maximum Sharpe Portfolio Allocation",
    )

    fig.update_traces(
        textposition="outside",
        marker_color="royalblue",
        hovertemplate=(
            "<b>%{x}</b><br>"
            "Weight: %{y:.2%}"
            "<extra></extra>"
        ),
    )

    fig.update_layout(
        template="plotly_white",
        title=dict(
            text="Maximum Sharpe Portfolio Allocation",
            x=0.5,
            xanchor="center",
        ),
        xaxis_title="Assets",
        yaxis_title="Portfolio Weight",
        yaxis_tickformat=".0%",
        showlegend=False,
        height=600,
        width=900,
        margin=dict(
            l=60,
            r=40,
            t=80,
            b=60,
        ),
    )

    return fig