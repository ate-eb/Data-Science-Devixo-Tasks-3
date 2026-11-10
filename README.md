# Devixo Solutions — Business Intelligence & Dashboard Development

**Internship:** Data Science Internship — Week 3, Task 03  
**Student:** Ateeb Mustapha  
**Selected BI platform:** Microsoft Power BI  
**Interactive application:** Streamlit dashboard  
**Dataset:** Simulated retail sales dataset (10,000+ source rows; cleaned transaction count: 10,000)

## Project objective
Transform business transaction data into actionable insights through cleaning, feature engineering, KPI calculation, SQL analysis, and an interactive dashboard.

## Dataset note
The dataset is synthetic and was generated for this educational project. It is not real company or customer data. The full project dataset is expected at `data/raw/retail_sales_raw.csv`; the repository currently includes only a small sample CSV, so the full dataset must be added before running the analysis.

## Features
- Data cleaning: duplicate removal, missing city handling, date parsing.
- Feature engineering: year, month, year-month, profit margin, discount band, profitability flag, delivery days.
- KPIs: sales, profit, profit margin, orders, customers, average order value.
- SQL analysis using SQLite.
- Interactive Streamlit dashboard with filters and downloadable filtered data.
- Monthly revenue trend and baseline linear trend projection.
- Power BI-ready cleaned CSV, DAX measures, and report-page implementation guide.

## Technologies
Python, Pandas, NumPy, Matplotlib, Plotly, Streamlit, SQLite/SQL, Microsoft Power BI.

## Folder structure
```text
data/
  raw/retail_sales_raw.csv
  processed/retail_sales_clean.csv
  retail_sales.db
src/
  analysis.py
  dashboard.py
sql/analysis_queries.sql
powerbi/PowerBI_Guide_and_DAX.md
reports/
assets/
  charts/
  screenshots/
docs/
README.md
```

## Setup and run (Windows)
1. Install Python 3.10 or newer and Microsoft Power BI Desktop.
2. Download or clone this repository and open the project folder in VS Code or File Explorer.
3. Open Command Prompt or the VS Code terminal in the project folder.
4. Create a virtual environment: `py -m venv .venv`
5. Activate it: `.venv\\Scripts\\activate`
6. Install dependencies: `python -m pip install -r requirements.txt`
7. Make sure the full synthetic dataset is present at `data/raw/retail_sales_raw.csv`.
8. Run the analysis: `python src/analysis.py`
9. Launch the interactive application: `python -m streamlit run src/dashboard.py`
10. Open the local URL printed in the terminal (usually `http://localhost:8501`).

## Power BI report
1. Run the Python analysis first so that `data/processed/retail_sales_clean.csv` exists.
2. Open Power BI Desktop.
3. Select **Get data → Text/CSV** and choose the cleaned CSV.
4. Follow `powerbi/PowerBI_Guide_and_DAX.md` to create the DAX measures and report pages.
5. Save the completed report as `powerbi/Devixo_Business_Intelligence.pbix`.

Power BI is the selected BI platform for this submission; Tableau is not used.

## Results snapshot from the completed analysis run
- Total sales: $2,451,274.78
- Total profit: $202,102.15
- Profit margin: 8.2%
- Unique orders: 10,000
- Unique customers: 800

## Screenshots and report
Live Streamlit and Power BI screenshots have not yet been captured. Save genuine screenshots in `assets/screenshots/`; do not use the static dashboard preview as evidence of a running application. The final PDF report should identify the student as **Ateeb Mustapha** and include the actual application screenshots.

## Forecast limitation
The bonus forecast is a simple linear trend baseline based on monthly sales. It is intended as a demonstration, not a production forecast. It does not model holidays, promotions, economic conditions, or other external factors.

## Source
Devixo Solutions, Week 3 Tasks — Data Science Internship, Task 03: Business Intelligence & Dashboard Development (brief supplied by the student).
