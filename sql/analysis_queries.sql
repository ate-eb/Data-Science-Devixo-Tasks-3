-- Devixo Solutions: Business Intelligence SQL queries
-- Run with SQLite against data/retail_sales.db after running src/analysis.py.
SELECT COUNT(DISTINCT "Order ID") AS total_orders, ROUND(SUM(Sales), 2) AS total_sales,
       ROUND(SUM(Profit), 2) AS total_profit, ROUND(SUM(Profit) / SUM(Sales), 4) AS profit_margin
FROM sales;
SELECT "Year-Month", ROUND(SUM(Sales),2) AS monthly_revenue FROM sales
GROUP BY "Year-Month" ORDER BY "Year-Month";
SELECT "Product Name", ROUND(SUM(Sales),2) AS revenue FROM sales
GROUP BY "Product Name" ORDER BY revenue DESC LIMIT 10;
SELECT "Customer ID", ROUND(SUM(Sales),2) AS revenue FROM sales
GROUP BY "Customer ID" ORDER BY revenue DESC LIMIT 10;
SELECT Region, ROUND(SUM(Sales),2) AS sales, ROUND(SUM(Profit),2) AS profit
FROM sales GROUP BY Region ORDER BY profit DESC;
SELECT Category, ROUND(SUM(Sales),2) AS sales, ROUND(SUM(Profit),2) AS profit,
       ROUND(SUM(Profit)/SUM(Sales),4) AS profit_margin FROM sales
GROUP BY Category ORDER BY profit DESC;
SELECT "Discount Band", COUNT(*) AS transactions, ROUND(AVG(Profit),2) AS average_profit,
       ROUND(SUM(Profit),2) AS total_profit FROM sales GROUP BY "Discount Band";
SELECT Category, "Sub-Category", ROUND(SUM(Sales),2) AS sales, ROUND(SUM(Profit),2) AS profit
FROM sales GROUP BY Category, "Sub-Category" ORDER BY profit;
SELECT "Customer Segment", ROUND(SUM(Sales),2) AS sales, ROUND(SUM(Profit),2) AS profit
FROM sales GROUP BY "Customer Segment" ORDER BY sales DESC;
SELECT "Ship Mode", ROUND(AVG("Delivery Days"),2) AS avg_delivery_days, COUNT(*) AS line_items
FROM sales GROUP BY "Ship Mode" ORDER BY avg_delivery_days;
