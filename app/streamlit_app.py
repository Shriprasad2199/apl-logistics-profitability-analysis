import streamlit as st
import pandas as pd
from pathlib import Path

#-------------------------------------------------------------
# Page configuration
#-------------------------------------------------------------

st.set_page_config(
    page_title="APL Logistics Profitability Analysis",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded"
)


#-------------------------------------------------------------
# Project path
#-------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PROCESSED_DATA = PROJECT_ROOT / "data" / "processed"


#-------------------------------------------------------------
# Load data
#-------------------------------------------------------------

@st.cache_data
def load_data():

    df = pd.read_csv(
        PROCESSED_DATA / "apl_logistics_eda.csv",
    )

    customer_profitability = pd.read_csv(
        PROCESSED_DATA / "customer_profitability.csv",
    )

    product_profitability = pd.read_csv(
        PROCESSED_DATA / "product_profitability.csv",
    )

    category_profitability = pd.read_csv(
        PROCESSED_DATA / "category_profitability.csv",
    )

    market_profitability = pd.read_csv(
        PROCESSED_DATA / "market_profitability.csv",
    )

    region_profitability = pd.read_csv(
        PROCESSED_DATA / "region_profitability.csv",
    )

    discount_band_analysis = pd.read_csv(
        PROCESSED_DATA / "discount_band_analysis.csv",
    )

    return (
        df,
        customer_profitability,
        product_profitability,
        category_profitability,
        market_profitability,
        region_profitability,
        discount_band_analysis,
    )

(
    
    df,
    customer_profitability,
    product_profitability,
    category_profitability,
    market_profitability,
    region_profitability,
    discount_band_analysis,
) = load_data()



#-------------------------------------------------------------
# Sidebar
#-------------------------------------------------------------

st.sidebar.title("Dashboard Filters")

st.sidebar.markdown(
    "Use the filters below to explore profitability performance."
)

# Customer Segment
customer_segments = sorted(
    df["Customer Segment"].dropna().unique().tolist()
)

selected_customer_segments = st.sidebar.multiselect(
    "Customer Segment",
    options=customer_segments,
    default=customer_segments,
)

# Category
categories = sorted(
    df["Category Name"].dropna().unique().tolist()
)

selected_categories = st.sidebar.multiselect(
    "Category",
    options=categories,
    default=categories,
)

# Product
products = sorted(
    df["Product Name"].dropna().unique().tolist()
)

selected_products = st.sidebar.multiselect(
    "Product",
    options=products,
    default=products,
)

# Market
markets = sorted(
    df["Market"].dropna().unique().tolist()
)

selected_markets = st.sidebar.multiselect(
    "Market",
    options=markets,
    default=markets
)

# Order Region
regions = sorted(
    df["Order Region"].dropna().unique().tolist()
)

selected_regions = st.sidebar.multiselect(
    "Order Region",
    options=regions,
    default=regions
)



#-------------------------------------------------------------
# Apply filters
#-------------------------------------------------------------

filtered_df = df[
    df["Customer Segment"].isin(selected_customer_segments)
    & df["Category Name"].isin(selected_categories)
    & df["Product Name"].isin(selected_products)
    & df["Market"].isin(selected_markets)
    & df["Order Region"].isin(selected_regions)
].copy()



#-------------------------------------------------------------
# Application header
#-------------------------------------------------------------

st.title("APL Logistics Profitability Analysis")

st.markdown(
    """
    ### Customer, Product, and Profitability Performance Analysis
    
    Interactive analysis of revenue, profit, customer contribution,
    product performance, discount exposure, and market and regional profitability.
    """

)

#-------------------------------------------------------------
# Data status
#-------------------------------------------------------------

st.success(
    f"Showing {len(filtered_df):,} of {len(df):,} transactions"
)


#-------------------------------------------------------------
# Overview KPIs
#-------------------------------------------------------------


st.subheader("Dashboard Overview")

total_sales = filtered_df["Sales"].sum()

total_profit = filtered_df[
    "Order Profit Per Order"
].sum()

total_discount = filtered_df[
    "Order Item Discount"
].sum()

profit_margin = (
    total_profit / total_sales
    if total_sales != 0
    else 0
)

discount_impact_ratio = (
    total_discount / total_sales
    if total_sales != 0
    else 0
)


#-------------------------------------------------------------
# Dashboard Overview KPI Cards
#-------------------------------------------------------------

st.markdown(
    """
    <style>

    .kpi-card {
        padding: 22px 24px;
        border-radius: 14px;
        min-height: 125px;
        margin-bottom: 10px;
        border: 1px solid rgba(255, 255, 255, 0.10);
        background: linear-gradient(
            135deg,
            rgba(30, 41, 59, 0.95),
            rgba(15, 23, 42, 0.95)
        );
        box-shadow: 0 4px 14px rgba(0, 0, 0, 0.18);
    }

    .kpi-title {
        font-size: 15px;
        font-weight: 600;
        color: #AEB7C4;
        margin-bottom: 12px;
    }

    .kpi-value {
        font-size: 30px;
        font-weight: 700;
        color: #F8FAFC;
        line-height: 1.2;
    }

    .kpi-description {
        font-size: 12px;
        color: #7F8A9A;
        margin-top: 9px;
    }

    .kpi-blue {
        border-left: 4px solid #3B82F6;
    }

    .kpi-green {
        border-left: 4px solid #10B981;
    }

    .kpi-amber {
        border-left: 4px solid #F59E0B;
    }

    .kpi-purple {
        border-left: 4px solid #8B5CF6;
    }

    </style>
    """,
    unsafe_allow_html=True
)


col1, col2, col3, col4 = st.columns(4)


with col1:
    st.markdown(
        f"""
        <div class="kpi-card kpi-blue">
            <div class="kpi-title">Total Revenue</div>
            <div class="kpi-value">{total_sales:,.2f}</div>
            <div class="kpi-description">Total sales value</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col2:
    st.markdown(
        f"""
        <div class="kpi-card kpi-green">
            <div class="kpi-title">Total Profit</div>
            <div class="kpi-value">{total_profit:,.2f}</div>
            <div class="kpi-description">Net profit after costs</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col3:
    st.markdown(
        f"""
        <div class="kpi-card kpi-amber">
            <div class="kpi-title">Profit Margin</div>
            <div class="kpi-value">{profit_margin * 100:.2f}%</div>
            <div class="kpi-description">Profit as a percentage of revenue</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col4:
    st.markdown(
        f"""
        <div class="kpi-card kpi-purple">
            <div class="kpi-title">Discount Impact Ratio</div>
            <div class="kpi-value">{discount_impact_ratio * 100:.2f}%</div>
            <div class="kpi-description">Discount as a percentage of revenue</div>
        </div>
        """,
        unsafe_allow_html=True
    )



#-------------------------------------------------------------
# Analysis coverage
#-------------------------------------------------------------

st.subheader("Analysis Coverage")


col1, col2, col3, col4 = st.columns(4)


with col1:
    st.markdown(
        f"""
        <div class="kpi-card kpi-blue">
            <div class="kpi-title">Transactions</div>
            <div class="kpi-value">{len(filtered_df):,}</div>
            <div class="kpi-description">Total transaction records</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col2:
    st.markdown(
        f"""
        <div class="kpi-card kpi-green">
            <div class="kpi-title">Customers</div>
            <div class="kpi-value">
                {filtered_df['Order Customer Id'].nunique():,}
            </div>
            <div class="kpi-description">Unique customers</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col3:
    st.markdown(
        f"""
        <div class="kpi-card kpi-amber">
            <div class="kpi-title">Products</div>
            <div class="kpi-value">
                {filtered_df['Product Name'].nunique():,}
            </div>
            <div class="kpi-description">Unique products</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col4:
    st.markdown(
        f"""
        <div class="kpi-card kpi-purple">
            <div class="kpi-title">Categories</div>
            <div class="kpi-value">
                {filtered_df['Category Name'].nunique():,}
            </div>
            <div class="kpi-description">Unique product categories</div>
        </div>
        """,
        unsafe_allow_html=True
    )



#-------------------------------------------------------------
# Revenue vs Profit overview
#-------------------------------------------------------------

st.subheader("Revenue & Profit Overview")

# Market-level performance based on filtered transactions

market_chart_data = (
    filtered_df
    .groupby("Market", as_index=False)
    .agg(
        Revenue=("Sales", "sum"),
        Profit=("Order Profit Per Order", "sum")
    )
)

market_chart_data["Profit_Margin"] = (
    market_chart_data["Profit"]
    / market_chart_data["Revenue"]
)


col1, col2 = st.columns(2)

with col1:

    st.markdown("#### Revenue by Market")

    revenue_chart = (
        market_chart_data
        .set_index("Market")["Revenue"]
    )

    st.bar_chart(
        revenue_chart
    )


with col2:

    st.markdown("#### Profit by Market")

    profit_chart = (
        market_chart_data
        .set_index("Market")["Profit"]
    )

    st.bar_chart(
        profit_chart
    )


#-------------------------------------------------------------
# Profit margin by Market
#-------------------------------------------------------------

st.markdown("#### Profit Margin by Market")

profit_margin_chart = (
    market_chart_data
    .set_index("Market")["Profit_Margin"]
    * 100
)

st.bar_chart(
    profit_margin_chart
)



#-------------------------------------------------------------
# Profitability status
#-------------------------------------------------------------

st.markdown("#### Transaction Profitability Status")

profitability_status = (
    filtered_df["Profitability Status"]
    .value_counts()
    .rename_axis("Status")
    .reset_index(name="Transactions")
)

st.bar_chart(
    profitability_status
    .set_index("Status")["Transactions"]
)



#-------------------------------------------------------------
# Market performance table
#-------------------------------------------------------------

st.markdown("#### Market Performance Summary")

market_display = market_chart_data.copy()

market_display["Revenue"] = (
    market_display["Revenue"].round(2)
)

market_display["Profit"] = (
    market_display["Profit"].round(2)
)

market_display["Profit_Margin"] = (
    market_display["Profit_Margin"] * 100
).round(2)

market_display = market_display.rename(
    columns={
        "Profit_Margin": "Profit Margin (%)"
    }
)

st.dataframe(
    market_display,
    use_container_width=True,
    hide_index=True
)



#-------------------------------------------------------------
# Customer Value Dashboard
#-------------------------------------------------------------

st.subheader("Customer Value Dashboard")

total_customers = customer_profitability[
    "Customer Id"
].nunique()

profitable_customers = (
    customer_profitability["Profit"] > 0
).sum()

loss_making_customers = (
    customer_profitability["Profit"] < 0
).sum()

average_customer_margin = (
    customer_profitability["Profit"].sum()
    / customer_profitability["Sales"].sum()
)



customer_card_css = """
<style>

.customer-card-container {
    display: flex;
    gap: 22px;
    margin-top: 10px;
    margin-bottom: 30px;
}

.customer-card {
    flex: 1;
    min-height: 150px;
    background: #172033;
    border: 1px solid #2b3850;
    border-radius: 18px;
    padding: 24px 26px 20px 26px;
    box-sizing: border-box;
    position: relative;
    overflow: hidden;
}

.customer-card::before {
    content: "";
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 5px;
    border-radius: 18px 0 0 18px;
}

.customer-card.blue::before {
    background: #3b82f6;
}

.customer-card.green::before {
    background: #10b981;
}

.customer-card.orange::before {
    background: #f59e0b;
}

.customer-card.purple::before {
    background: #8b5cf6;
}

.customer-card-title {
    color: #aeb8c9;
    font-size: 19px;
    font-weight: 600;
    margin-bottom: 20px;
}

.customer-card-value {
    color: #f8fafc;
    font-size: 36px;
    font-weight: 700;
    line-height: 1.1;
}

.customer-card-description {
    color: #8792a5;
    font-size: 15px;
    margin-top: 16px;
}

</style>
"""

st.markdown(customer_card_css, unsafe_allow_html=True)


customer_cards_html = f"""
<div class="customer-card-container">

<div class="customer-card blue">
        <div class="customer-card-title">
            Total Customers
        </div>
        <div class="customer-card-value">
            {total_customers:,}
        </div>
        <div class="customer-card-description">
            Unique customers in the analysis
        </div>
    </div>

<div class="customer-card green">
        <div class="customer-card-title">
            Profitable Customers
        </div>
        <div class="customer-card-value">
            {profitable_customers:,}
        </div>
        <div class="customer-card-description">
            Customers generating positive profit
        </div>
    </div>

<div class="customer-card orange">
        <div class="customer-card-title">
            Loss-making Customers
        </div>
        <div class="customer-card-value">
            {loss_making_customers:,}
        </div>
        <div class="customer-card-description">
            Customers generating negative profit
        </div>
    </div>

<div class="customer-card purple">
        <div class="customer-card-title">
            Customer Profit Margin
        </div>
        <div class="customer-card-value">
            {average_customer_margin * 100:.2f}%
        </div>
        <div class="customer-card-description">
            Profit as a percentage of customer sales
        </div>
    </div>

</div>
"""

st.markdown(
    customer_cards_html,
    unsafe_allow_html=True
)



#-------------------------------------------------------------
# Customer profitability segments
#-------------------------------------------------------------

st.markdown("### Customer Profitability Segments")

customer_segment_summary = (
    customer_profitability
    .groupby("Customer_Value_Segment")
    .agg(
        Customers=("Customer Id", "nunique"),
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
    .reset_index()
)

customer_segment_summary["Profit_Margin"] = (
    customer_segment_summary["Profit"]
    / customer_segment_summary["Sales"]
)

st.bar_chart(
    customer_segment_summary
    .set_index("Customer_Value_Segment")["Profit"]
)



#-------------------------------------------------------------
# Top customers by profit
#-------------------------------------------------------------

st.markdown("#### Top 10 Customers by Profit")

top_customers = (
    customer_profitability
    .sort_values("Profit", ascending=False)
    .head(10)
    [
        [
            "Customer Id",
            "Customer_Segment",
            "Orders",
            "Sales",
            "Profit",
            "Profit_Margin"
        ]
    ]
    .copy()
)

top_customers["Profit_Margin"] = (
    top_customers["Profit_Margin"] * 100
).round(2)

st.dataframe(
    top_customers,
    use_container_width=True,
    hide_index=True
)



#-------------------------------------------------------------
# Loss making customers
#-------------------------------------------------------------

st.markdown("#### Loss-making Customers")

loss_customers = (
    customer_profitability[
        customer_profitability["Profit"] < 0
    ]
    .sort_values("Profit")
    .head(10)
    [
        [
            "Customer Id",
            "Customer_Segment",
            "Orders",
            "Sales",
            "Profit",
            "Profit_Margin"
        ]
    ]
    .copy()
)

loss_customers["Profit_Margin"] = (
    loss_customers["Profit_Margin"] * 100
).round(2)

st.dataframe(
    loss_customers,
    use_container_width=True,
    hide_index=True
)



#-------------------------------------------------------------
# Loss making customers
#-------------------------------------------------------------

st.markdown("#### Customer Sales vs Profit")

customer_scatter = customer_profitability[
    [
        "Customer Id",
        "Sales",
        "Profit"
    ]
].copy()

st.scatter_chart(
    customer_scatter,
    x="Sales",
    y="Profit"
)

customer_sales_profit_corr = (
    customer_profitability[
        ["Sales", "Profit"]
    ]
    .corr()
    .loc["Sales", "Profit"]
)

st.caption(
    f"Customer-level Sales vs Profit correlation: "
    f"{customer_sales_profit_corr:.4f}"
)



#-------------------------------------------------------------
# Product & category performance
#-------------------------------------------------------------

st.subheader("Product & Category Performance")

total_products = product_profitability[
    "Product Name"
].nunique()

total_categories = category_profitability[
    "Category Name"
].nunique()

profitable_products = (
    product_profitability["Profit"] > 0 
).sum()

loss_making_products = (
    product_profitability["Profit"] < 0
).sum()


col1, col2, col3, col4 = st.columns(4)



with col1:
    st.markdown(
        f"""
        <div class="kpi-card kpi-blue">
            <div class="kpi-label">Products</div>
            <div class="kpi-value">{total_products:,}</div>
            <div class="kpi-description">Unique products in the analysis</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div class="kpi-card kpi-green">
            <div class="kpi-label">Categories</div>
            <div class="kpi-value">{total_categories:,}</div>
            <div class="kpi-description">Unique product categories</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        f"""
        <div class="kpi-card kpi-orange">
            <div class="kpi-label">Profitable Products</div>
            <div class="kpi-value">{profitable_products:,}</div>
            <div class="kpi-description">Products generating positive profit</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col4:
    st.markdown(
        f"""
        <div class="kpi-card kpi-purple">
            <div class="kpi-label">Loss-making Products</div>
            <div class="kpi-value">{loss_making_products:,}</div>
            <div class="kpi-description">Products generating negative profit</div>
        </div>
        """,
        unsafe_allow_html=True
    )



#-------------------------------------------------------------
# Top products by profit
#-------------------------------------------------------------

st.markdown("#### Top 10 Products by Profit")

top_products_profit = (
    product_profitability
    .sort_values("Profit", ascending=False)
    .head(10)
    [
        [
            "Product Name",
            "Category",
            "Sales",
            "Profit",
            "Profit_Margin",
            "Discount"
        ]
    ]
    .copy()
)

top_products_profit["Profit_Margin"] = (
    top_products_profit["Profit_Margin"] * 100
).round(2)

st.dataframe(
    top_products_profit,
    use_container_width=True,
    hide_index=True
)



#-------------------------------------------------------------
# Top products by revenue
#-------------------------------------------------------------

st.markdown("#### Top 10 Products by Revenue")

top_products_revenue = (
    product_profitability
    .sort_values("Sales", ascending=False)
    .head(10)
    [
        [
            "Product Name",
            "Category",
            "Sales",
            "Profit",
            "Profit_Margin",
            "Discount"
        ]
    ]
    .copy()
)

top_products_revenue["Profit_Margin"] = (
    top_products_revenue["Profit_Margin"] * 100
).round(2)

st.dataframe(
    top_products_revenue,
    use_container_width=True,
    hide_index=True
)


#-------------------------------------------------------------
# Category profitability
#-------------------------------------------------------------

st.markdown("#### Category Profitability")

category_dashboard = (
    category_profitability[
        [
            "Category Name",
            "Products",
            "Sales",
            "Profit",
            "Profit_Margin",
            "Discount"
        ]
    ]
    .sort_values("Profit", ascending=False)
    .copy()
)

category_dashboard["Profit_Margin"] = (
    category_dashboard["Profit_Margin"] * 100
).round(2)

st.dataframe(
    category_dashboard,
    use_container_width=True,
    hide_index=True
)



#-------------------------------------------------------------
# Product sales vs profit
#-------------------------------------------------------------

st.markdown("#### Product Sales vs Profit")

product_scatter = product_profitability[
    [
        "Product Name",
        "Sales",
        "Profit"
    ]
].copy()

st.scatter_chart(
    product_scatter,
    x="Sales",
    y="Profit"
)


product_sales_profit_corr = (
    product_profitability[
        ["Sales", "Profit"]
    ]
    .corr()
    .loc["Sales", "Profit"]
)

st.caption(
    f"Product-level Sales vs Profit correlation: "
    f"{product_sales_profit_corr:.4f}"
)



#-------------------------------------------------------------
# Category profitability chart
#-------------------------------------------------------------

st.markdown("#### Profitability by Product Category")

category_chart = (
    category_profitability[
        [
            "Category Name",
            "Profit"
        ]
    ]
    .sort_values("Profit", ascending=True)
    .set_index("Category Name")
)

st.bar_chart(
    category_chart
)



#-------------------------------------------------------------
# Discount Impact Analyzer
#-------------------------------------------------------------

st.subheader("Discount Impcat Analyzer")

total_discount = df["Order Item Discount"].sum()

average_discount_rate = (
    df["Order Item Discount Rate"].mean()
)

median_discount_rate = (
    df["Order Item Discount Rate"].median()
)

maximum_discount_rate = (
    df["Order Item Discount Rate"].max()
)

discount_impact_ratio = (
    total_discount / df["Sales"].sum()
)


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        f"""
        <div class="kpi-card kpi-blue">
            <div class="kpi-label">Total Discount</div>
            <div class="kpi-value">{total_discount:,.2f}</div>
            <div class="kpi-description">Total discount value applied</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div class="kpi-card kpi-green">
            <div class="kpi-label">Average Discount Rate</div>
            <div class="kpi-value">{average_discount_rate * 100:.2f}%</div>
            <div class="kpi-description">Average discount across transactions</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        f"""
        <div class="kpi-card kpi-orange">
            <div class="kpi-label">Maximum Discount Rate</div>
            <div class="kpi-value">{maximum_discount_rate * 100:.0f}%</div>
            <div class="kpi-description">Highest discount rate observed</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col4:
    st.markdown(
        f"""
        <div class="kpi-card kpi-purple">
            <div class="kpi-label">Discount Impact Ratio</div>
            <div class="kpi-value">{discount_impact_ratio * 100:.2f}%</div>
            <div class="kpi-description">Discount as a percentage of revenue</div>
        </div>
        """,
        unsafe_allow_html=True
    )




#-------------------------------------------------------------
# Profit margin by discount band
#-------------------------------------------------------------

st.markdown("#### Profit Margin by Discount Band")

discount_analysis = df.copy()


discount_analysis["Discount Band"] = pd.cut(
    discount_analysis["Order Item Discount Rate"],
    bins=[-0.001, 0, 0.05, 0.10, 0.15, 0.20, 0.25],
    labels=[
        "No Discount",
        "Low (0-5%)",
        "Moderate (5-10%)",
        "High (10-15%)",
        "Very High (15-20%)",
        "Highest (20-25%)"
    ],
    include_lowest=True
)

discount_band_summary = (
    discount_analysis
    .groupby("Discount Band", observed=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Order Profit Per Order", "sum"),
        Transaction=("Order Item Quantity", "count")
    )
    .reset_index()
)

discount_band_summary["Profit_Margin"] = (
    discount_band_summary["Profit"]
    / discount_band_summary["Sales"]
)

discount_chart = (
    discount_band_summary
    .set_index("Discount Band")["Profit_Margin"]
    * 100
)

st.bar_chart(discount_chart)




#-------------------------------------------------------------
# Discount rate vs profit margin
#-------------------------------------------------------------

st.markdown("#### Discount Rate vs Profit Margin")

discount_margin_summary = (
    df.groupby("Order Item Discount Rate")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Order Profit Per Order", "sum")
    )
    .reset_index()
)


discount_margin_summary["Profit_Margin"] = (
    discount_margin_summary["Profit"]
    / discount_margin_summary["Sales"]
)

discount_margin_chart = (
    discount_margin_summary[
        [
            "Order Item Discount Rate",
            "Profit_Margin"
        ]
    ]
    .copy()
)

discount_margin_chart["Order Item Discount Rate"] = (
    discount_margin_chart["Order Item Discount Rate"] * 100
)

discount_margin_chart["Profit_Margin"] = (
    discount_margin_chart["Profit_Margin"] * 100
)


st.line_chart(
    discount_margin_chart.set_index(
        "Order Item Discount Rate"
    )["Profit_Margin"]
)



#-------------------------------------------------------------
# High discount / low margin products
#-------------------------------------------------------------

st.subheader("High-Discount / Low-Margin Products")


# High discount = top 25% of products by average discount rate
product_discount_threshold = (
    product_profitability["Avg_Discount_Rate"].quantile(0.75)
)

# Low margin = below median product profit margin
product_margin_threshold = (
    product_profitability["Profit_Margin"].median()
)


high_discount_low_margin_products = product_profitability[
    (product_profitability["Avg_Discount_Rate"] >= product_discount_threshold) &
    (product_profitability["Profit_Margin"] < product_margin_threshold)
].copy()

# Sort from lowest margin to highest margin
high_discount_low_margin_products = (
    high_discount_low_margin_products
    .sort_values("Profit_Margin", ascending=True)
)


display_columns = [
    "Product Name",
    "Category",
    "Sales",
    "Profit",
    "Profit_Margin",
    "Avg_Discount_Rate"
]

display_df = high_discount_low_margin_products[
    display_columns
].copy()

# Convert margins and discount rates to percentages
display_df["Profit_Margin"] = (
    display_df["Profit_Margin"] * 100
).round(2)

display_df["Avg_Discount_Rate"] = (
    display_df["Avg_Discount_Rate"] * 100
).round(2)

# Rename columns for dashboard presentation
display_df = display_df.rename(
    columns={
        "Profit_Margin": "Profit_Margin (%)",
        "Avg_Discount_Rate": "Avg_Discount_Rate (%)"
    }
)


st.dataframe(
    display_df,
    width="stretch",
    hide_index=True
)


st.caption(
    f"High-discount threshold: "
    f"{product_discount_threshold * 100:.2f}% | "
    f"Low-margin threshold: "
    f"{product_margin_threshold * 100:.2f}%"
)

st.write(
    f"Products meeting the high-discount / low-margin criteria: "
    f"{len(high_discount_low_margin_products)}"
)



#-------------------------------------------------------------
# High discount / low margin categories
#-------------------------------------------------------------

st.subheader("High-Discount / Low-Margin Categories")


category_discount_threshold = (
    category_profitability["Avg_Discount_Rate"].quantile(0.75)
)

category_margin_threshold = (
    category_profitability["Profit_Margin"].median()
)


high_discount_low_margin_categories = category_profitability[
    (category_profitability["Avg_Discount_Rate"] >= category_discount_threshold) &
    (category_profitability["Profit_Margin"] < category_margin_threshold)
].copy()

high_discount_low_margin_categories = (
    high_discount_low_margin_categories
    .sort_values("Profit_Margin", ascending=True)
)


category_display_columns = [
    "Category Name",
    "Products",
    "Sales",
    "Profit",
    "Profit_Margin",
    "Avg_Discount_Rate"
]

category_display_df = high_discount_low_margin_categories[
    category_display_columns
].copy()

# Convert to percentages
category_display_df["Profit_Margin"] = (
    category_display_df["Profit_Margin"] * 100
).round(2)

category_display_df["Avg_Discount_Rate"] = (
    category_display_df["Avg_Discount_Rate"] * 100
).round(2)

# Rename columns
category_display_df = category_display_df.rename(
    columns={
        "Profit_Margin": "Profit_Margin (%)",
        "Avg_Discount_Rate": "Avg_Discount_Rate (%)"
    }
)


st.dataframe(
    category_display_df,
    width="stretch",
    hide_index=True
)


st.caption(
    f"High-discount threshold: "
    f"{category_discount_threshold * 100:.2f}% | "
    f"Low-margin threshold: "
    f"{category_margin_threshold * 100:.2f}%"
)

st.write(
    f"Categories meeting the high-discount / low-margin criteria: "
    f"{len(high_discount_low_margin_categories)}"
)




#-------------------------------------------------------------
# What if discount scenarios
#-------------------------------------------------------------

st.subheader("What-If Discount Scenario")

st.write(
    "Estimate the financial impact of changing the discount rate "
    "while keeping sales volume and other factors constant."
)



current_sales = filtered_df["Sales"].sum()

current_discount = filtered_df["Order Item Discount"].sum()

current_net_sales = filtered_df["Order Item Total"].sum()

current_profit = filtered_df["Order Profit Per Order"].sum()

current_profit_margin = (
    current_profit / current_net_sales
    if current_net_sales != 0
    else 0
)

# Current weighted discount rate
current_discount_rate = (
    current_discount / current_sales
    if current_sales != 0
    else 0
)


scenario_discount_rate = st.slider(
    "Select Scenario Discount Rate",
    min_value=0.0,
    max_value=25.0,
    value=round(current_discount_rate * 100, 1),
    step=0.5,
    format="%.1f%%"
)

scenario_discount_rate_decimal = (
    scenario_discount_rate / 100
)


scenario_discount = (
    current_sales * scenario_discount_rate_decimal
)

scenario_net_sales = (
    current_sales - scenario_discount
)

# Additional discount compared with current position
additional_discount = (
    scenario_discount - current_discount
)

# Estimate profit impact from the change in discount
scenario_profit = (
    current_profit - additional_discount
)

scenario_profit_margin = (
    scenario_profit / scenario_net_sales
    if scenario_net_sales != 0
    else 0
)

profit_change = (
    scenario_profit - current_profit
)

profit_margin_change = (
    scenario_profit_margin - current_profit_margin
)



col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Scenario Discount",
        f"{scenario_discount:,.2f}"
    )

with col2:
    st.metric(
        "Scenario Net Revenue",
        f"{scenario_net_sales:,.2f}"
    )

with col3:
    st.metric(
        "Scenario Profit",
        f"{scenario_profit:,.2f}",
        delta=f"{profit_change:,.2f}"
    )

with col4:
    st.metric(
        "Scenario Net Profit Margin",
        f"{scenario_profit_margin * 100:.2f}%",
        delta=f"{profit_margin_change * 100:+.2f} pp"
    )



scenario_comparison = pd.DataFrame({
    "Metric": [
        "Discount",
        "Net Revenue",
        "Profit",
        "Net Profit Margin"
    ],
    "Current": [
        current_discount,
        current_net_sales,
        current_profit,
        current_profit_margin * 100
    ],
    "Scenario": [
        scenario_discount,
        scenario_net_sales,
        scenario_profit,
        scenario_profit_margin * 100
    ]
})

scenario_comparison["Change"] = (
    scenario_comparison["Scenario"] -
    scenario_comparison["Current"]
)

scenario_comparison["Current"] = (
    scenario_comparison["Current"].round(2)
)

scenario_comparison["Scenario"] = (
    scenario_comparison["Scenario"].round(2)
)

scenario_comparison["Change"] = (
    scenario_comparison["Change"].round(2)
)

st.dataframe(
    scenario_comparison,
    width="stretch",
    hide_index=True
)



st.caption(
    "Scenario assumption: sales volume and other operating factors "
    "remain constant. The estimated profit change is driven only by "
    "the change in discount expenditure."
)