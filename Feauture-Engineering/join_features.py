import pandas as pd
import os

os.makedirs("outputs", exist_ok=True)

velocity_df = pd.read_csv("outputs/velocity_features.csv")
dormancy_df = pd.read_csv("outputs/dormancy_features.csv")
behavioral_df = pd.read_csv("outputs/behavioral_features.csv")

merged_df = pd.merge(velocity_df, dormancy_df, on=["CustomerID", "TransactionDate"], how="left")

merged_df['TransactionDate'] = pd.to_datetime(merged_df['TransactionDate'])
behavioral_df['LoginTime'] = pd.to_datetime(behavioral_df['LoginTime'])

merged_df = merged_df.sort_values("TransactionDate")
behavioral_df = behavioral_df.sort_values("LoginTime")

final_df = pd.merge_asof(merged_df, behavioral_df, left_on="TransactionDate", right_on="LoginTime", by="CustomerID", direction="backward")

final_df.drop(columns=["LoginID", "LoginTime"], inplace=True)

final_df.to_csv("outputs/final_features.csv", index=False)
print("All features successfully joined into outputs/final_features.csv")
