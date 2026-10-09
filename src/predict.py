import joblib

vec = joblib.load("models/vectorizer.joblib")
model = joblib.load("models/model.joblib")

def predict_category(text):
    return model.predict(vec.transform([text]))[0]

if __name__ == "__main__":
    tests = [
        "Swiggy order 450",
        "Paid to Uber",
        "UPI-Netflix-1234",
        "Apollo Pharmacy Rs 300",
        "Subway sandwich 220",
        "Namma Yatri ride 90",
        "Tata Play recharge 450",
        "Lenskart order 2100",
        "Zee5 subscription 199",
        "Manipal Hospital 1500",
    ]
    for t in tests:
        print(t, "->", predict_category(t))