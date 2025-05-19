# 🍽️ Zomato Bangalore Restaurant Analysis

This project presents an end-to-end data analysis of restaurant listings in Bangalore, India using data extracted from the Zomato platform. The goal is to explore food delivery trends, table booking preferences, location-wise customer engagement, and service patterns to provide actionable insights for restaurant business strategies.

---

## 📌 Objective

To perform exploratory data analysis (EDA) on Zomato restaurant data to uncover trends in online ordering, table booking, ratings, pricing, and locality-based restaurant performance across Bangalore.

---

## 📂 Data Sources

- `location_booktable.csv`: Contains details about restaurants that offer **table booking** services by location.
- `location_online.csv`: Contains restaurant data categorized by **online order availability** and **location**.
- Core dataset includes variables such as:
  - Restaurant name
  - Location
  - Average cost for two
  - Online order availability
  - Table booking availability
  - Ratings
  - Cuisines
  - Votes and reviews

---

## 🔍 Key Analyses Performed

### 📊 Data Cleaning & Preparation
- Removed duplicates and handled missing values.
- Standardized inconsistent location names and columns for accuracy.
- Converted data types for numerical and categorical operations.

### 📍 Location-Based Insights
- Analyzed restaurant **distribution by area/locality**.
- Identified the **top 10 locations** with the highest number of restaurants.
- Mapped **locations with high demand for online ordering and table booking**.

### 🍴 Service Type Trends
- Compared restaurants offering:
  - **Online food ordering**
  - **Table booking**
  - Both/neither
- Found customer preferences based on **location and service type**.

### ⭐ Ratings & Customer Engagement
- Examined distribution of **ratings and votes** across restaurants.
- Identified high-performing locations in terms of **ratings and popularity**.
- Correlated average cost with ratings and votes.

### 💰 Price Analysis
- Compared the **average cost for two** across different locations and cuisines.
- Segmented locations by affordability to support pricing decisions.

---

## 📈 Key Visualizations

- Bar plots of top restaurant locations
- Pie charts for service preferences (online/table booking)
- Heatmaps for correlation among numerical features
- Distribution plots for votes, ratings, and pricing
- Scatter plots comparing cost vs rating

---

## 🧠 Business Insights

- Locations like **BTM, Indiranagar, Koramangala** show high engagement and customer demand.
- Most restaurants provide **online ordering**, but **table booking** is limited to premium locations.
- High-rated restaurants tend to maintain a balance between **cost and service offerings**.
- **Mid-range pricing** (₹300–₹700) is most common and well-rated across the city.
- Online food ordering is dominant and can be leveraged for marketing and delivery expansion.

---

## 🛠️ Tools & Technologies Used

- **Python** (Pandas, NumPy, Matplotlib, Seaborn)
- **Jupyter Notebook**
- **CSV data preprocessing**
- **Exploratory Data Analysis (EDA)** techniques
- **Data visualization**

---

## ✅ Outcome

This project provides:
- A clear understanding of restaurant dynamics in Bangalore
- Data-driven insights for restaurateurs, marketers, and investors
- A framework for expanding or improving Zomato listings and services based on locality demand

---
