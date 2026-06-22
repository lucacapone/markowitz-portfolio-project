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
PORTFOLIO_SIMULATION_PATH = PORTFOLIOS_DIR / "portfolio_simulation.csv"
MINIMUM_VARIANCE_PATH = PORTFOLIOS_DIR / "minimum_variance_portfolio.csv"
MAXIMUM_SHARPE_PATH = PORTFOLIOS_DIR / "maximum_sharpe_portfolio.csv"
EFFICIENT_FRONTIER_PATH = PORTFOLIOS_DIR / "efficient_frontier.csv"
EFFICIENT_FRONTIER_FIGURE_PATH = FIGURES_DIR / "efficient_frontier.png"


def read_log_returns(path: Path) -> pd.DataFrame:
    """Read daily log returns with dates in the first column."""
    return pd.read_csv(path, index_col=0, parse_dates=True)


def annualize_returns(log_returns: pd.DataFrame) -> tuple[pd.Series, pd.DataFrame]:
    """Compute annualized expected returns and covariance matrix."""
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
    portfolio_return = float(np.dot(weights, annual_returns))
    portfolio_variance = float(
        weights.T @ annual_covariance_matrix.to_numpy() @ weights
    )
    portfolio_volatility = float(np.sqrt(portfolio_variance))
    sharpe_ratio = (portfolio_return - RISK_FREE_RATE) / portfolio_volatility
    return portfolio_return, portfolio_volatility, sharpe_ratio


def simulate_random_portfolios(
    annual_returns: pd.Series,
    annual_covariance_matrix: pd.DataFrame,
    n_portfolios: int = N_PORTFOLIOS,
) -> pd.DataFrame:
    """Generate random long-only portfolios and calculate their metrics."""
    rng = np.random.default_rng(RANDOM_SEED)
    records = []

    for _ in range(n_portfolios):
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


def build_efficient_frontier(
    annual_returns: pd.Series,
    annual_covariance_matrix: pd.DataFrame,
    n_points: int = N_FRONTIER_POINTS,
) -> pd.DataFrame:
    """Build the long-only efficient frontier using constrained optimization."""
    n_assets = len(annual_returns)
    bounds = [(0.0, 1.0)] * n_assets
    initial_weights = np.repeat(1.0 / n_assets, n_assets)
    target_returns = np.linspace(annual_returns.min(), annual_returns.max(), n_points)
    frontier_records = []

    def portfolio_volatility(weights: np.ndarray) -> float:
        return compute_portfolio_metrics(
            weights, annual_returns, annual_covariance_matrix
        )[1]

    for target_return in target_returns:
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
            # Skip rare numerical failures while keeping the frontier from valid targets.
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


def plot_efficient_frontier(
    portfolios: pd.DataFrame,
    efficient_frontier: pd.DataFrame,
    minimum_variance: pd.DataFrame,
    maximum_sharpe: pd.DataFrame,
    output_path: Path,
) -> None:
    """Plot simulated portfolios, the efficient frontier, and key portfolios."""
    fig, ax = plt.subplots(figsize=(10, 6))
    scatter = ax.scatter(
        portfolios["Volatility"],
        portfolios["Return"],
        c=portfolios["Sharpe Ratio"],
        cmap="viridis",
        s=12,
        alpha=0.5,
    )
    ax.plot(
        efficient_frontier["Volatility"],
        efficient_frontier["Return"],
        color="red",
        linewidth=2,
        label="Efficient Frontier",
    )
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
    ax.hlines(
        y=min_var_return,
        xmin=min_var_volatility,
        xmax=right_volatility,
        colors="blue",
        linestyles="--",
        linewidth=1.5,
        label="Rendimento del portafoglio a minima varianza",
    )
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
    PORTFOLIOS_DIR.mkdir(parents=True, exist_ok=True)
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    log_returns = read_log_returns(LOG_RETURNS_PATH)
    missing_tickers = set(TICKERS) - set(log_returns.columns)
    if missing_tickers:
        raise ValueError(f"Missing expected tickers: {sorted(missing_tickers)}")
    log_returns = log_returns.reindex(columns=TICKERS)
    annual_returns, annual_covariance_matrix = annualize_returns(log_returns)

    portfolios = simulate_random_portfolios(annual_returns, annual_covariance_matrix)
    minimum_variance, maximum_sharpe = find_extreme_portfolios(portfolios)
    efficient_frontier = build_efficient_frontier(annual_returns, annual_covariance_matrix)

    portfolios.to_csv(PORTFOLIO_SIMULATION_PATH, index=False)
    minimum_variance.to_csv(MINIMUM_VARIANCE_PATH, index=False)
    maximum_sharpe.to_csv(MAXIMUM_SHARPE_PATH, index=False)
    efficient_frontier.to_csv(EFFICIENT_FRONTIER_PATH, index=False)
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
    print("\nFiles created:")
    for path in (
        PORTFOLIO_SIMULATION_PATH,
        MINIMUM_VARIANCE_PATH,
        MAXIMUM_SHARPE_PATH,
        EFFICIENT_FRONTIER_PATH,
        EFFICIENT_FRONTIER_FIGURE_PATH,
    ):
        print(path)


if __name__ == "__main__":
    main()
