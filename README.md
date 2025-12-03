# 📊 Modeling and Forecasting Patterns in Economic Time Series Data

This repository contains the code, analyses, and predictive models developed as part of an **Undergraduate Scientific Research Project** conducted by **Gabriel Andrade do Nascimento** in the **Data Science** program at **FATEC Baixada Santista – Rubens Lara**, under the supervision of **Prof. Ms. Márcia Roberta dos Santos Pires da Silva**.

The project focuses on the **analysis and forecasting of fuel prices in Brazil** through the integration of **macroeconomic and financial variables**, using **Time Series Analysis**, **Machine Learning**, and **Exploratory Data Analysis (EDA)** techniques.

---

## 🎯 Project Objectives

### General Objective

To investigate the economic relationships between:

- Fuel prices (Gasoline, Ethanol, Diesel, and LPG);
- Exchange rates (US Dollar and Saudi Riyal);
- Global oil company stocks (Petrobras, Aramco, Chevron, and Exxon);

and to apply predictive models to forecast fuel prices.

### Specific Objectives

- Perform **detailed exploratory analysis** of historical data;
- Identify **trends, seasonality, and outliers**;
- Evaluate models using **MAE, RMSE, and MAPE** metrics;
- Integrate **macroeconomic variables** into the predictive process;
- Create **clear and interpretable visualizations**;
- Fully **document the end-to-end analytical pipeline**.

---

## 🧠 Methodology

The project follows best practices in Data Science, inspired by the **CRISP-DM** framework, covering:

1. Literature review;
2. Data collection and preprocessing;
3. Exploratory Data Analysis (EDA);
4. Predictive modeling;
5. Model evaluation;
6. Results discussion.

### Data Treatment

Two auxiliary parameters were created to improve data quality and visualization:

- **`intervalo_de_corte_outliers`**: used to smooth the time series and detect outliers;
- **`intervalo_de_agrupamento`**: used to reduce point density in plots and improve visual interpretation.

---

## 📈 Exploratory Data Analysis

Key findings during EDA:

- Strong correlation among fuel prices;
- Significant price increase starting in 2020 (COVID-19 pandemic);
- Weak relationships between exchange rates (USD and Riyal) and fuel prices;
- More relevant correlations between Diesel/LPG prices and international oil company stocks (Aramco, Chevron, and Exxon);
- High interdependence between Gasoline and Ethanol, and between Diesel and LPG.

These analyses indicate that **global market variables have greater influence on fuel prices than exchange rates alone**.

---

## 🤖 Predictive Modeling

Separate models were trained for each fuel type using **LightGBM (LGBMRegressor)**, a **Gradient Boosting-based algorithm** highly efficient for regression tasks.

### Features Used per Target

- **Gasoline**: Date, EXXON Trading Volume, ARAMCO and CHEVRON Closing Prices;
- **Ethanol**: Date, EXXON Trading Volume, ARAMCO Closing Price;
- **Diesel**: Date, EXXON Trading Volume, ARAMCO, CHEVRON, and EXXON Closing Prices;
- **LPG (GLP)**: Date, EXXON Trading Volume, ARAMCO, CHEVRON, and EXXON Closing Prices.

### Evaluation Metrics

| Fuel     | MAE  | RMSE | MAPE  |
|----------|------|------|-------|
| Gasoline | 0.03 | 0.04 | 0.49% |
| Ethanol  | 0.04 | 0.05 | 0.99% |
| Diesel   | 0.03 | 0.05 | 0.60% |
| LPG      | 0.53 | 0.69 | 0.58% |

All models achieved **MAPE below 1%**, indicating **very high predictive accuracy**.

---

## 🛠 Language, Tools, and Libraries

### Programming Language

- **Python**

### Main Libraries

- **Pandas** – Data manipulation
- **NumPy** – Numerical computing
- **Scikit-learn** – Preprocessing, metrics, and modeling
- **Statsmodels** – Statistical analysis and time series modeling
- **Matplotlib** – Data visualization
- **Seaborn** – Statistical visualization
- **LightGBM** – Gradient boosting models

### Development & Version Control

- **Visual Studio Code**
- **Git & GitHub** for version control

---

## ✅ Main Contributions

- End-to-end **time series analysis framework** applied to the energy sector;
- Identification of **global market influences** on Brazilian fuel prices;
- Highly accurate **machine learning forecasting models**;
- A **replicable analytical pipeline** for economic and financial time series studies.

---

## 📌 Final Remarks

The study shows that **international market variables (global oil company stocks) are more relevant for fuel price forecasting than exchange rates alone**. The **Machine Learning-based approach outperformed traditional models**, delivering highly accurate predictions.

Future work may include:

- Incorporation of additional macroeconomic variables (interest rates, inflation, fiscal policy);
- Use of hybrid modeling approaches;
- Exploration of **Deep Learning models for time series (LSTM, CNN)**.

---

## 👨‍💻 Author

**Gabriel Andrade do Nascimento**  
Undergraduate in Data Science – FATEC Baixada Santista

---

## 📄 License

This project is intended for **academic and educational use**. You are free to study, reuse, and extend this work, provided proper credit is given.
