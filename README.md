# 🕵️‍♂️ Fraud Detection Platform – Transaction Intelligence Engine

A full-scale fraud detection simulation project using Python, synthetic transaction generation, SQL Server database architecture, and modular feature engineering pipelines. Built to mimic real-world financial fraud analysis with a clear progression from basic rules to advanced behavioral, dormancy, and velocity-based analytics.

---

## 🚧 Project Summary

This project simulates fraud detection in a transactional banking environment by building a local database, generating realistic synthetic transaction data, and applying rule-based and advanced analytics to extract high-risk signals. The entire process is fully automated in Python and modularly organized for reuse in ML pipelines or BI dashboards.

---

## 🧱 Architecture Overview

| Component               | Technology           | Purpose                                                  |
|------------------------|----------------------|-----------------------------------------------------------|
| Database               | Microsoft SQL Server | Hosts structured schema (Customers, Transactions, Logins) |
| Data Generation        | Python + Faker       | Simulates realistic synthetic transaction data            |
| Feature Engineering    | Python + Pandas      | Extracts rule-based, velocity, behavioral, dormancy       |
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
│   ├── behavioral_features.py        # IP and device anomaly indicators
│   └── dormancy_features.py          # Dormancy-based inactivity and gap features
│
├── Rule-Based-Method/
│   ├── generate_data.py              # Faker data generator for SQLite (Phase 1)
│   ├── fraud_detection.py            # Simple rule-based fraud flagging (SQLite)
│   └── fraud_detection.db            # SQLite DB for Phase 1 (legacy)
│
├── velocity_features.csv             # Output from velocity pipeline
├── behavioral_features.csv           # Output from behavioral pipeline
├── dormancy_features.csv             # Output from dormancy pipeline
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

Simulates a production-grade data architecture with:

- Local Microsoft SQL Server
- A normalized schema (Customers, Transactions, Login)
- External Python feature pipelines

---

## ⚙️ Features Engineered

### 📈 Velocity Features

| Feature                        | Description                                  |
|-------------------------------|----------------------------------------------|
| TransactionCountUnder30Minutes| Rolling 30-min transaction window count      |
| TransactionratePerHour        | Hourly grouped transaction volume            |
| TransactionBurstScore         | # of 5+ txns within a 10-min burst           |

### 🧠 Behavioral Features

| Feature               | Description                                 |
|------------------------|---------------------------------------------|
| RecentIPChange         | Login from unseen IP address                |
| RecentDeviceChange     | Login from new device                       |

### 💤 Dormancy Features

| Feature                 | Description                                                    |
|-------------------------|----------------------------------------------------------------|
| DaysSinceLastTransaction| Days between current and previous transaction                  |
| GapBeforeHighTransaction| Long inactivity followed by a high-value transaction           |
| IsDormantThenUsed       | Any transaction after a long period of inactivity              |
| DormancyPeriodLength    | Longest inactivity gap recorded for the customer               |

---

## 🧪 How to Use Phase 2 (MSSQL Version)

### 🔧 Step 1: Set up SQL Server
- Install MSSQL Server (Developer Edition)
- Run `generate_fraud_data.py` to populate the schema

### 🏗 Step 2: Generate Data
```bash
python Feature-Engineering/generate_fraud_data.py
```

### 🧮 Step 3: Extract Features
```bash
python Feature-Engineering/velocity_features.py
python Feature-Engineering/behavioral_features.py
python Feature-Engineering/dormancy_features.py
```

Each script:
- Reads data from SQL Server
- Computes its respective features
- Outputs `.csv` for inspection or downstream processing

---

## 📊 Use Cases

- 🛡 Fraud analytics simulation
- 🧠 Feature engineering for ML
- 🔍 Pattern mining for internal audit teams
- 📉 Data exploration using time-based metrics

---

## 📌 Future Roadmap

- ✅ Implement behavioral and dormancy features
- 🔄 Join all features into a master transaction dataset
- 📊 Build Power BI dashboard for fraud visualization
- 🤖 Add machine learning for fraud scoring (Random Forest / Isolation Forest)
- 📥 Optionally load enriched features back into SQL Server

---

## 💡 Sample Output (Dormancy)

| CustomerID | TransactionDate | DaysSinceLastTransaction | GapBeforeHighTransaction | IsDormantThenUsed | DormancyPeriodLength |
|------------|------------------|--------------------------|---------------------------|--------------------|-----------------------|
| 1001       | 2025-05-01       | 0                        | 0                         | 0                  | 26                    |
| 1001       | 2025-05-27       | 26                       | 1                         | 1                  | 26                    |

---

## 📦 Tech Stack

- Python 3.10+
- Pandas, Faker
- pyodbc, sqlite3
- Microsoft SQL Server
- Power BI (optional)

---

## 👨‍💻 Author

**Musaib Nagani**  
Computer Science | AI & Data Analytics | Fraud Detection Systems  
Built to simulate end-to-end real-world fraud detection systems for enterprise-style pipelines.

---

## 📜 License

MIT License – open source and reusable for learning and experimentation.