import joblib
from textutils import clean_text

vec = joblib.load("models/vectorizer.joblib")
model = joblib.load("models/model.joblib")

THRESHOLD = 0.5

def predict_category(text):
    return model.predict(vec.transform([clean_text(text)]))[0]

def predict_with_confidence(text):
    probs = model.predict_proba(vec.transform([clean_text(text)]))[0]
    best = probs.argmax()
    return model.classes_[best], probs[best]

def predict_or_unsure(text, threshold=THRESHOLD):
    category, conf = predict_with_confidence(text)
    if conf < threshold:
        return "Not sure"
    return category

if __name__ == "__main__":
    tests = ["Swiggy order 450", "Paid to Uber", "UPI-Netflix-1234", "Apollo Pharmacy Rs 300"]
    for t in tests:
        print(t, "->", predict_or_unsure(t))