import pandas as pd
from parser import parse
from predict import predict_with_confidence, THRESHOLD


def app_logic(text):
    info = parse(text)
    if info["type"] == "credit":
        return "Money Received", 1.0
    if info["transfer"]:
        return "Money Transfer", 1.0
    merchant = info["merchant"]
    if not merchant:
        return "No merchant found", 0.0
    category, conf = predict_with_confidence(merchant)
    return category, float(conf)


df = pd.read_csv("data/realistic_test.csv")
raw = 0
answered = 0
answered_right = 0
for text, expected in zip(df["description"], df["category"]):
    got, conf = app_logic(text)
    ok = got == expected
    raw += ok
    if conf >= THRESHOLD:
        answered += 1
        answered_right += ok
    print("OK " if ok else "XX ", round(conf, 2), got, "| expected:", expected, "|", text[:45])

print()
print("raw correct:", raw, "out of", len(df))
print("answered with cutoff:", answered, "| right of answered:", answered_right)