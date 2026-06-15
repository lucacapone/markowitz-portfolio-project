# Markowitz Portfolio Optimization Project

## Objective

Analyze six diversified stocks, compute log returns, descriptive statistics, correlations, and build efficient portfolios using the Markowitz mean-variance model.

## Stocks

- AAPL
- JPM
- KO
- JNJ
- XOM
- BA

## Data

- **Data source:** Yahoo Finance
- **Frequency:** Daily
- **Period:** Last 5 years

## Project Structure

```text
markowitz-portfolio-project/
├── data/
│   ├── raw/
│   └── processed/
├── figures/
├── outputs/
│   ├── tables/
│   └── portfolios/
├── report/
├── slides/
├── src/
│   ├── 01_download_data.py
│   ├── 02_descriptive_analysis.py
│   ├── 03_correlations.py
│   └── 04_markowitz_simulation.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Reproducible Outputs

Generated datasets, tables, portfolio outputs, and figures are intentionally not committed.
They can be reproduced from the project root by running the scripts in order:

```bash
python src/01_download_data.py
python src/02_descriptive_analysis.py
python src/03_correlations.py
python src/04_markowitz_simulation.py
```

The first script downloads adjusted close prices from Yahoo Finance and writes
`data/raw/adjusted_close_prices.csv` and `data/processed/log_returns.csv`.
The following scripts consume those files and regenerate the descriptive tables,
correlation outputs, portfolio CSV files, and figures under `outputs/` and
`figures/`.
