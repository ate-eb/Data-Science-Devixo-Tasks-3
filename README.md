# Retail Sales Analysis & Business Intelligence Dashboard

**Devixo Solutions — Data Science Internship**  
**Week 3 | Task 03: Business Intelligence & Dashboard Development**

**Developed by:** Ateeb Mustapha  
**BI Tool:** Microsoft Power BI Desktop  
**Dataset:** Simulated Retail Sales Dataset

---

## Project Overview

This project focuses on transforming raw retail sales data into meaningful business insights using Microsoft Power BI.

An interactive sales performance dashboard was developed to analyse revenue, profitability, order volume, product categories, regional performance, shipping methods, and product sub-categories.

The dashboard presents key business metrics through KPI cards and visualisations, making it easier to understand sales trends and compare business performance.

## Dashboard Preview

The Power BI dashboard provides a consolidated view of retail sales performance, including:

- Total Sales
- Total Profit
- Total Orders
- Profit Margin
- Sales by Year
- Sales by Product Category
- Profit by Region
- Sales by Shipping Mode
- Sales by Product Sub-Category

## Key Performance Indicators

The completed dashboard displays the following results:

| Metric | Result |
|---|---:|
| Total Sales | $2,454,256.96 |
| Total Profit | $202,386.39 |
| Total Orders | 10,000 |
| Profit Margin | 8.25% |

*These figures are from the live Power BI dashboard.*

## Tools & Technologies

- **Microsoft Power BI Desktop** — Dashboard development and visualisation
- **Power Query** — Data cleaning and preparation
- **DAX** — Calculated measures and business metrics
- **CSV** — Retail sales dataset

## Data Preparation

The retail sales dataset was imported into Power BI and prepared for analysis using Power Query.

The preparation workflow included:

- Reviewing column names and data types
- Checking date and numerical fields
- Inspecting missing values
- Reviewing duplicate records
- Preparing the data for dashboard visualisations

## Dashboard Insights

The dashboard highlights several observations:

1. Furniture contributes the highest sales among the displayed product categories.
2. Technology is the second-highest sales category.
3. West records the highest profit among the four regions.
4. South records the lowest regional profit.
5. Standard Class accounts for the largest share of sales by shipping mode.
6. The annual sales chart allows comparison across 2022–2025.
7. The sub-category chart highlights differences in sales contribution across products.

## Repository Structure

```text
Data-Science-Devixo-Tasks-3/
│
├── Ateeb_Mustapha_BI_Dashboard.pbix
├── retail_sales_raw.csv
│
├── data/
│   └── raw/
│
├── assets/
│   └── screenshots/
│
├── docs/
│
├── reports/
│
├── sql/
│
├── src/
│
└── README.md
```

The `.pbix` file contains the editable Power BI dashboard, while the CSV file contains the retail sales dataset.

The `src/` and `sql/` folders contain supplementary project materials from the earlier analysis workflow.

## How to Open the Dashboard

1. Clone or download this repository.
2. Install Microsoft Power BI Desktop.
3. Open `Ateeb_Mustapha_BI_Dashboard.pbix`.
4. If Power BI requests the source file, locate `retail_sales_raw.csv` and update the data source path if necessary.
5. Refresh the data if required.
6. Explore the dashboard visuals and available filters.

## Project Objective

The main objective of this project is to demonstrate how business intelligence tools can transform raw transactional data into an interactive reporting solution.

By combining data preparation, DAX calculations, and visual analytics, the dashboard provides a clear overview of retail business performance and supports data-driven decision-making.

## Dataset Disclaimer

The dataset used in this project is simulated and intended for educational purposes. It does not represent actual company transactions or customer information.

## Author

**Ateeb Mustapha**  
Data Science Internship — Devixo Solutions  
Week 3, Task 03

---

**Repository:** [Data-Science-Devixo-Tasks-3](https://github.com/ate-eb/Data-Science-Devixo-Tasks-3)
