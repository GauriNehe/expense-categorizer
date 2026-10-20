import pandas as pd

CATEGORIES = ["Food", "Transport", "Bills", "Shopping", "Entertainment",
              "Health", "Education", "Money Transfer", "Money Received"]

df = pd.read_csv("data/corrections.csv")
print("total rows:", len(df))
print(df["category"].value_counts())
print("duplicate rows:", df.duplicated().sum())
print("distinct merchants:", df["description"].nunique())
print("too long (over 60 chars):", (df["description"].str.len() > 60).sum())
print("unknown categories:", (~df["category"].isin(CATEGORIES)).sum())
print("rows with 6+ digit numbers:", df["description"].str.contains(r"\d{6,}").sum())