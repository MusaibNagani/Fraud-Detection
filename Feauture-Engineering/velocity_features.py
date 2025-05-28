import pyodbc
import pandas as pd
from datetime import timedelta

conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};" 
    "Server=localhost;" 
    "Database=FraudDetection;"
    "Trusted_Connection=yes;" 
)

query = """
SELECT CustomerID, TransactionDate
FROM Transactions;
"""

df = pd.read_sql(query, conn)
print("Columns in df:", df.columns.tolist())

df['TransactionDate'] = pd.to_datetime(df['TransactionDate'])

df = df.sort_values(by=['CustomerID', 'TransactionDate'])

# First Feature
df['TxnFlag'] = 1

txn_count = (
    df.set_index('TransactionDate')
      .groupby('CustomerID')['TxnFlag']
      .rolling('30min')
      .count()
      .reset_index()
      .rename(columns={'TxnFlag': 'TransactionCountUnder30Minutes'})
)

df = pd.merge(df, txn_count, on=['CustomerID', 'TransactionDate'], how='left')

# Second feature 
df['TransactionsEveryHour'] = df['TransactionDate'].dt.floor('h')
TransactionRate = df.groupby(['CustomerID', 'TransactionsEveryHour']).size().reset_index(name='TransactionratePerHour')


# Third Feature 
def countBursts(timeStamps):
    count = 0
    timeStamps = sorted(timeStamps)
    for i in range(len(timeStamps)-4):
        if timeStamps[i + 4] - timeStamps[i] <= timedelta(minutes=10):
            count +=1
    return count

BurstCounts = df.groupby('CustomerID')['TransactionDate'].apply(countBursts).reset_index(name = 'TransactionBurstScore')


features = df[['CustomerID', 'TransactionDate', 'TransactionCountUnder30Minutes', 'TransactionsEveryHour']].drop_duplicates()
features = features.merge(TransactionRate, on=['CustomerID', 'TransactionsEveryHour'], how='left')
features = features.merge(BurstCounts, on='CustomerID', how='left')

features.drop(columns=['TransactionsEveryHour'], inplace=True)

print(features.head(3))

features.to_csv("velocity_features.csv", index=False)

print("Velocity features exported to CSV.")