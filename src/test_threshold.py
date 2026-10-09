from predict import predict_with_confidence

clear = [
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

unclear = [
    "Rahul Sharma UPI",
    "Mummy Bday and Anni",
    "ATM CASH WITHDRAWAL",
    "CREDIT INTEREST",
    "BigBasket groceries 850",
    "xyzqwerty",
]

clear_preds = []
for text, expected in clear:
    got, conf = predict_with_confidence(text)
    clear_preds.append((got == expected, conf))
    mark = "OK " if got == expected else "XX "
    print(mark, round(conf, 2), text, "->", got)

unclear_conf = []
print()
for text in unclear:
    got, conf = predict_with_confidence(text)
    unclear_conf.append(conf)
    print(round(conf, 2), text, "->", got)

print()
print("cutoff | answered | right of answered | not sure (of 20) | unclear flagged (of 6)")
for th in [0.3, 0.4, 0.5, 0.6, 0.7]:
    answered = [ok for ok, conf in clear_preds if conf >= th]
    right = sum(answered)
    not_sure = len(clear_preds) - len(answered)
    flagged = sum(1 for c in unclear_conf if c < th)
    print(th, "|", len(answered), "|", right, "|", not_sure, "|", flagged)