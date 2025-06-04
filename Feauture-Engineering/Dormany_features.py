import pandas as pd
import pyodbc

conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=localhost;" 
    "Database=FraudDetection;"
    "Trusted_Connection=yes;"
)

query = "SELECT CustomerID, TransactionDate, Amount FROM Transactions"

df = pd.read_sql(query,conn)

df['TransactionDate'] = pd.to_datetime(df['TransactionDate'])

df = df.sort_values(['CustomerID', 'TransactionDate'])

df['PreviousTransactionDate'] = df.groupby('CustomerID')['TransactionDate'].shift(1)
df['DaysSinceLastTransaction'] = (df['TransactionDate'] - df['PreviousTransactionDate']).dt.days
df['DaysSinceLastTransaction'] = df['DaysSinceLastTransaction'].fillna(0).astype(int)

HighAmountThreshold = 500
DormancyGapThreshold = 59
df['GapBeforeHighTransaction'] = (
    (df['DaysSinceLastTransaction'] > DormancyGapThreshold) &
    (df['Amount'] > HighAmountThreshold)
).astype(int)

DormantDays = 25
df['IsDormantThenUsed'] = (df['DaysSinceLastTransaction'] > DormantDays).astype(int)

DormancyMaxDays = df.groupby('CustomerID')['DaysSinceLastTransaction'].max().reset_index(name='DormancyPeriodLength')
df = df.merge(DormancyMaxDays,on='CustomerID', how='left')

dormancy_features = df[['CustomerID', 'TransactionDate', 'Amount','DaysSinceLastTransaction', 'GapBeforeHighTransaction','IsDormantThenUsed', 'DormancyPeriodLength']]

dormancy_features.to_csv("dormancy_features.csv", index=False)
print("Dormancy features exported to dormancy_features.csv")
