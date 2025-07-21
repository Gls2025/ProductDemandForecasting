# ProductDemandForecasting

# 📦 Product Demand Forecasting with Machine Learning

This project uses machine learning (LightGBM) to forecast **daily product demand** based on historical sales, price, promotional activity, and calendar features. It is designed for retail and supply chain teams to improve inventory planning, reduce stockouts, and optimize operational decisions.

---

## 📈 Project Objective

The goal is to:
- Predict future **daily unit sales** for each product
- Train a separate demand model per product using historical data
- Use lag features, time-based calendar features, and promotion flags
- Apply **LightGBM** models for fast and accurate forecasting
- Produce a forecast horizon of **30 days** (configurable)

---

## 🛠️ Features

- ⚡ Fast training using **LightGBM Regressor**
- 🧠 Intelligent feature engineering:
  - Lag features (1, 2, 3, 7, 14, 28-day lags)
  - Calendar features (weekday, month, year, holidays)
- 🗃️ Model-per-product training with KFold cross-validation
- 📤 Forecast export to CSV
- 📊 Optional forecast visualization using `matplotlib`

---

## 📁 Project Structure


---

## 📊 Sample Input Format (`sales_history.csv`)

| date       | product_id | units | price | promo_flag |
|------------|------------|-------|-------|------------|
| 2023-01-01 | A1001      | 120   | 19.99 | 1          |
| 2023-01-02 | A1001      | 105   | 19.99 | 0          |
| 2023-01-01 | B2011      | 60    | 14.50 | 1          |

- `date`: sales date (YYYY-MM-DD)
- `product_id`: unique identifier for each product
- `units`: units sold on that day (target)
- `price`: unit price for the product
- `promo_flag`: binary indicator (1 if promotional activity was active)

---

## 📦 Installation

1. Clone the repo:
```bash
git clone https://github.com/your-username/ProductDemandForecasting.git
cd ProductDemandForecasting

##Install dependencies:
pip install -r requirements.txt


Contact
Author: Timon Osida
📧 Email: timonochieng88@gmail.com
🌐 LinkedIn: https://www.linkedin.com/in/timon-osida-61171922a/
