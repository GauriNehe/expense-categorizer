import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from textutils import clean_text

df = pd.read_csv("data/transactions.csv")

X_train, X_test, y_train, y_test = train_test_split(
    df["description"], df["category"],
    test_size=0.2, random_state=42, stratify=df["category"]
)

vec = TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 5))
X_train_vec = vec.fit_transform(X_train.apply(clean_text))
X_test_vec = vec.transform(X_test.apply(clean_text))

model = LogisticRegression(C=10, max_iter=1000)
model.fit(X_train_vec, y_train)
pred = model.predict(X_test_vec)
print("Accuracy:", accuracy_score(y_test, pred))

for text, true, p in zip(X_test, y_test, pred):
    if true != p:
        print(text, "| true:", true, "| predicted:", p)

joblib.dump(vec, "models/vectorizer.joblib")
joblib.dump(model, "models/model.joblib")
print("Saved model and vectorizer")