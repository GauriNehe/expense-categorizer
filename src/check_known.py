from predict import predict_with_confidence

for t in ["Amazon", "Swiggy", "Uber", "Netflix", "Zomato", "Myntra", "Apollo Pharmacy", "Jio"]:
    category, conf = predict_with_confidence(t)
    print(t, "->", category, round(float(conf), 2))
    