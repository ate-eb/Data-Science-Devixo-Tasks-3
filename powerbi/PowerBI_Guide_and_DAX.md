# Power BI implementation guide

## Import
1. Open Power BI Desktop.
2. Select **Get data > Text/CSV**.
3. Import `data/processed/retail_sales_clean.csv`.
4. Confirm `Order Date` and `Ship Date` are Date types and numeric fields are Decimal/Whole Number.
5. Create a date table and mark it as the Date table.

## DAX measures
```DAX
Total Sales = SUM(sales[Sales])
Total Profit = SUM(sales[Profit])
Profit Margin = DIVIDE([Total Profit], [Total Sales], 0)
Total Orders = DISTINCTCOUNT(sales[Order ID])
Total Customers = DISTINCTCOUNT(sales[Customer ID])
Average Order Value = DIVIDE([Total Sales], [Total Orders], 0)
Average Discount = AVERAGE(sales[Discount])
Loss-Making Transactions = CALCULATE(COUNTROWS(sales), sales[Profit] < 0)
```

## Recommended report pages
### Executive Overview
KPI cards for sales, profit, margin and orders; monthly sales line chart; region comparison; category donut; year/region/category slicers.

### Product & Customer Analysis
Top 10 products by sales; top 10 customers by sales and profit; profit by sub-category.

### Profitability & Operations
Average profit by discount band; profit by region; average delivery days by ship mode; loss-making transaction KPI.

A native `.pbix` report must be saved from Power BI Desktop after building these pages.
