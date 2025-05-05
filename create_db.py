import sqlite3

conn = sqlite3.connect("fraud_detection.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        Sender_id TEXT,
        Receiver_id TEXT,
        Amount REAL,
        transaction_type TEXT,
        loaction TEXT,
        is_fraud INTEGER DEFAULT 0
    )
''')

conn.commit()
conn.close()

print("Database and table created successfully.")