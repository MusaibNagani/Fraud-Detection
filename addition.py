import sqlite3

conn = sqlite3.connect('fraud_detection.db')
cursor = conn.cursor()


try:
    cursor.execute('ALTER TABLE transactions ADD COLUMN location TEXT;')
    print("✅ 'location' column added successfully!")
except sqlite3.OperationalError as e:
    print(f"⚠️ Skipped: {e}")

conn.commit()
conn.close()
