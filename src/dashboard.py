from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed" / "retail_sales_clean.csv"
st.set_page_config(page_title="Devixo BI Dashboard", layout="wide")
st.title("Devixo Solutions | Retail Business Intelligence")
st.caption("Interactive analysis of a simulated 10,000+ transaction retail dataset.")
df = pd.read_csv(DATA, parse_dates=["Order Date", "Ship Date"])
with st.sidebar:
    st.header("Dashboard filters")
    regions = st.multiselect("Region", sorted(df["Region"].unique()), default=sorted(df["Region"].unique()))
    categories = st.multiselect("Category", sorted(df["Category"].unique()), default=sorted(df["Category"].unique()))
    years = st.multiselect("Year", sorted(df["Year"].unique()), default=sorted(df["Year"].unique()))
d = df[df["Region"].isin(regions) & df["Category"].isin(categories) & df["Year"].isin(years)]
sales, profit = d["Sales"].sum(), d["Profit"].sum()
orders = d["Order ID"].nunique()
margin = profit / sales if sales else 0
a, b, c, e = st.columns(4)
a.metric("Total Sales", f"${sales:,.0f}")
b.metric("Total Profit", f"${profit:,.0f}")
c.metric("Profit Margin", f"{margin:.1%}")
e.metric("Orders", f"{orders:,}")
monthly = d.groupby("Year-Month", as_index=False).agg(Sales=("Sales", "sum"), Profit=("Profit", "sum"))
left, right = st.columns(2)
with left:
    st.subheader("Monthly Revenue")
    st.plotly_chart(px.line(monthly, x="Year-Month", y="Sales", markers=True), use_container_width=True)
with right:
    st.subheader("Category Comparison")
    cs = d.groupby("Category", as_index=False).agg(Sales=("Sales", "sum"), Profit=("Profit", "sum"))
    st.plotly_chart(px.bar(cs, x="Category", y=["Sales", "Profit"], barmode="group"), use_container_width=True)
left, right = st.columns(2)
with left:
    st.subheader("Regional Performance")
    rs = d.groupby("Region", as_index=False).agg(Sales=("Sales", "sum"), Profit=("Profit", "sum"))
    st.plotly_chart(px.bar(rs, x="Region", y=["Sales", "Profit"], barmode="group"), use_container_width=True)
with right:
    st.subheader("Top 10 Products by Sales")
    ps = d.groupby("Product Name", as_index=False)["Sales"].sum().nlargest(10, "Sales")
    st.plotly_chart(px.bar(ps, x="Sales", y="Product Name", orientation="h"), use_container_width=True)
st.subheader("Top 10 Customers")
tc = d.groupby("Customer ID", as_index=False).agg(Sales=("Sales", "sum"), Profit=("Profit", "sum")).nlargest(10, "Sales")
st.dataframe(tc, use_container_width=True, hide_index=True)
st.subheader("Profit Analysis")
sub = d.groupby("Sub-Category", as_index=False)["Profit"].sum().sort_values("Profit")
st.plotly_chart(px.bar(sub, x="Profit", y="Sub-Category", orientation="h"), use_container_width=True)
st.download_button("Download filtered data", d.to_csv(index=False).encode("utf-8"),
    file_name="filtered_retail_sales.csv", mime="text/csv")
