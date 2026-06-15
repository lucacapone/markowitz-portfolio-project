"""Compute and visualize correlations between stock returns."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


PROCESSED_DATA_DIR = Path("data/processed")
FIGURES_DIR = Path("figures")
TABLES_DIR = Path("outputs/tables")

LOG_RETURNS_PATH = PROCESSED_DATA_DIR / "log_returns.csv"
CORRELATION_MATRIX_PATH = TABLES_DIR / "correlation_matrix.csv"
CORRELATION_HEATMAP_PATH = FIGURES_DIR / "correlation_heatmap.png"


def read_log_returns(path: Path) -> pd.DataFrame:
    """Read daily log returns with dates in the first column."""
    return pd.read_csv(path, index_col=0, parse_dates=True)


def compute_correlation_matrix(log_returns: pd.DataFrame) -> pd.DataFrame:
    """Compute the Pearson correlation matrix for daily log returns."""
    return log_returns.corr(method="pearson")


def plot_correlation_heatmap(correlation_matrix: pd.DataFrame, output_path: Path) -> None:
    """Create a matplotlib heatmap with correlation values in each cell."""
    fig, ax = plt.subplots(figsize=(8, 6))
    image = ax.imshow(correlation_matrix, cmap="coolwarm", vmin=-1, vmax=1)

    ax.set_title("Pearson Correlation Matrix of Daily Log Returns")
    ax.set_xticks(range(len(correlation_matrix.columns)))
    ax.set_xticklabels(correlation_matrix.columns, rotation=45, ha="right")
    ax.set_yticks(range(len(correlation_matrix.index)))
    ax.set_yticklabels(correlation_matrix.index)

    for row_index, row_name in enumerate(correlation_matrix.index):
        for column_index, column_name in enumerate(correlation_matrix.columns):
            value = correlation_matrix.loc[row_name, column_name]
            ax.text(
                column_index,
                row_index,
                f"{value:.2f}",
                ha="center",
                va="center",
                color="black",
            )

    colorbar = fig.colorbar(image, ax=ax)
    colorbar.set_label("Pearson correlation")

    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close(fig)


def main() -> None:
    """Compute correlations for log returns and save the table and heatmap."""
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    TABLES_DIR.mkdir(parents=True, exist_ok=True)

    log_returns = read_log_returns(LOG_RETURNS_PATH)
    correlation_matrix = compute_correlation_matrix(log_returns)

    correlation_matrix.to_csv(CORRELATION_MATRIX_PATH)
    plot_correlation_heatmap(correlation_matrix, CORRELATION_HEATMAP_PATH)

    print("Correlation matrix:")
    print(correlation_matrix)
    print("\nSaved CSV:")
    print(CORRELATION_MATRIX_PATH)
    print("\nSaved figure:")
    print(CORRELATION_HEATMAP_PATH)


if __name__ == "__main__":
    main()
