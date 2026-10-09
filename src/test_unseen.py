from predict import predict_category

tests = [
    ("Subway sandwich 220", "Food"),
    ("Namma Yatri ride 90", "Transport"),
    ("Tata Play recharge 450", "Bills"),
    ("Lenskart order 2100", "Shopping"),
    ("Zee5 subscription 199", "Entertainment"),
    ("Manipal Hospital 1500", "Health"),
    ("BluSmart cab 350", "Transport"),
    ("Pepperfry furniture 8000", "Shopping"),
    ("Burger Singh meal 250", "Food"),
    ("Dish TV recharge 300", "Bills"),
    ("Aster Clinic 700", "Health"),
    ("Eros Now premium 149", "Entertainment"),
    ("Wow Momo 180", "Food"),
]

correct = 0
for text, expected in tests:
    got = predict_category(text)
    mark = "OK " if got == expected else "XX "
    if got == expected:
        correct += 1
    print(mark, text, "->", got, "(expected", expected + ")")
print(correct, "out of", len(tests))