# Devixo Solutions — Business Intelligence & Dashboard Development

**Internship:** Data Science Internship — Week 3, Task 03  
**Student:** [Student Name]  
**Dataset:** Simulated retail sales dataset (10,000+ source rows; cleaned transaction count: 10,000)

## Project objective
Transform business transaction data into actionable insights through cleaning, feature engineering, KPI calculation, SQL analysis, and an interactive dashboard.

## Dataset note
The included CSV is an **original simulated business dataset generated for this educational project**. It is not a real company's confidential data and should not be described as real customer activity. It contains more than 5,000 transaction records and business fields such as order date, customer segment, region, category, sales, discount, quantity, and profit.

## Features
- Data cleaning: duplicate removal, missing city handling, date parsing.
- Feature engineering: year, month, year-month, profit margin, discount band, profitability flag, delivery days.
- KPIs: sales, profit, profit margin, orders, customers, average order value.
- SQL analysis using SQLite.
- Interactive Streamlit dashboard with filters and downloadable filtered data.
- Monthly revenue trend and baseline linear trend projection.
- Power BI-ready cleaned CSV, DAX measures, and report-page implementation guide.

## Technologies
Python, Pandas, NumPy, Matplotlib, Plotly, Streamlit, SQLite/SQL, Power BI (import-ready dataset + DAX guide).

## Folder structure
```text
Devixo_BI_Dashboard_Project/
├── data/
│   ├── raw/retail_sales_raw.csv
│   ├── processed/retail_sales_clean.csv
│   └── retail_sales.db
├── src/
│   ├── analysis.py
│   └── dashboard.py
├── sql/analysis_queries.sql
├── powerbi/PowerBI_Guide_and_DAX.md
├── reports/Internship_Task_03_Report.pdf
├── assets/
│   ├── charts/
│   └── screenshots/
├── docs/
└── README.md
```

## Setup
1. Install Python 3.10 or newer.
2. Open a terminal in the project folder.
3. Create and activate a virtual environment (recommended).
4. Install dependencies: `pip install -r requirements.txt`

## Run the analysis
`python src/analysis.py`

This creates the cleaned CSV and SQLite database.

## Run the interactive dashboard
`streamlit run src/dashboard.py`

The dashboard includes filters for region, category, and year. It displays KPIs, monthly revenue, category comparison, regional performance, top products, top customers, and sub-category profit.

## Run SQL
Run `src/analysis.py` first, then open `data/retail_sales.db` in a SQLite client and execute `sql/analysis_queries.sql`.

## Power BI
Import `data/processed/retail_sales_clean.csv` into Power BI Desktop and follow `powerbi/PowerBI_Guide_and_DAX.md`. Save the completed native `.pbix` report in the `powerbi/` folder before final submission.

## Results snapshot
- Total sales: $2,451,274.78
- Total profit: $202,102.15
- Profit margin: 8.2%
- Unique orders: 10,000
- Unique customers: 800

## Forecast limitation
The bonus forecast is a simple linear trend baseline based on monthly sales. It is intended as a demonstration, not a production forecast. It does not model holidays, promotions, economic conditions, or other external factors.

## Reproducibility
The synthetic dataset is generated with a fixed random seed (42) in the project preparation process. The raw and cleaned CSV files are included so the analysis can be reproduced without regenerating data.

## Source
Project brief: Devixo Solutions, Week 3 Tasks — Data Science Internship, Task 03 (provided by the student).
