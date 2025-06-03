import pandas as pd
import pyodbc

conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=localhost;" 
    "Database=FraudDetection;"
    "Trusted_Connection=yes;"
    )


query = "SELECT LoginID, CustomerID, LoginTime, IPAddress, DeviceID FROM Login"

df = pd.read_sql(query,conn)

df['LoginTime'] = pd.to_datetime(df['LoginTime'])

df=df.sort_values(['CustomerID','LoginTime'])

df['PreviousIP'] = df.groupby('CustomerID')['IPAddress'].shift(1)
df['PreviousDevice'] = df.groupby('CustomerID')['DeviceID'].shift(1)

df['RecentIPChange'] = (df['IPAddress'] != df['PreviousIP']).astype(int)
df['RecentDeviceChange'] = (df['DeviceID'] != df['PreviousDevice']).astype(int)

df[['RecentIPChange', 'RecentDeviceChange']] = df[['RecentIPChange', 'RecentDeviceChange']].fillna(0).astype(int)

behavioral_features = df[['LoginID', 'CustomerID', 'LoginTime', 'RecentIPChange', 'RecentDeviceChange']]

behavioral_features.to_csv("behavioral_features.csv", index=False)
print("Behavioral features exported to behavioral_features.csv")