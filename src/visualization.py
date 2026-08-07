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
        color_continuous_scale="Blues",
        opacity=0.75,
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
                    color="orange",
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
                    color="purple",
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
                    color="red",
                    width=4,
                ),
            )
        )

    
    # Layout
    

    fig.update_layout(
        template="plotly_white",
        
        xaxis_title="Portfolio Volatility",
        yaxis_title="Expected Annual Return",
        legend=dict(
            orientation="h",
            y=-0.22,
            xanchor="center",
            x=0.5,
        ),
        height=500,
        width=700,
        hovermode="closest",
        margin=dict(
            l=25,
            r=25,
            t=20,
            b=25,
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
        xaxis_title="Assets",
        yaxis_title="Portfolio Weight",
        yaxis_tickformat=".0%",
        showlegend=False,
        height=500,
        width=700,
        margin=dict(
            l=25,
            r=25,
            t=20,
            b=25,
        ),
    )

    return fig

def create_correlation_heatmap(correlation_matrix):
    """
    Create an interactive correlation heatmap.
    """

    fig = px.imshow(
        correlation_matrix,
        text_auto=".2f",
        color_continuous_scale="RdBu_r",
        zmin=-1,
        zmax=1,
        aspect="auto",
    )

    fig.update_layout(
        template="plotly_white",
        height=500,
        width=500,
        margin=dict(
            l=25,
            r=25,
            t=20,
            b=25,
        ),
        coloraxis_colorbar=dict(
            title="Correlation",
        ),
    )

    return fig

def create_portfolio_growth_plot(portfolio_growth):
    """
    Create an interactive cumulative portfolio growth chart.
    """

    fig = px.line(
        portfolio_growth,
        x=portfolio_growth.index,
        y="Portfolio Value",
        labels={
            "x": "Date",
            "Portfolio Value": "Portfolio Value ($100 Initial Investment)",
        },
    )

    fig.update_traces(
        line=dict(width=3),
    )

    fig.update_layout(
        template="plotly_white",
        height=500,
        width=700,
        margin=dict(
            l=25,
            r=25,
            t=20,
            b=25,
        ),
        hovermode="x unified",
    )

    return fig