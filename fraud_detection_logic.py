import sqlite3

conn = sqlite3.connect('fraud_detection.db')
cursor = conn.cursor()

cursor.execute('SELECT count(*) FROM transactions WHERE is_fraud = 1')
before_count = cursor.fetchone()[0]
print(f"Before: {before_count}")

print("Flagging logic who's transactions are higher than 3000")
cursor.execute('''
    UPDATE transactions
    SET is_fraud = 1
    WHERE Amount > 3000
''')

high_risk_cities = ['Toronto', 'Mumbai', 'Manchester', 'New York']
print("Flagging logic for high-risk cities")
cursor.execute('''
    UPDATE transactions
    SET is_fraud = 1
    WHERE location IN (?, ?, ?, ?)
''', high_risk_cities)

print("Flagging logic for high-risk devices")
cursor.execute('''
    UPDATE transactions
    SET is_fraud = 1
    WHERE device = 'ATM' AND amount > 1000
''')

conn.commit()
cursor.execute('SELECT count(*) FROM transactions WHERE is_fraud = 1')
after_count = cursor.fetchone()[0]
print(f"After: {after_count} transactions flagged as fraud")

conn.close()
print("Fraud detection logic executed successfully.")