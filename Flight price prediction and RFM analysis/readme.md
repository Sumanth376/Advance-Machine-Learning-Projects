# ✈️ Flight Price Prediction and RFM Analysis

This project focuses on **predicting airline ticket prices** using machine learning techniques and analyzing customer behavior using **Recency, Frequency, Monetary (RFM)** analysis. The project utilizes historical flight booking data, including airline details, source and destination cities, flight durations, stops, and pricing. The goal is to help travelers and platforms anticipate pricing patterns and understand customer segmentation for marketing insights.

---

## 📁 Datasets

### 1. `Flight_Price_Train.xlsx`
- Training dataset with labeled flight ticket prices.
- Features include:
  - **Airline**, **Date_of_Journey**, **Source**, **Destination**
  - **Route**, **Dep_Time**, **Arrival_Time**, **Duration**
  - **Total_Stops**, **Additional_Info**
  - **Price** (Target variable)

### 2. `Flight_Price_Test.xlsx`
- Test dataset for making predictions.
- Contains all features except the **Price** column.

---

## 📊 Project Modules

### 1. 🔍 Data Preprocessing
- Handled missing values and converted date/time columns into useful features (e.g., day, month, hour).
- Cleaned inconsistent entries in the `Route` and `Duration` fields.
- Converted categorical variables into numerical format using **Label Encoding** and **One-Hot Encoding**.

### 2. 📈 Exploratory Data Analysis (EDA)
- Visualized price variation by airline, total stops, source/destination cities.
- Observed:
  - Non-stop flights are generally cheaper.
  - Airlines like Jet Airways tend to have higher average fares.
  - Night-time or early-morning departures are often less expensive.

### 3. 🔨 Feature Engineering
- Extracted features:
  - **Journey Day** and **Month**
  - **Departure and Arrival Hour/Minute**
  - **Flight Duration in Minutes**
  - Encoded categorical variables

### 4. 🤖 Model Building
- Tried multiple regression models:
  - **Linear Regression**
  - **Random Forest Regressor**
  - **XGBoost Regressor**
- Evaluated using metrics like **R² score**, **MAE**, **RMSE**
- Best performance: **Random Forest Regressor** with optimized hyperparameters.

### 5. 💸 RFM Analysis (Bonus Insight)
- Segmented customers using:
  - **Recency**: Days since last flight
  - **Frequency**: Number of flights taken
  - **Monetary**: Total spend
- Assigned RFM scores and classified into groups like **Loyal Customers**, **Big Spenders**, **At-Risk**, etc.

---

## ✅ Results

- **Best Model**: Random Forest with R² Score > 0.85
- **Feature Importance** shows total stops, airline, and duration are key predictors.
- RFM Analysis gives marketing insights for targeted offers and loyalty programs.

---

## 📦 Requirements

```bash
pandas
numpy
matplotlib
seaborn
scikit-learn
xgboost
openpyxl
