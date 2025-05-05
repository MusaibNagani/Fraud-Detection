# 🕵️‍♂️ SQLite Fraud Detection

This project simulates a fraud detection system using Python + SQLite.

## 🚀 Features

- Generates fake transactions using `Faker`
- Flags fraud based on:
    - High amounts (>3000)
    - High-risk cities
    - ATM + high-amount transactions

## 🗂️ Files

| File                  | Description                                    |
|-----------------------|------------------------------------------------|
| `fraud_detection.db`  | SQLite DB with transactions                   |
| `generate_data.py`    | Script to create fake transactions            |
| `fraud_detection.py`  | Script to apply fraud detection rules         |

## ▶️ How to Run

1️⃣ Install requirements:

```bash
pip install faker
