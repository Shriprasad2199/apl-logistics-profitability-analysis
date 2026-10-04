# Customer, Product, and Profitability Performance Analysis in Supply Chain Operations

## APL Logistics

An end-to-end data analytics project analysing customer, product, category, discount, market, and regional profitability to identify areas of financial performance and potential margin pressure.

The project combines data cleaning, financial validation, exploratory data analysis, profitability analysis, and an interactive Streamlit dashboard.

---

## Project Overview

High sales volumes do not necessarily translate into strong profitability. Discounts, product mix, customer characteristics, and regional performance can all influence the financial contribution of transactions.

This project analyses APL Logistics transaction data to provide a structured view of:

- Sales and profit performance
- Customer profitability
- Product and category profitability
- Discount exposure and margin impact
- Market and regional profitability
- Profitable and loss-making transactions

The analysis is supported by an interactive Streamlit dashboard that allows users to explore profitability performance using different business filters.

---

## Business Problem

The analysis addresses several business questions:

1. Which customers generate the highest financial contribution?
2. Which customers generate high sales but relatively low or negative profit?
3. Which products and categories contribute most to profitability?
4. Where does discount exposure create potential margin pressure?
5. Which markets and regions demonstrate stronger or weaker profitability?
6. How can profitability analysis support better pricing and customer decisions?

---

## Project Objectives

The main objectives are to:

- Clean and validate the transaction-level dataset.
- Validate key financial relationships within the data.
- Analyse overall sales, profit, discount, and margin performance.
- Identify profitable and loss-making customers.
- Evaluate product and category profitability.
- Assess discount exposure and its relationship with profit margin.
- Compare profitability across markets and regions.
- Develop an interactive dashboard for business users.
- Translate analytical findings into practical recommendations.

---

## Dataset

The project uses an APL Logistics transaction dataset containing:

- **180,519 transactions**
- **40 original variables**
- Customer information
- Product and category information
- Sales and discount measures
- Profitability measures
- Market and regional information
- Delivery and shipping information

Key financial fields include:

- `Sales`
- `Order Item Discount`
- `Order Item Total`
- `Order Profit Per Order`
- `Order Item Profit Ratio`
- `Order Item Discount Rate`
- `Order Item Quantity`

There is no currency field in the dataset, so monetary values are presented as numerical values without assigning a specific currency.

---

## Methodology

The project was completed through six analytical stages.

### 1. Data Cleaning and Financial Validation

The dataset was checked for:

- Missing values
- Duplicate records
- Invalid financial values
- Negative sales
- Negative discounts
- Invalid quantities
- Financial calculation consistency
- Category and product consistency
- Customer identifier consistency
- Text formatting and whitespace

Key financial relationships were also validated, including:

- Product price × quantity = Sales
- Sales − discount = Order Item Total
- Profit measure consistency
- Profit ratio consistency

---

### 2. Revenue and Profitability Analysis

The analysis established the overall financial baseline and examined:

- Total Sales
- Total Profit
- Total Discount
- Profit Margin
- Average transaction value
- Average profit per transaction
- Transaction profitability status
- Sales and profit relationship

Transactions were classified as:

- Profitable
- Break-even
- Loss-making

---

### 3. Customer Profitability Analysis

Customer-level profitability was analysed using:

- Sales
- Profit
- Profit Margin
- Discount
- Order volume
- Customer segment
- Market
- Delivery risk

Customers were grouped into analytical profitability segments based on revenue and profit performance.

This helped identify customers with:

- High revenue and positive profit
- Lower revenue and positive profit
- High revenue and negative profit
- Lower revenue and negative profit

---

### 4. Product and Category Profitability

Product-level and category-level analysis examined:

- Sales
- Profit
- Profit Margin
- Discount
- Units
- Orders
- Product contribution

The analysis identified products and categories with strong profitability as well as areas where higher discount exposure coincided with lower margins.

---

### 5. Discount Impact Analysis

Discount performance was analysed using:

- Average discount rate
- Median discount rate
- Maximum discount rate
- Discount Impact Ratio
- Profit Margin by Discount Band
- Discount Rate vs Profit Margin
- High-discount / low-margin products
- High-discount / low-margin categories

The analysis distinguishes between observed relationships and causal claims. The results identify areas requiring commercial review rather than claiming that discounts alone caused changes in profitability.

---

### 6. Market and Regional Analysis

Profitability was compared across:

- Markets
- Order regions
- Sales
- Profit
- Profit Margin

The analysis identified markets and regions with stronger financial performance and areas with relatively high sales but weaker margins.

---

## Key Findings

### Overall Financial Performance

- **Total Sales:** 36,784,734.31
- **Total Profit:** 3,966,902.97
- **Total Discount:** 3,730,378.40
- **Profit Margin:** 10.78%
- **Transactions:** 180,519
- **Units:** 384,079
- **Average Transaction Value:** 203.77
- **Average Profit per Transaction:** 21.97

### Transaction Profitability

- **Profitable transactions:** 80.63%
- **Loss-making transactions:** 18.71%
- **Break-even transactions:** 0.65%

Loss-making transactions generated a substantial offset against the profit generated by profitable transactions.

### Customer Profitability

The dataset contains **20,652 unique customers**.

A notable group of **6,043 high-revenue but low-margin customers** generated approximately:

- **53.67% of total sales**
- **2.48% combined profit margin**

A further **4,069 customers** were loss-making at the aggregated customer level.

### Product Performance

The dataset contains:

- **118 unique products**
- **50 product categories**

Product-level analysis identified substantial variation in sales, profit, margin, and discount exposure.

### Discount Performance

- **Average discount rate:** 10.17%
- **Maximum discount rate:** 25.00%
- **Discount Impact Ratio:** 10.14%

The profit margin was:

- **13.09%** for transactions with no discount
- **9.39%** for the highest-discount band

This represents a difference of approximately **3.71 percentage points**.

At the category level, the relationship between discount rate and profit margin was moderately negative, with a correlation of approximately **-0.451**.

### Market and Regional Performance

The analysis covered:

- **5 markets**
- **23 order regions**

No order region was identified as aggregate loss-making, although **7 regions** were classified as high-revenue and low-margin.

---

## Interactive Dashboard

The project includes a Streamlit dashboard covering:

### Dashboard Overview
- Total Sales
- Total Profit
- Profit Margin
- Discount Impact Ratio

### Revenue and Profit Overview
- Sales by market
- Profit by market
- Profit margin by market
- Transaction profitability status
- Market performance summary

### Customer Value Dashboard
- Customer profitability segments
- Top customers by profit
- Loss-making customers
- Customer Sales vs Profit

### Product and Category Performance
- Top products by profit
- Top products by sales
- Category profitability
- Product Sales vs Profit
- Category profit comparison

### Discount Impact Analyzer
- Discount exposure
- Average and maximum discount rates
- Profit margin by discount band
- Discount rate vs profit margin
- High-discount / low-margin products
- High-discount / low-margin categories

### What-If Discount Scenario

The dashboard also includes a scenario analysis tool that estimates the financial effect of changing the discount rate while holding sales volume and other factors constant.

This is a scenario analysis rather than a causal forecasting model.

---

## Key Recommendations

Based on the analysis, the following actions are recommended:

1. **Review high-revenue, low-margin customers**

   High sales contribution should not be treated as sufficient evidence of customer value. Customers generating high sales with weak or negative margins should be reviewed for pricing, discount, service, and cost-to-serve factors.

2. **Review high-discount, low-margin products and categories**

   Products and categories with relatively high discount exposure and weaker margins should be prioritised for commercial review.

3. **Strengthen customer profitability monitoring**

   Customer-level profitability should be monitored alongside sales to identify financially valuable customers and potential margin leakage.

4. **Use discount controls based on profitability**

   Discount decisions should consider expected margin contribution rather than focusing only on sales generation.

5. **Monitor market and regional margin performance**

   Market-level sales should be evaluated together with profit and margin to identify areas where revenue growth may not translate into proportional profit growth.

6. **Introduce regular profitability reporting**

   The dashboard provides a foundation for recurring monitoring of customer, product, discount, market, and regional performance.

---

## Project Structure

```text
APL-Logistics-Profitability-Analysis/
│
├── app/
│   └── streamlit_app.py
│
├── data/
│   ├── raw/
│   │   └── APL_Logistics.csv
│   │
│   └── processed/
|       |── apl_logistics_clean.csv
│       ├── apl_logistics_eda.csv
│       ├── category_profitability.csv
│       ├── customer_profitability.csv
│       ├── discount_band_analysis.csv
│       ├── high_discount_low_margin_categories.csv
│       ├── high_discount_low_margin_products.csv
│       ├── high_revenue_low_margin_markets.csv
│       ├── high_revenue_low_margin_regions.csv
│       ├── market_profitability.csv
│       ├── product_profitability.csv
│       └── region_profitability.csv
│
├── docs/
│
├── notebooks/
│   ├── 01_data_cleaning_validation.ipynb
│   ├── 02_eda_revenue_profitability.ipynb
│   ├── 03_customer_profitability.ipynb
│   ├── 04_product_category_profitability.ipynb
│   ├── 05_discount_impact_analysis.ipynb
│   └── 06_market_regional_analysis.ipynb
│
├── outputs/
│   ├── figures/
│   ├── tables/
│   └── reports/
│
├── src/
├── tests/
│
├── .gitignore
├── README.md
└── requirements.txt