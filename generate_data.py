import sqlite3
from faker import Faker 
import random

fake = Faker()
conn = sqlite3.connect('fraud_detection.db')
cursor = conn.cursor()

high_risk_cities = ['Toronto', 'Mumbai', 'Manchester', 'New York']

def insert_fake_transactions():
    timestamp = fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S")
    sender_id = fake.uuid4()
    receiver_id = fake.uuid4()

    if random.random() < 0.8:
        amount = round(random.uniform(10,3000), 2)
    else:
        amount = round(random.uniform(3001, 10000), 2)

    transaction_type = random.choice(['payment', 'transfer', 'withdrawal', 'deposit'])
    device = random.choice(['mobile', 'desktop','ATM'])

    if random.random() < 0.9:
        location = fake.city()
    else:
        location = random.choice(high_risk_cities)

    cursor.execute('''
        INSERT INTO transactions (timestamp, sender_id, receiver_id, amount, transaction_type, device, location)
        VALUES (?, ?, ?, ?, ?, ?,?)
    ''', (timestamp, sender_id, receiver_id, amount, transaction_type, device, location))


for _ in range(1000):
    insert_fake_transactions()

conn.commit()
conn.close()

print("Fake transactions generated and inserted successfully.")