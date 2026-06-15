"""Download and preprocess daily stock price data from Yahoo Finance."""

from pathlib import Path

import numpy as np
import pandas as pd
import yfinance as yf


TICKERS = ["AAPL", "JPM", "KO", "JNJ", "XOM", "BA"]
RAW_DATA_DIR = Path("data/raw")
PROCESSED_DATA_DIR = Path("data/processed")
ADJUSTED_CLOSE_PATH = RAW_DATA_DIR / "adjusted_close_prices.csv"
LOG_RETURNS_PATH = PROCESSED_DATA_DIR / "log_returns.csv"


def download_adjusted_close_prices(tickers: list[str]) -> pd.DataFrame:
    """Download the last five years of daily adjusted close prices."""
    data = yf.download(
        tickers=tickers,
        period="5y",
        interval="1d",
        auto_adjust=False,
        progress=False,
    )

    if data.empty:
        raise RuntimeError("No data was downloaded from Yahoo Finance.")

    if isinstance(data.columns, pd.MultiIndex):
        adjusted_close = data["Adj Close"]
    else:
        adjusted_close = data[["Adj Close"]]
        adjusted_close.columns = tickers

    adjusted_close = adjusted_close.reindex(columns=tickers)
    adjusted_close.index.name = "Date"

    # Remove rows with any missing prices so every return uses the same dates.
    return adjusted_close.dropna(how="any")


def compute_log_returns(prices: pd.DataFrame) -> pd.DataFrame:
    """Compute daily log returns from adjusted close prices."""
    return np.log(prices / prices.shift(1)).dropna(how="any")


def main() -> None:
    """Download prices, compute log returns, save both datasets, and print a summary."""
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

    prices = download_adjusted_close_prices(TICKERS)
    log_returns = compute_log_returns(prices)

    prices.to_csv(ADJUSTED_CLOSE_PATH)
    log_returns.to_csv(LOG_RETURNS_PATH)

    print(f"Date range: {prices.index.min().date()} to {prices.index.max().date()}")
    print(f"Number of observations: {len(prices)}")
    print("\nFirst rows of adjusted close prices:")
    print(prices.head())
    print("\nFirst rows of log returns:")
    print(log_returns.head())


if __name__ == "__main__":
    main()
