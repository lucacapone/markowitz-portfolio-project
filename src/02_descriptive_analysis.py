"""Create descriptive statistics and basic plots for the stock return data."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


RAW_DATA_DIR = Path("data/raw")
PROCESSED_DATA_DIR = Path("data/processed")
FIGURES_DIR = Path("figures")
TABLES_DIR = Path("outputs/tables")

ADJUSTED_CLOSE_PATH = RAW_DATA_DIR / "adjusted_close_prices.csv"
LOG_RETURNS_PATH = PROCESSED_DATA_DIR / "log_returns.csv"
DESCRIPTIVE_STATS_PATH = TABLES_DIR / "descriptive_statistics.csv"
NORMALIZED_PRICES_FIGURE_PATH = FIGURES_DIR / "normalized_prices.png"
LOG_RETURNS_FIGURE_PATH = FIGURES_DIR / "log_returns.png"


def read_time_series(path: Path) -> pd.DataFrame:
    """Read a CSV time series with dates in the first column."""
    return pd.read_csv(path, index_col=0, parse_dates=True)


def compute_descriptive_statistics(log_returns: pd.DataFrame) -> pd.DataFrame:
    """Compute descriptive statistics for daily log returns by asset."""
    return pd.DataFrame(
        {
            "mean": log_returns.mean(),
            "standard_deviation": log_returns.std(),
            "minimum": log_returns.min(),
            "maximum": log_returns.max(),
            "skewness": log_returns.skew(),
            "kurtosis": log_returns.kurtosis(),
        }
    )


def plot_normalized_prices(prices: pd.DataFrame, output_path: Path) -> None:
    """Plot adjusted close prices normalized to start at 100."""
    # Portiamo ogni serie a base 100 per confrontare performance relative.
    normalized_prices = np.multiply(prices.div(prices.iloc[0]), 100)

    # Disegniamo tutte le serie nello stesso grafico per il confronto visivo.
    ax = normalized_prices.plot(figsize=(10, 6), linewidth=1.5)
    ax.set_title("Normalized Adjusted Close Prices")
    ax.set_xlabel("Date")
    ax.set_ylabel("Normalized Price (Start = 100)")
    ax.grid(True, alpha=0.3)
    ax.legend(title="Ticker", loc="best")

    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()


def plot_log_returns(log_returns: pd.DataFrame, output_path: Path) -> None:
    """Plot daily log returns through time."""
    # Mostriamo la volatilità giornaliera dei rendimenti per ciascun titolo.
    ax = log_returns.plot(figsize=(10, 6), linewidth=1.0, alpha=0.8)
    ax.set_title("Daily Log Returns")
    ax.set_xlabel("Date")
    ax.set_ylabel("Log Return")
    ax.grid(True, alpha=0.3)
    ax.legend(title="Ticker", loc="best")

    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()


def main() -> None:
    """Run the descriptive analysis and save tables and figures."""
    # Prepariamo le cartelle per tabelle e grafici generati dallo script.
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    TABLES_DIR.mkdir(parents=True, exist_ok=True)

    # Carichiamo prezzi e rendimenti già puliti dallo script precedente.
    prices = read_time_series(ADJUSTED_CLOSE_PATH)
    log_returns = read_time_series(LOG_RETURNS_PATH)

    # Calcoliamo e salviamo le statistiche descrittive dei rendimenti.
    descriptive_statistics = compute_descriptive_statistics(log_returns)
    descriptive_statistics.to_csv(DESCRIPTIVE_STATS_PATH)

    # Produciamo i grafici principali per prezzi normalizzati e rendimenti.
    plot_normalized_prices(prices, NORMALIZED_PRICES_FIGURE_PATH)
    plot_log_returns(log_returns, LOG_RETURNS_FIGURE_PATH)

    print("Descriptive statistics for daily log returns:")
    print(descriptive_statistics)
    print("\nSaved table:")
    print(DESCRIPTIVE_STATS_PATH)
    print("\nSaved figures:")
    print(NORMALIZED_PRICES_FIGURE_PATH)
    print(LOG_RETURNS_FIGURE_PATH)


if __name__ == "__main__":
    main()
