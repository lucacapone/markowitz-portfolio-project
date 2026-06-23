"""Compute and visualize correlations between stock returns."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats


PROCESSED_DATA_DIR = Path("data/processed")
FIGURES_DIR = Path("figures")
TABLES_DIR = Path("outputs/tables")

LOG_RETURNS_PATH = PROCESSED_DATA_DIR / "log_returns.csv"
CORRELATION_MATRIX_PATH = TABLES_DIR / "correlation_matrix.csv"
CORRELATION_PVALUES_PATH = TABLES_DIR / "correlation_pvalues.csv"
CORRELATION_PVALUES_FORMATTED_PATH = (
    TABLES_DIR / "correlation_pvalues_formatted.csv"
)
CORRELATION_SIGNIFICANCE_PATH = TABLES_DIR / "correlation_significance.csv"
CORRELATION_HEATMAP_PATH = FIGURES_DIR / "correlation_heatmap.png"


def read_log_returns(path: Path) -> pd.DataFrame:
    """Read daily log returns with dates in the first column."""
    return pd.read_csv(path, index_col=0, parse_dates=True)


def compute_correlation_matrix(log_returns: pd.DataFrame) -> pd.DataFrame:
    """Compute the Pearson correlation matrix for daily log returns."""
    return log_returns.corr(method="pearson")


def compute_pvalue_matrix(log_returns: pd.DataFrame) -> pd.DataFrame:
    """Compute Pearson correlation p-values for each pair of return series."""
    # Inizializziamo una matrice con gli stessi ticker su righe e colonne.
    p_values = pd.DataFrame(
        index=log_returns.columns,
        columns=log_returns.columns,
        dtype=float,
    )

    # Calcoliamo il p-value di Pearson per ogni coppia di asset.
    for row_name in log_returns.columns:
        for column_name in log_returns.columns:
            _, p_value = stats.pearsonr(log_returns[row_name], log_returns[column_name])
            p_values.loc[row_name, column_name] = p_value

    return p_values


def compute_significance_matrix(pvalue_matrix: pd.DataFrame) -> pd.DataFrame:
    """Convert p-values to conventional string significance markers."""
    return pvalue_matrix.map(format_significance_marker)


def compute_formatted_pvalue_matrix(pvalue_matrix: pd.DataFrame) -> pd.DataFrame:
    """Format p-values for reporting without changing numeric p-values."""
    return pvalue_matrix.map(format_pvalue_for_reporting)


def format_pvalue_for_reporting(p_value: float) -> str:
    """Return a reporting-friendly p-value string."""
    if p_value < 0.001:
        return "<0.001"
    return f"{p_value:.3f}"


def format_significance_marker(p_value: float) -> str:
    """Return a conventional significance marker for a p-value."""
    if p_value < 0.01:
        return "***"
    if p_value < 0.05:
        return "**"
    if p_value < 0.1:
        return "*"
    return ""


def plot_correlation_heatmap(
    correlation_matrix: pd.DataFrame,
    output_path: Path,
) -> None:
    """Create a matplotlib heatmap with Pearson correlation values."""
    # La scala va da -1 a 1 per rappresentare correttamente le correlazioni.
    fig, ax = plt.subplots(figsize=(8, 6))
    image = ax.imshow(correlation_matrix, cmap="coolwarm", vmin=-1, vmax=1)

    ax.set_title("Pearson Correlation Matrix of Daily Log Returns")
    ax.set_xticks(range(len(correlation_matrix.columns)))
    ax.set_xticklabels(correlation_matrix.columns, rotation=45, ha="right")
    ax.set_yticks(range(len(correlation_matrix.index)))
    ax.set_yticklabels(correlation_matrix.index)

    # Scriviamo il valore numerico dentro ogni cella della heatmap.
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
    # Prepariamo le cartelle dove salvare CSV e grafico.
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    TABLES_DIR.mkdir(parents=True, exist_ok=True)

    # Carichiamo i rendimenti e calcoliamo correlazioni, p-value e significatività.
    log_returns = read_log_returns(LOG_RETURNS_PATH)
    correlation_matrix = compute_correlation_matrix(log_returns)
    pvalue_matrix = compute_pvalue_matrix(log_returns)
    formatted_pvalue_matrix = compute_formatted_pvalue_matrix(pvalue_matrix)
    significance_matrix = compute_significance_matrix(pvalue_matrix)

    # Salviamo sia i valori numerici sia le versioni formattate per il report.
    correlation_matrix.to_csv(CORRELATION_MATRIX_PATH)
    pvalue_matrix.to_csv(CORRELATION_PVALUES_PATH)
    formatted_pvalue_matrix.to_csv(CORRELATION_PVALUES_FORMATTED_PATH)
    significance_matrix.to_csv(CORRELATION_SIGNIFICANCE_PATH)
    plot_correlation_heatmap(correlation_matrix, CORRELATION_HEATMAP_PATH)

    print("Correlation matrix:")
    print(correlation_matrix)
    print("\nP-value matrix:")
    print(pvalue_matrix)
    print("\nFormatted p-value matrix:")
    print(formatted_pvalue_matrix)
    print("\nSignificance matrix:")
    print(significance_matrix)
    print("\nSaved CSV:")
    print(CORRELATION_MATRIX_PATH)
    print(CORRELATION_PVALUES_PATH)
    print(CORRELATION_PVALUES_FORMATTED_PATH)
    print(CORRELATION_SIGNIFICANCE_PATH)
    print("\nSaved figure:")
    print(CORRELATION_HEATMAP_PATH)


if __name__ == "__main__":
    main()
