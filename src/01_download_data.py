"""Download and preprocess daily stock price data from Yahoo Finance."""

from pathlib import Path

import numpy as np
import pandas as pd
import yfinance as yf


TICKERS = ["AAPL", "JPM", "KO", "JNJ", "XOM", "BA"]
RAW_DATA_DIR = Path("data/raw")
PROCESSED_DATA_DIR = Path("data/processed")
ADJUSTED_CLOSE_PATH = RAW_DATA_DIR / "adjusted_close_prices.csv"
ADJUSTED_CLOSE_FULL_PATH = RAW_DATA_DIR / "adjusted_close_prices_full.csv"
ADJUSTED_CLOSE_TRAIN_PATH = RAW_DATA_DIR / "adjusted_close_prices_train.csv"
ADJUSTED_CLOSE_TEST_PATH = RAW_DATA_DIR / "adjusted_close_prices_test.csv"
LOG_RETURNS_PATH = PROCESSED_DATA_DIR / "log_returns.csv"
LOG_RETURNS_FULL_PATH = PROCESSED_DATA_DIR / "log_returns_full.csv"
LOG_RETURNS_TRAIN_PATH = PROCESSED_DATA_DIR / "log_returns_train.csv"
LOG_RETURNS_TEST_PATH = PROCESSED_DATA_DIR / "log_returns_test.csv"


def download_adjusted_close_prices(tickers: list[str]) -> pd.DataFrame:
    """Download daily adjusted close prices for approximately the last five years."""
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


def split_train_test_by_last_calendar_month(
    prices: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Split prices into training data and the most recent calendar month."""
    latest_date = prices.index.max()
    is_test_month = (prices.index.year == latest_date.year) & (
        prices.index.month == latest_date.month
    )

    # Exclude the final calendar month from estimation to avoid look-ahead bias:
    # it is reserved as an out-of-sample test period.
    train_prices = prices.loc[~is_test_month]
    test_prices = prices.loc[is_test_month]

    if train_prices.empty:
        raise RuntimeError("Training price sample is empty after calendar-month split.")

    if test_prices.empty:
        raise RuntimeError("Test price sample is empty after calendar-month split.")

    return train_prices, test_prices


def compute_log_returns(prices: pd.DataFrame) -> pd.DataFrame:
    """Compute daily log returns from adjusted close prices."""
    return np.log(prices / prices.shift(1)).dropna(how="any")


def print_sample_summary(label: str, sample: pd.DataFrame) -> None:
    """Print the date range and observation count for a price sample."""
    print(
        f"{label} sample date range: "
        f"{sample.index.min().date()} to {sample.index.max().date()}"
    )
    print(f"{label} sample observation count: {len(sample)}")


def main() -> None:
    """Download prices, compute log returns, save both datasets, and print a summary."""
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

    prices = download_adjusted_close_prices(TICKERS)
    train_prices, test_prices = split_train_test_by_last_calendar_month(prices)

    log_returns_full = compute_log_returns(prices)
    log_returns_train = compute_log_returns(train_prices)
    log_returns_test = compute_log_returns(test_prices)

    prices.to_csv(ADJUSTED_CLOSE_FULL_PATH)
    train_prices.to_csv(ADJUSTED_CLOSE_TRAIN_PATH)
    test_prices.to_csv(ADJUSTED_CLOSE_TEST_PATH)
    log_returns_full.to_csv(LOG_RETURNS_FULL_PATH)
    log_returns_train.to_csv(LOG_RETURNS_TRAIN_PATH)
    log_returns_test.to_csv(LOG_RETURNS_TEST_PATH)

    train_prices.to_csv(ADJUSTED_CLOSE_PATH)
    log_returns_train.to_csv(LOG_RETURNS_PATH)

    print_sample_summary("Full", prices)
    print_sample_summary("Training", train_prices)
    print_sample_summary("Test", test_prices)
    print("\nFirst rows of adjusted close prices:")
    print(train_prices.head())
    print("\nFirst rows of log returns:")
    print(log_returns_train.head())


if __name__ == "__main__":
    main()
