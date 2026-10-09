import joblib
from textutils import clean_text

vec = joblib.load("models/vectorizer.joblib")
model = joblib.load("models/model.joblib")

def predict_category(text):
    return model.predict(vec.transform([clean_text(text)]))[0]

if __name__ == "__main__":
    tests = ["Swiggy order 450", "Paid to Uber", "UPI-Netflix-1234", "Apollo Pharmacy Rs 300"]
    for t in tests:
        print(t, "->", predict_category(t))