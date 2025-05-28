
# 🕵️‍♂️ Fraud Detection Platform 

A full-scale fraud detection simulation project using Python, synthetic transaction generation, SQL Server database architecture, and modular feature engineering pipelines. Built to mimic real-world financial fraud analysis with a clear progression from basic rules to advanced behavioral and velocity-based analytics.

---

## 🚧 Project Summary

This project simulates fraud detection in a transactional banking environment by building a local database, generating realistic synthetic transaction data, and applying rule-based and advanced analytics to extract high-risk signals. The entire process is fully automated in Python and modularly organized for reuse in ML pipelines or BI dashboards.

---

## 🧱 Architecture Overview

| Component               | Technology           | Purpose                                                  |
|------------------------|----------------------|-----------------------------------------------------------|
| Database               | Microsoft SQL Server | Hosts structured schema (Customers, Transactions, Logins) |
| Data Generation        | Python + Faker       | Simulates realistic synthetic transaction data            |
| Feature Engineering    | Python + Pandas      | Extracts rule-based, velocity, and behavioral indicators  |
| Storage                | CSV / Excel Export   | Saves enriched features for downstream usage              |
| Visualization (optional)| Power BI            | Dashboarding for fraud analysts                           |

---

## 📁 Project Structure

```
fraud-detection/
│
├── Feature-Engineering/
│   ├── generate_fraud_data.py        # Generates Customers, Transactions, Logins
│   ├── velocity_features.py          # Computes rolling/temporal features
│   └── behavioral_features.py        # (Coming Soon) IP/device/dormancy/geo signals
│
├── Rule-Based-Method/
│   ├── generate_data.py                  # Faker data generator for SQLite (Phase 1)
|   ├── fraud_detection.py                # Simple rule-based fraud flagging (SQLite)
|   └── fraud_detection.db                # SQLite DB for Phase 1 (legacy)
|
├── velocity_features.csv             # Output from velocity pipeline
├── .venv/                            # Python virtual environment
└── README.md                         # Full project documentation
```

---

## 🔄 Phased Development

### 📌 Phase 1 — Rule-Based Fraud (SQLite)

A lightweight version using SQLite as a backend to test fundamental fraud rules.

**Rules Applied:**
- Transactions above $3,000
- Known high-risk cities
- ATM + high-amount combinations

**How to Run:**
```bash
pip install faker
python generate_data.py
python fraud_detection.py
```

---

### 📌 Phase 2 — MSSQL + Feature Engineering

Phase 2 simulates a production environment with:

- A full relational schema
- Hosted locally on MSSQL Server Developer Edition
- Multiple tables: Customers, Transactions, Login

**Schema includes:**
- `Customers`: metadata like region, account type, open date
- `Transactions`: timestamped, geo-tagged financial activity
- `Login`: IPs, devices, and login history per customer

---

## ⚙️ Features Engineered

### 📈 Velocity Features

| Feature                        | Description                                  |
|-------------------------------|----------------------------------------------|
| TransactionCountUnder30Minutes| Rolling 30-min transaction window count      |
| TransactionratePerHour        | Hourly grouped transaction volume            |
| TransactionBurstScore         | # of 5+ txns within a 10-min burst           |

### 🧠 Behavioral Features (Planned)

| Feature               | Description                                 |
|------------------------|---------------------------------------------|
| RecentIPChange         | Login from unseen IP in last 5 logins       |
| RecentDeviceChange     | Login from new device                       |
| DormancyPeriodLength   | # of days since last active use             |
| GeoDriftScore          | Distance-based geo anomaly detection        |

---

## 🧪 How to Use Phase 2 (MSSQL Version)

### 🔧 Step 1: Set up MSSQL Server
- Install SQL Server Developer Edition
- Create a database named `FraudDetection`
- Use the provided schema in `generate_fraud_data.py` to create tables

### 🏗 Step 2: Generate Data
```bash
python Feature-Engineering/generate_fraud_data.py
```
Generates:
- 100s of customers
- 1000s of transactions
- login patterns with IPs and devices

### 🧮 Step 3: Extract Velocity Features
```bash
python Feature-Engineering/velocity_features.py
```
- Reads from SQL Server using `pyodbc`
- Computes rolling metrics, burst scores, hourly rates
- Exports enriched features to `velocity_features.csv`

### 📊 Step 4 (Optional): Load to Power BI
- Connect to `velocity_features.csv`
- Build dashboards by customer, risk score, date, etc.

---

## 📊 Use Cases

- 🛡 Fraud analytics simulation
- 🧠 Feature engineering for ML
- 🔍 Pattern mining for internal audit teams
- 📉 Data exploration using time-based metrics

---

## 💡 Sample Output

| CustomerID | TransactionDate     | TransactionCountUnder30Minutes | TransactionratePerHour | TransactionBurstScore |
|------------|---------------------|--------------------------------|-------------------------|------------------------|
| 1001       | 2025-05-10 14:12:00 | 4                              | 6                       | 2                      |

---

## 🧠 Learning Highlights

- Simulated real-world data pipelines
- Local database hosting and connectivity via `pyodbc`
- Rolling windows and burst detection using pandas
- Data engineering best practices in modular file structure

---

## 📌 Future Roadmap

- ✅ Add behavioral feature script (IP, device, dormancy)
- ✅ Create merged master feature table
- 🔄 Build Power BI dashboard for visual detection
- 🔍 Add unsupervised anomaly detection (Isolation Forest)
- 🧠 Enable model training using engineered features

---

## 📦 Tech Stack

- Python 3.10+
- pandas, Faker
- pyodbc, sqlite3
- MSSQL Server Developer Edition
- Power BI (optional for visuals)

---

## 👨‍💻 Author

**Musaib Nagani**  
Computer Science | AI & Data Analytics | Fraud Detection Systems  
Built with a focus on real-world applications and data engineering workflow simulation.

---

## 📜 License

MIT License – open source and reusable for learning and experimentation.
