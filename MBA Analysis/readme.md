# 🛒 Market Basket Analysis using Apriori Algorithm

This project performs **Market Basket Analysis (MBA)** on transactional retail data to discover frequently purchased itemsets and generate actionable association rules. It leverages the **Apriori algorithm** from the `mlxtend` library to identify item combinations that occur together and compute metrics like **support**, **confidence**, and **lift**.

---

## 📁 Project Structure

- `Market Basket Analysis.ipynb` — Jupyter notebook with data preprocessing, EDA, Apriori rule mining, and visualizations.
- `MBA.xlsx` — Excel file containing processed transaction data used for analysis.
- `transactions.csv` — Raw transaction data in basket format (multiple items per transaction).

---

## 🔍 Objective

To analyze transaction data and identify:
- Most frequently bought item combinations
- Association rules that help in cross-selling and recommendation
- Business insights from customer purchasing patterns

---

## 🧠 Techniques & Tools

- **Apriori Algorithm** for frequent itemset mining
- **Association Rule Mining** (Support, Confidence, Lift)
- **Data Preprocessing** (conversion to basket format)
- **Python Libraries**:  
  `pandas`, `mlxtend`, `matplotlib`, `seaborn`

---

## 📊 Key Steps

1. **Data Preparation**
   - Read and clean the transaction data from `transactions.csv`
   - Convert to a one-hot encoded basket format for algorithm input

2. **Frequent Itemsets**
   - Apply the Apriori algorithm with varying `min_support` thresholds
   - Visualize top frequent itemsets

3. **Association Rules**
   - Generate rules with specified metrics (confidence, lift)
   - Filter rules for business-relevant combinations

4. **Visualization**
   - Bar charts of top itemsets
   - Network plots for rule visualization

---

## 📈 Example Output

- Items like `milk` and `bread` are often bought together
- Rule: `{bread} → {butter}` with high confidence and lift
- Recommendation: Offer bundle discounts or promotions based on discovered rules

---

## ✅ Business Use Case

Retailers can:
- Enhance product recommendations
- Optimize store layouts
- Create effective combo offers and pricing strategies
