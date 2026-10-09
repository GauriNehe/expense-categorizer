from predict import predict_category

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

correct = 0
for text, expected in clear:
    got = predict_category(text)
    mark = "OK " if got == expected else "XX "
    if got == expected:
        correct += 1
    print(mark, text, "->", got, "(expected", expected + ")")
print(correct, "out of", len(clear))

print()
print("No correct answer exists for these, see what the model says:")
for text in unclear:
    print(text, "->", predict_category(text))