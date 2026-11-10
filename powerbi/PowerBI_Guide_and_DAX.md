# Microsoft Power BI implementation guide

**Student:** Ateeb Mustapha  
**Selected BI platform:** Microsoft Power BI Desktop (not Tableau)

## 1. Prepare the data
Run the Python analysis first. It should create `data/processed/retail_sales_clean.csv`.

## 2. Import the cleaned CSV
1. Open **Power BI Desktop**.
2. Select **Home → Get data → Text/CSV**.
3. Browse to `data/processed/retail_sales_clean.csv`.
4. Select **Transform Data** if any data types need adjustment.
5. Confirm `Order Date` and `Ship Date` are Date types, `Sales` and `Profit` are Decimal Number, and `Quantity` is Whole Number.
6. Select **Close & Apply**.

## 3. Create DAX measures
Select the imported sales table, choose **Modeling → New measure**, and add these measures one at a time. If Power BI names the table differently, replace `sales` with the actual table name.

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

Format **Total Sales**, **Total Profit**, and **Average Order Value** as currency; format **Profit Margin** as a percentage.

## 4. Build report pages
### Page 1 — Executive Overview
- Card visuals: Total Sales, Total Profit, Profit Margin, Total Orders.
- Line chart: Order Date (month) against Total Sales.
- Bar chart: Total Sales by Region.
- Donut chart: Total Sales by Category.
- Slicers: Year, Region, Category.

### Page 2 — Product & Customer Analysis
- Bar chart: Top 10 Products by Total Sales.
- Bar chart or table: Top 10 Customers by Total Sales and Total Profit.
- Bar chart: Total Profit by Sub-Category.

### Page 3 — Profitability & Operations
- Column chart: Average Profit by Discount Band.
- Bar chart: Total Profit by Region.
- Bar chart: Average Delivery Days by Ship Mode (if the field is available).
- Card: Loss-Making Transactions.

## 5. Save the Power BI file
Choose **File → Save As** and save the report as:

`powerbi/Devixo_Business_Intelligence.pbix`

The `.pbix` file and screenshots must be created from Power BI Desktop; this guide is not itself a completed Power BI report.
