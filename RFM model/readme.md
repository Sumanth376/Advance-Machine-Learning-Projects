# 📊 RFM Customer Segmentation using Python

This project implements **RFM (Recency, Frequency, Monetary) Analysis** on transactional data to segment customers based on their purchasing behavior. The analysis helps businesses identify high-value customers, build targeted marketing strategies, and improve customer retention.

---

## 📁 Project Files

- `RFM.ipynb` – Jupyter notebook containing the full analysis workflow.
- `RFM Sales Data.xlsx` – Dataset of customer transactions.
- `What-is-RFM-Analysis.pptx` – Summary presentation explaining RFM methodology and key findings.

---

## 🧠 What is RFM Analysis?

**RFM** stands for:
- **Recency (R):** How recently a customer made a purchase.
- **Frequency (F):** How often a customer makes a purchase.
- **Monetary (M):** How much money the customer has spent.

Customers are scored on each metric, and the scores are combined to create meaningful segments such as:

- 🏆 **Champions**
- 💎 **Loyal Customers**
- 💤 **Hibernating**
- ⚠️ **At Risk**
- 🧪 **New Customers**
- 💔 **Lost Customers**

---

## 🔍 Objectives

- Calculate RFM scores from customer transaction data.
- Segment customers into behavior-based groups.
- Visualize customer distribution and value contribution.
- Provide actionable insights for targeted marketing.

---

## 📈 Key Steps

### 1. Data Preparation
- Loaded transactional data from `RFM Sales Data.xlsx`.
- Cleaned null values and converted dates.
- Computed R, F, M values for each customer.

### 2. RFM Scoring
- Assigned quantile-based scores (1 to 5) for R, F, and M.
- Combined into a composite `RFM_Score`.

### 3. Segmentation
- Mapped RFM scores to business-friendly labels:
  - `"555"` = **Champions**
  - `"155"` = **New Customers**
  - `"511"` = **Loyal Customers**
  - `"111"` = **Lost Customers**

### 4. Visualization
- Distribution of R, F, M scores using histograms.
- Pie chart of customer segments.
- Bar chart of revenue by segment.

---

## 📊 Sample Insights

- 💰 **Top 10% of customers generate over 50% of revenue.**
- 💤 **20% of customers are hibernating** – need reactivation campaigns.
- 🏆 **Champions and Loyalists** should be targeted with exclusive offers.
- ⚠️ **At Risk customers** are dropping off and may churn.

---

## 🛠 Tech Stack

- Python
- Pandas, NumPy
- Seaborn, Matplotlib
- Jupyter Notebook
- Excel

---

## 🚀 Business Applications

- 🎯 **Targeted marketing** by customer segment
- 🔁 **Retention strategy** for at-risk groups
- 📊 **Revenue analysis** by customer lifetime value
- 📧 **Email campaigns** personalized by RFM group
