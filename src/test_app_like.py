from parser import parse
from predict import predict_with_confidence, THRESHOLD


def app_like(text):
    info = parse(text)
    if info["type"] == "credit":
        return "Money Received", 1.0
    if info["transfer"]:
        return "Money Transfer", 1.0
    merchant = info["merchant"] or text
    return predict_with_confidence(merchant)


tests = [
    ("Rasoi Dhaba Kolkata", "Food"),
    ("Chaiwala Corner 40", "Food"),
    ("Sagar Ratna 560", "Food"),
    ("by debit card-OTHPOS803014290736SAGAR RATNA KOLKATTA--", "Food"),
    ("Yulu bike rental 30", "Transport"),
    ("Local train pass Mumbai 450", "Transport"),
    ("BULK POSTING- 00000014528 IRCTC TICKETING INR--", "Transport"),
    ("Indraprastha Gas IGL 450", "Bills"),
    ("Excitel broadband 799", "Bills"),
    ("Municipal property tax 3200", "Bills"),
    ("Lifestyle stores 1999", "Shopping"),
    ("Shoppers Stop 3400", "Shopping"),
    ("boAt earphones order 1299", "Shopping"),
    ("Audible membership 199", "Entertainment"),
    ("Smaaash arcade 600", "Entertainment"),
    ("Wonderla tickets 1200", "Entertainment"),
    ("Dr Batra clinic 900", "Health"),
    ("Pathkind labs 1100", "Health"),
    ("TO TRANSFER-INB Wellness Forever Medicare--", "Health"),
    ("Sankara Nethralaya eye test 500", "Health"),
]

raw_correct = 0
answered = 0
answered_right = 0
for text, expected in tests:
    got, conf = app_like(text)
    ok = got == expected
    raw_correct += ok
    if conf >= THRESHOLD:
        answered += 1
        answered_right += ok
    print("OK " if ok else "XX ", round(float(conf), 2), text, "->", got)

print()
print("raw correct (no cutoff):", raw_correct, "out of", len(tests))
print("answered with cutoff:", answered, "| right of answered:", answered_right)