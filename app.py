import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

# Set page configuration for a professional look
st.set_page_config(
    page_title="E-commerce Sales & Customer Insights Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------------------------------
# DATA LOADING & CLEANING (Phase 1 & 2)
# ---------------------------------------------------------
@st.cache_data
def load_and_clean_data():
    try:
        # Load core CSV files
        orders = pd.read_csv('olist_orders_dataset.csv')
        order_items = pd.read_csv('olist_order_items_dataset.csv')
        customers = pd.read_csv('olist_customers_dataset.csv')
        products = pd.read_csv('olist_products_dataset.csv')
        
        # Merge datasets together based on relational keys
        df = pd.merge(order_items, orders, on='order_id', how='inner')
        df = pd.merge(df, customers, on='customer_id', how='inner')
        df = pd.merge(df, products, on='product_id', how='inner')
        
        # Clean missing values & handle dates
        df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
        df['product_category_name'] = df['product_category_name'].fillna('Unknown Category')
        
        # Filter out canceled orders to ensure clean financial calculations
        df = df[df['order_status'] != 'canceled']
        
        # Calculate total item price (price + freight)
        df['total_item_value'] = df['price'] + df['freight_value']
        
        return df
    except FileNotFoundError as e:
        st.error(f"Missing data file: {e}. Please ensure Olist CSV files are in the directory.")
        return pd.DataFrame()

df = load_and_clean_data()

if df.empty:
    st.stop()

# ---------------------------------------------------------
# SIDEBAR FILTERS (Phase 6)
# ---------------------------------------------------------
st.sidebar.header("Dashboard Filters")

min_date = df['order_purchase_timestamp'].min().date()
max_date = df['order_purchase_timestamp'].max().date()

date_range = st.sidebar.date_input(
    "Select Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# Filter dataframe based on user selection
filtered_df = df[
    (df['order_purchase_timestamp'].dt.date >= date_range[0]) & 
    (df['order_purchase_timestamp'].dt.date <= date_range[1])
]

# ---------------------------------------------------------
# KPI METRICS CALCULATION (Phase 3)
# ---------------------------------------------------------
total_revenue = filtered_df['total_item_value'].sum()
total_orders = filtered_df['order_id'].nunique()
avg_order_value = total_revenue / total_orders if total_orders > 0 else 0
repeat_customers = filtered_df.groupby('customer_id')['order_id'].nunique()
repeat_rate = (repeat_customers > 1).mean() * 100

st.title("🛍️ E-commerce Sales & Customer Insights Dashboard")
st.markdown("An interactive analytics dashboard tracking revenue drivers, customer behavior, and product performance.")

# Display KPIs in columns
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue", f"${total_revenue:,.2f}")
col2.metric("Total Orders", f"{total_orders:,}")
col3.metric("Avg Order Value (AOV)", f"${avg_order_value:,.2f}")
col4.metric("Repeat Customer Rate", f"{repeat_rate:.1f}%")

st.markdown("---")

# ---------------------------------------------------------
# VISUALIZATIONS & INSIGHTS (Phase 4 & 5)
# ---------------------------------------------------------
row1_col1, row1_col2 = st.columns(2)

with row1_col1:
    st.subheader("Monthly Revenue Trend")
    monthly_sales = filtered_df.copy()
    monthly_sales['month_year'] = monthly_sales['order_purchase_timestamp'].dt.to_period('M').astype(str)
    trend_data = monthly_sales.groupby('month_year')['total_item_value'].sum().reset_index()
    
    fig_trend = px.line(trend_data, x='month_year', y='total_item_value', markers=True, labels={'total_item_value': 'Revenue ($)', 'month_year': 'Month'})
    st.plotly_chart(fig_trend, use_container_width=True)

with row1_col2:
    st.subheader("Top 5 Product Categories by Revenue")
    top_categories = filtered_df.groupby('product_category_name')['total_item_value'].sum().reset_index()
    top_categories = top_categories.sort_values(by='total_item_value', ascending=False).head(5)
    
    fig_cat = px.bar(top_categories, x='total_item_value', y='product_category_name', orientation='h', labels={'total_item_value': 'Revenue ($)', 'product_category_name': 'Category'})
    fig_cat.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig_cat, use_container_width=True)

# ---------------------------------------------------------
# RECOMMENDATIONS (Phase 6)
# ---------------------------------------------------------
st.markdown("---")
st.subheader("💡 Data-Backed Recommendations")
st.markdown("""
- **Inventory Focus:** High-performing categories should be stocked strategically to prevent stockouts during peak ordering months.
- **Regional Targeting:** Focus marketing budgets on top-performing customer states to maximize marketing ROI.
- **Customer Retention:** Implement loyalty programs to drive up the repeat customer rate and boost long-term customer lifetime value (LTV).
""")