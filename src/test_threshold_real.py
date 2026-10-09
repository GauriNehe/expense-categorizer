import pandas as pd
from predict import predict_with_confidence

df = pd.read_csv("data/real_test.csv")
rows = []
for text, expected in zip(df["description"], df["category"]):
    got, conf = predict_with_confidence(text)
    rows.append((got == expected, conf))
    print("OK " if got == expected else "XX ", round(conf, 2), text, "->", got)

print()
print("cutoff | answered | right of answered | not sure")
for th in [0.3, 0.4, 0.5, 0.6]:
    answered = [ok for ok, conf in rows if conf >= th]
    print(th, "|", len(answered), "|", sum(answered), "|", len(rows) - len(answered))