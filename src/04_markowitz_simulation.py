"""Build efficient portfolios using the Markowitz mean-variance model."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import minimize


TRADING_DAYS_PER_YEAR = 252
RISK_FREE_RATE = 0.0
N_PORTFOLIOS = 10_000
N_FRONTIER_POINTS = 50
RANDOM_SEED = 42
TICKERS = ["AAPL", "JPM", "KO", "JNJ", "XOM", "BA"]

PROCESSED_DATA_DIR = Path("data/processed")
PORTFOLIOS_DIR = Path("outputs/portfolios")
FIGURES_DIR = Path("figures")

LOG_RETURNS_PATH = PROCESSED_DATA_DIR / "log_returns.csv"
TEST_LOG_RETURNS_PATH = PROCESSED_DATA_DIR / "log_returns_test.csv"
PORTFOLIO_SIMULATION_PATH = PORTFOLIOS_DIR / "portfolio_simulation.csv"
MINIMUM_VARIANCE_PATH = PORTFOLIOS_DIR / "minimum_variance_portfolio.csv"
MAXIMUM_SHARPE_PATH = PORTFOLIOS_DIR / "maximum_sharpe_portfolio.csv"
EFFICIENT_FRONTIER_PATH = PORTFOLIOS_DIR / "efficient_frontier.csv"
OUT_OF_SAMPLE_EVALUATION_PATH = PORTFOLIOS_DIR / "out_of_sample_evaluation.csv"
OPTIMIZED_MINIMUM_VARIANCE_PATH = (
    PORTFOLIOS_DIR / "minimum_variance_portfolio_optimized.csv"
)
OPTIMIZED_MAXIMUM_SHARPE_PATH = (
    PORTFOLIOS_DIR / "maximum_sharpe_portfolio_optimized.csv"
)
PORTFOLIO_OPTIMIZATION_COMPARISON_PATH = (
    PORTFOLIOS_DIR / "portfolio_optimization_comparison.csv"
)
EFFICIENT_FRONTIER_FIGURE_PATH = FIGURES_DIR / "efficient_frontier.png"


def read_log_returns(path: Path) -> pd.DataFrame:
    """Read daily log returns with dates in the first column."""
    return pd.read_csv(path, index_col=0, parse_dates=True)


def validate_and_reindex_log_returns(
    log_returns: pd.DataFrame, tickers: list[str] = TICKERS
) -> pd.DataFrame:
    """Validate that expected tickers are present and order columns consistently."""
    # Verify that the dataset contains all required stocks.
    missing_tickers = set(tickers) - set(log_returns.columns)
    if missing_tickers:
        raise ValueError(f"Missing expected tickers: {sorted(missing_tickers)}")
    return log_returns.reindex(columns=tickers)


def annualize_returns(log_returns: pd.DataFrame) -> tuple[pd.Series, pd.DataFrame]:
    """Compute annualized expected returns and covariance matrix."""
    # Annualize mean and covariance assuming 252 trading days.
    mean_daily_returns = log_returns.mean()
    daily_covariance_matrix = log_returns.cov()
    return (
        mean_daily_returns * TRADING_DAYS_PER_YEAR,
        daily_covariance_matrix * TRADING_DAYS_PER_YEAR,
    )


def compute_portfolio_metrics(
    weights: np.ndarray,
    annual_returns: pd.Series,
    annual_covariance_matrix: pd.DataFrame,
) -> tuple[float, float, float]:
    """Compute annual return, volatility, and Sharpe ratio for one portfolio."""
    # Return is the weighted average of expected annual returns.
    portfolio_return = float(np.dot(weights, annual_returns))
    # Variance uses weights and the annualized covariance matrix.
    portfolio_variance = float(
        weights.T @ annual_covariance_matrix.to_numpy() @ weights
    )
    portfolio_volatility = float(np.sqrt(portfolio_variance))
    # Sharpe measures excess return per unit of risk.
    sharpe_ratio = (portfolio_return - RISK_FREE_RATE) / portfolio_volatility
    return portfolio_return, portfolio_volatility, sharpe_ratio


def simulate_random_portfolios(
    annual_returns: pd.Series,
    annual_covariance_matrix: pd.DataFrame,
    n_portfolios: int = N_PORTFOLIOS,
) -> pd.DataFrame:
    """Generate random long-only portfolios and calculate their metrics."""
    # Set the seed for reproducible simulations.
    rng = np.random.default_rng(RANDOM_SEED)
    records = []

    for _ in range(n_portfolios):
        # Generate long-only weights and normalize them to sum to 1.
        weights = rng.random(len(annual_returns))
        weights = weights / weights.sum()
        portfolio_return, portfolio_volatility, sharpe_ratio = compute_portfolio_metrics(
            weights,
            annual_returns,
            annual_covariance_matrix,
        )

        records.append(
            [portfolio_return, portfolio_volatility, sharpe_ratio, *weights]
        )

    columns = [
        "Return",
        "Volatility",
        "Sharpe Ratio",
        *[f"{ticker} weight" for ticker in annual_returns.index],
    ]
    return pd.DataFrame(records, columns=columns)


def find_extreme_portfolios(
    portfolios: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Identify the minimum variance and maximum Sharpe ratio simulated portfolios."""
    minimum_variance = portfolios.loc[[portfolios["Volatility"].idxmin()]]
    maximum_sharpe = portfolios.loc[[portfolios["Sharpe Ratio"].idxmax()]]
    return minimum_variance, maximum_sharpe


def optimize_minimum_variance_portfolio(
    annual_returns: pd.Series,
    annual_covariance_matrix: pd.DataFrame,
) -> pd.DataFrame:
    """Compute the long-only minimum variance portfolio by optimization.

    This optimized portfolio is added only as a comparison benchmark and does
    not replace the minimum variance portfolio selected from the simulations.
    """
    n_assets = len(annual_returns)
    bounds = [(0.0, 1.0)] * n_assets
    initial_weights = np.repeat(1.0 / n_assets, n_assets)
    constraints = {"type": "eq", "fun": lambda weights: np.sum(weights) - 1.0}

    def portfolio_variance(weights: np.ndarray) -> float:
        covariance_matrix = annual_covariance_matrix.to_numpy()
        return float(weights.T @ covariance_matrix @ weights)

    result = minimize(
        portfolio_variance,
        initial_weights,
        method="SLSQP",
        bounds=bounds,
        constraints=constraints,
    )

    if not result.success:
        raise ValueError(f"Minimum variance optimization failed: {result.message}")

    return build_portfolio_summary(result.x, annual_returns, annual_covariance_matrix)


def optimize_maximum_sharpe_portfolio(
    annual_returns: pd.Series,
    annual_covariance_matrix: pd.DataFrame,
) -> pd.DataFrame:
    """Compute the long-only maximum Sharpe Ratio portfolio by optimization.

    The risk-free rate is zero, consistently with the simulation. This optimized
    portfolio is added only for comparison and does not replace the simulated
    maximum Sharpe Ratio portfolio.
    """
    n_assets = len(annual_returns)
    bounds = [(0.0, 1.0)] * n_assets
    initial_weights = np.repeat(1.0 / n_assets, n_assets)
    constraints = {"type": "eq", "fun": lambda weights: np.sum(weights) - 1.0}

    def negative_sharpe_ratio(weights: np.ndarray) -> float:
        return -compute_portfolio_metrics(
            weights, annual_returns, annual_covariance_matrix
        )[2]

    result = minimize(
        negative_sharpe_ratio,
        initial_weights,
        method="SLSQP",
        bounds=bounds,
        constraints=constraints,
    )

    if not result.success:
        raise ValueError(f"Maximum Sharpe optimization failed: {result.message}")

    return build_portfolio_summary(result.x, annual_returns, annual_covariance_matrix)


def build_portfolio_summary(
    weights: np.ndarray,
    annual_returns: pd.Series,
    annual_covariance_matrix: pd.DataFrame,
) -> pd.DataFrame:
    """Create a one-row summary with metrics and weights."""
    portfolio_return, portfolio_volatility, sharpe_ratio = compute_portfolio_metrics(
        weights, annual_returns, annual_covariance_matrix
    )
    columns = [
        "Return",
        "Volatility",
        "Sharpe Ratio",
        *[f"{ticker} weight" for ticker in annual_returns.index],
    ]
    return pd.DataFrame(
        [[portfolio_return, portfolio_volatility, sharpe_ratio, *weights]],
        columns=columns,
    )


def build_portfolio_optimization_comparison(
    minimum_variance: pd.DataFrame,
    optimized_minimum_variance: pd.DataFrame,
    maximum_sharpe: pd.DataFrame,
    optimized_maximum_sharpe: pd.DataFrame,
) -> pd.DataFrame:
    """Compare simulated portfolios with the additional optimized portfolios."""
    comparison_inputs = [
        ("Simulation Minimum Variance", minimum_variance),
        ("Optimized Minimum Variance", optimized_minimum_variance),
        ("Simulation Maximum Sharpe", maximum_sharpe),
        ("Optimized Maximum Sharpe", optimized_maximum_sharpe),
    ]
    records = []

    for portfolio_name, portfolio in comparison_inputs:
        record = portfolio.iloc[0].to_dict()
        record = {"Portfolio": portfolio_name, **record}
        records.append(record)

    return pd.DataFrame(records)


def build_efficient_frontier(
    annual_returns: pd.Series,
    annual_covariance_matrix: pd.DataFrame,
    n_points: int = N_FRONTIER_POINTS,
) -> pd.DataFrame:
    """Build the long-only efficient frontier using constrained optimization."""
    n_assets = len(annual_returns)
    # Long-only bounds prevent negative weights or weights above 100%.
    bounds = [(0.0, 1.0)] * n_assets
    initial_weights = np.repeat(1.0 / n_assets, n_assets)
    # Sweep target returns to trace the efficient frontier.
    target_returns = np.linspace(annual_returns.min(), annual_returns.max(), n_points)
    frontier_records = []

    def portfolio_volatility(weights: np.ndarray) -> float:
        return compute_portfolio_metrics(
            weights, annual_returns, annual_covariance_matrix
        )[1]

    for target_return in target_returns:
        # Constrain weights to sum to 1 and return to match the current target.
        constraints = (
            {"type": "eq", "fun": lambda weights: np.sum(weights) - 1.0},
            {
                "type": "eq",
                "fun": lambda weights, target=target_return: (
                    np.dot(weights, annual_returns) - target
                ),
            },
        )
        result = minimize(
            portfolio_volatility,
            initial_weights,
            method="SLSQP",
            bounds=bounds,
            constraints=constraints,
        )

        if not result.success:
            # Skip rare numerical errors and keep valid targets.
            continue

        portfolio_return, portfolio_volatility_value, _ = compute_portfolio_metrics(
            result.x,
            annual_returns,
            annual_covariance_matrix,
        )
        frontier_records.append(
            {"Return": portfolio_return, "Volatility": portfolio_volatility_value}
        )

    return pd.DataFrame(frontier_records)


def evaluate_out_of_sample(
    portfolios: dict[str, pd.DataFrame],
    train_log_returns: pd.DataFrame,
    test_log_returns: pd.DataFrame,
) -> pd.DataFrame:
    """Evaluate optimal portfolios on the held-out test month.

    The test month is excluded from estimation and used only for ex-post
    evaluation of the portfolios selected with training data.
    """
    records = []
    # Retrieve weight columns using the same order as the training set.
    weight_columns = [f"{ticker} weight" for ticker in train_log_returns.columns]
    number_of_test_trading_days = len(test_log_returns)

    for portfolio_name, portfolio in portfolios.items():
        # Apply training-selected weights to the test month.
        weights = portfolio.loc[:, weight_columns].iloc[0].to_numpy(dtype=float)
        portfolio_mean_daily_log_return_train = float(
            np.dot(weights, train_log_returns.mean())
        )
        # Project mean daily return over the number of test days.
        expected_monthly_log_return = (
            portfolio_mean_daily_log_return_train * number_of_test_trading_days
        )
        expected_monthly_simple_return = float(
            np.exp(expected_monthly_log_return) - 1
        )
        # Sum realized daily returns to obtain the actual month.
        daily_test_portfolio_log_returns = test_log_returns.to_numpy() @ weights
        realized_monthly_log_return = float(daily_test_portfolio_log_returns.sum())
        realized_monthly_simple_return = float(np.exp(realized_monthly_log_return) - 1)
        forecast_error = realized_monthly_simple_return - expected_monthly_simple_return

        records.append(
            {
                "Portfolio": portfolio_name,
                "Expected Monthly Log Return": expected_monthly_log_return,
                "Expected Monthly Simple Return": expected_monthly_simple_return,
                "Realized Monthly Log Return": realized_monthly_log_return,
                "Realized Monthly Simple Return": realized_monthly_simple_return,
                "Forecast Error": forecast_error,
                "Number of Test Days": number_of_test_trading_days,
            }
        )

    return pd.DataFrame(records)


def plot_efficient_frontier(
    portfolios: pd.DataFrame,
    efficient_frontier: pd.DataFrame,
    minimum_variance: pd.DataFrame,
    maximum_sharpe: pd.DataFrame,
    output_path: Path,
) -> None:
    """Plot simulated portfolios, the efficient frontier, and key portfolios."""
    # Each point is a simulated portfolio, colored by Sharpe ratio.
    fig, ax = plt.subplots(figsize=(10, 6))
    scatter = ax.scatter(
        portfolios["Volatility"],
        portfolios["Return"],
        c=portfolios["Sharpe Ratio"],
        cmap="viridis",
        s=12,
        alpha=0.5,
    )
    # The red line shows efficient portfolios estimated by optimization.
    ax.plot(
        efficient_frontier["Volatility"],
        efficient_frontier["Return"],
        color="red",
        linewidth=2,
        label="Efficient Frontier",
    )
    # Highlight the minimum-risk portfolio among simulated portfolios.
    ax.scatter(
        minimum_variance["Volatility"],
        minimum_variance["Return"],
        marker="*",
        color="blue",
        s=250,
        label="Minimum Variance Portfolio",
    )
    min_var_return = float(minimum_variance["Return"].iloc[0])
    min_var_volatility = float(minimum_variance["Volatility"].iloc[0])
    right_volatility = max(
        portfolios["Volatility"].max(),
        efficient_frontier["Volatility"].max(),
    )
    # Add a horizontal guide from the minimum variance portfolio.
    ax.hlines(
        y=min_var_return,
        xmin=min_var_volatility,
        xmax=right_volatility,
        colors="blue",
        linestyles="--",
        linewidth=1.5,
        label="Rendimento del portafoglio a minima varianza",
    )
    # Highlight the portfolio with the best return-to-risk ratio.
    ax.scatter(
        maximum_sharpe["Volatility"],
        maximum_sharpe["Return"],
        marker="*",
        color="orange",
        s=250,
        label="Maximum Sharpe Portfolio",
    )

    colorbar = fig.colorbar(scatter, ax=ax)
    colorbar.set_label("Sharpe Ratio")
    ax.set_title("Markowitz Efficient Frontier")
    ax.set_xlabel("Annual Volatility")
    ax.set_ylabel("Expected Annual Return")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="best")

    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close(fig)


def main() -> None:
    """Run the Markowitz portfolio simulation and save all outputs."""
    # Prepare folders for numeric results and charts.
    PORTFOLIOS_DIR.mkdir(parents=True, exist_ok=True)
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    # Load the training set used to estimate returns and covariances.
    train_log_returns = validate_and_reindex_log_returns(
        read_log_returns(LOG_RETURNS_PATH)
    )
    # Keep the test month out of estimation and use it only for evaluation.
    test_log_returns = validate_and_reindex_log_returns(
        read_log_returns(TEST_LOG_RETURNS_PATH)
    )

    # Convert daily statistics into annualized Markowitz inputs.
    annual_returns, annual_covariance_matrix = annualize_returns(train_log_returns)

    # Simulate random portfolios and identify the most relevant ones.
    portfolios = simulate_random_portfolios(annual_returns, annual_covariance_matrix)
    minimum_variance, maximum_sharpe = find_extreme_portfolios(portfolios)
    efficient_frontier = build_efficient_frontier(annual_returns, annual_covariance_matrix)
    # Also compute optimized portfolios as an additional comparison:
    # these results do not replace portfolios identified through
    # random simulation, but allow the two approaches to be compared.
    optimized_minimum_variance = optimize_minimum_variance_portfolio(
        annual_returns, annual_covariance_matrix
    )
    optimized_maximum_sharpe = optimize_maximum_sharpe_portfolio(
        annual_returns, annual_covariance_matrix
    )
    portfolio_optimization_comparison = build_portfolio_optimization_comparison(
        minimum_variance,
        optimized_minimum_variance,
        maximum_sharpe,
        optimized_maximum_sharpe,
    )
    # Evaluate out of sample the portfolios selected on the training set.
    out_of_sample_evaluation = evaluate_out_of_sample(
        {
            "Minimum Variance Portfolio": minimum_variance,
            "Maximum Sharpe Portfolio": maximum_sharpe,
        },
        train_log_returns,
        test_log_returns,
    )

    # Save tabular outputs and the final efficient frontier figure.
    portfolios.to_csv(PORTFOLIO_SIMULATION_PATH, index=False)
    minimum_variance.to_csv(MINIMUM_VARIANCE_PATH, index=False)
    maximum_sharpe.to_csv(MAXIMUM_SHARPE_PATH, index=False)
    efficient_frontier.to_csv(EFFICIENT_FRONTIER_PATH, index=False)
    optimized_minimum_variance.to_csv(OPTIMIZED_MINIMUM_VARIANCE_PATH, index=False)
    optimized_maximum_sharpe.to_csv(OPTIMIZED_MAXIMUM_SHARPE_PATH, index=False)
    portfolio_optimization_comparison.to_csv(
        PORTFOLIO_OPTIMIZATION_COMPARISON_PATH, index=False
    )
    out_of_sample_evaluation.to_csv(OUT_OF_SAMPLE_EVALUATION_PATH, index=False)
    plot_efficient_frontier(
        portfolios,
        efficient_frontier,
        minimum_variance,
        maximum_sharpe,
        EFFICIENT_FRONTIER_FIGURE_PATH,
    )

    print("Minimum variance portfolio summary:")
    print(minimum_variance.to_string(index=False))
    print("\nMaximum Sharpe portfolio summary:")
    print(maximum_sharpe.to_string(index=False))
    print("\nPortfolio optimization comparison:")
    print(portfolio_optimization_comparison.to_string(index=False))
    print("\nOut-of-sample evaluation:")
    print(out_of_sample_evaluation.to_string(index=False))
    print("\nFiles created:")
    for path in (
        PORTFOLIO_SIMULATION_PATH,
        MINIMUM_VARIANCE_PATH,
        MAXIMUM_SHARPE_PATH,
        EFFICIENT_FRONTIER_PATH,
        OPTIMIZED_MINIMUM_VARIANCE_PATH,
        OPTIMIZED_MAXIMUM_SHARPE_PATH,
        PORTFOLIO_OPTIMIZATION_COMPARISON_PATH,
        OUT_OF_SAMPLE_EVALUATION_PATH,
        EFFICIENT_FRONTIER_FIGURE_PATH,
    ):
        print(path)


if __name__ == "__main__":
    main()
