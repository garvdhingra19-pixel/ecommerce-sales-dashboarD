# E-Commerce Sales & Customer Insights Dashboard

## Overview
This repository contains an end-to-end data analysis pipeline for an e-commerce retail dataset, transforming raw transactional records into actionable business intelligence. The project covers data cleaning, relational table integration, automated feature engineering, and exploratory data analysis (EDA) using Python, Pandas, and Plotly to evaluate revenue drivers, customer behavior, and regional performance patterns.

## Key Objectives & Methodology
1. **Data Integration & Relational Merging:** Combined multiple relational tables including customer data, order details, item pricing, and product categories into a unified master dataset containing 112,650 rows.
2. **Data Cleaning & Quality Control:** Filtered out incomplete or unfulfilled orders, focusing specifically on successfully delivered transactions and dropping rows with null pricing parameters.
3. **Feature Engineering & Core KPIs:** Developed derived metrics including total line-item revenue (price plus freight), Average Order Value (AOV), unique customer tracking, and the repeat-customer rate.
4. **Exploratory Data Analysis & Visualization:** Built interactive visualizations using Plotly to analyze monthly revenue trajectories, top-performing product categories, and geographic concentrations across states.
5. **Strategic Recommendations:** Synthesized quantitative outputs into prioritized, data-backed operational strategies for executive decision-making.

## Key Performance Indicators (KPIs) & Metrics
* **Total Revenue:** R$ 15,419,773.75
* **Total Unique Orders:** 96,478
* **Average Order Value (AOV):** R$ 159.83
* **Total Unique Customers:** 93,358
* **Repeat Customer Rate:** 3.00%

## Exploratory Data Analysis & Visualizations
* **Monthly Sales Trends:** Tracks top-line revenue growth across historical operating months, highlighting seasonal surges and marketplace scaling.
* **Top Product Categories:** Identifies leading revenue-generating merchandise categories, such as health and beauty (`beleza_saude`) and watches (`relogios_presentes`).
* **Regional State Distribution:** Evaluates geographic revenue concentrations, revealing that São Paulo (SP) dominates transactional volume with over R$ 5.7M, followed by Rio de Janeiro (RJ) and Minas Gerais (MG).
* **Logistics Performance Overview:** Incorporates delivery timestamp metrics to segment delivery outcomes into on-time arrivals versus delayed shipments.

## Strategic Business Recommendations
* **Geographic Resource Allocation:** Because a significant majority of total revenue originates from southeast metropolitan hubs like São Paulo and Rio de Janeiro, marketing budgets and inventory staging should be concentrated in these regions to maximize return on investment.
* **Inventory Optimization:** High-demand product categories require proactive stock management to prevent stockouts during peak sales periods.
* **Customer Retention Initiatives:** Given a repeat customer rate of approximately 3.00%, the enterprise relies heavily on acquisition rather than retention; introducing structured post-purchase loyalty programs and automated email marketing campaigns is vital for boosting lifetime customer value.

## Tech Stack
* **Python** (Pandas, NumPy)
* **Google Colab** (Execution environment)
* **Plotly** (Interactive data visualization)