import pandas as pd
from predict import predict_category

df = pd.read_csv("data/real_test.csv")
df["predicted"] = df["description"].apply(predict_category)

correct = (df["category"] == df["predicted"]).sum()
print("Accuracy on real data:", correct, "out of", len(df))

wrong = df[df["category"] != df["predicted"]]
print(wrong.to_string())