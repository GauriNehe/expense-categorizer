import pandas as pd
from predict import vec, model
from textutils import clean_text

df = pd.read_csv("data/transactions.csv")
rows = df[df["description"].str.contains("Amazon", case=False)]
print("rows with Amazon:", len(rows))
print(rows["category"].value_counts())
print()

for text in ["Amazon", "Amazon order 450", "AMAZON"]:
    probs = model.predict_proba(vec.transform([clean_text(text)]))[0]
    top = sorted(zip(model.classes_, probs), key=lambda x: -x[1])[:3]
    print(text, "->", [(c, round(float(p), 2)) for c, p in top])