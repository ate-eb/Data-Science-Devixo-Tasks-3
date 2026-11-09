from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "retail_sales_raw.csv"
OUT = ROOT / "data" / "processed"
CHARTS = ROOT / "assets" / "charts"
OUT.mkdir(parents=True, exist_ok=True)
CHARTS.mkdir(parents=True, exist_ok=True)

def load_and_clean(path=RAW):
    df = pd.read_csv(path, parse_dates=["Order Date", "Ship Date"])
    before = len(df)
    df = df.drop_duplicates().copy()
    df["City"] = df["City"].fillna("Unknown")
    df = df.dropna(subset=["Order Date", "Sales", "Profit", "Quantity"])
    df["Year"] = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.month
    df["Month Name"] = df["Order Date"].dt.strftime("%b")
    df["Year-Month"] = df["Order Date"].dt.to_period("M").astype(str)
    df["Profit Margin"] = np.where(df["Sales"] != 0, df["Profit"] / df["Sales"], 0)
    df["Discount Band"] = pd.cut(df["Discount"], [-0.001, .001, .10, .20, .30, 1.0],
        labels=["No discount", "1–10%", "11–20%", "21–30%", ">30%"])
    df["Is Profitable"] = df["Profit"] > 0
    df["Delivery Days"] = (df["Ship Date"] - df["Order Date"]).dt.days.clip(lower=0)
    print(f"Rows before cleaning: {before:,}; after cleaning: {len(df):,}")
    return df

def calculate_kpis(df):
    sales, profit = df["Sales"].sum(), df["Profit"].sum()
    return {"total_sales": sales, "total_profit": profit,
        "profit_margin": profit / sales if sales else 0,
        "orders": df["Order ID"].nunique(), "customers": df["Customer ID"].nunique(),
        "average_order_value": sales / df["Order ID"].nunique()}

def export_outputs(df):
    df.to_csv(OUT / "retail_sales_clean.csv", index=False)
    with __import__("sqlite3").connect(ROOT / "data" / "retail_sales.db") as conn:
        df.to_sql("sales", conn, if_exists="replace", index=False)
    print(calculate_kpis(df))
    print("\nCategory performance:\n", df.groupby("Category")[["Sales", "Profit"]].sum())
    print("\nRegional performance:\n", df.groupby("Region")[["Sales", "Profit"]].sum())

if __name__ == "__main__":
    export_outputs(load_and_clean())
