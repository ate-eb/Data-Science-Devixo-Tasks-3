# Dataset files

The repository currently contains a small sample CSV only. The complete synthetic raw dataset (10,012 rows), cleaned dataset (10,000 rows), and SQLite database have not been uploaded here.

The Python analysis expects the full raw dataset at `data/raw/retail_sales_raw.csv`. Add that file before running `python src/analysis.py`. The script will create `data/processed/retail_sales_clean.csv` and `data/retail_sales.db`.
