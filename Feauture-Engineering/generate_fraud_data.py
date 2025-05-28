import pyodbc
from faker import Faker
import random
from datetime import datetime, timedelta

conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=localhost;"
    "Database=FraudDetection;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()
fake = Faker()

Num_Customers = 1000
Num_Logins_Per_Customer = 10
Num_Transactions_Per_Customer = 20

for customer_id in range(1, Num_Customers +1):
    name = fake.name()
    region = fake.state()
    account_date = fake.date_between(start_date = '-3y', end_date = '-1y')
    account_type = random.choice(['savings', 'checking', 'student'])

    cursor.execute('''
        INSERT INTO Customers (CustomerID, CustomerName, Region, AccountOpenDate, AccountType)
        VALUES (?, ?, ?, ?, ?)
    ''', (customer_id, name, region, account_date, account_type))


for customer_id in range(1, Num_Customers + 1):
    for _ in range(Num_Logins_Per_Customer):
        login_time = fake.date_time_between(start_date='-30d', end_date='now')
        ip = fake.ipv4()
        device_id = fake.uuid4()
        location = fake.city()

        cursor.execute('''
            INSERT INTO Login(CustomerID, LoginTime, IPAddress, DeviceID, Loaction)
            VALUES (?, ?, ?, ?, ?)
        ''', (customer_id, login_time, ip, device_id, location))

for customer_id in range(1, Num_Customers + 1):
    for _ in range(Num_Transactions_Per_Customer):
        amount = round(random.uniform(10.0, 1000.0), 2)
        transaction_time = fake.date_time_between(start_date='-30d', end_date='now')
        Channel = random.choice(['online', 'mobile', 'ATM', 'branch'])
        merchant = fake.company()
        location = fake.city()

        cursor.execute('''
            INSERT INTO Transactions (CustomerID, Amount, TransactionDate, Channel, Merchant, Location)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (customer_id, amount, transaction_time, Channel, merchant, location))


conn.commit()
cursor.close()
print("Fake data generated and inserted successfully.")
conn.close()







