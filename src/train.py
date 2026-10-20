import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from textutils import clean_text
from parser import parse

MODEL_CATEGORIES = ["Food", "Transport", "Bills", "Shopping",
                    "Entertainment", "Health", "Education"]
REPEAT = 5

df = pd.read_csv("data/transactions.csv")

X_train, X_test, y_train, y_test = train_test_split(
    df["description"], df["category"],
    test_size=0.2, random_state=42, stratify=df["category"]
)

# realistic raw rows -> parser -> merchant text (jaisa app mein hota hai)
real = pd.read_csv("data/realistic_train.csv")
keep_text = []
keep_label = []
dropped = []
for text, label in zip(real["description"], real["category"]):
    info = parse(text)
    merchant = info["merchant"]
    if (not merchant) or info["type"] == "credit" or info["transfer"] or label not in MODEL_CATEGORIES:
        dropped.append(text)
        continue
    keep_text.append(merchant)
    keep_label.append(label)

print("realistic rows kept:", len(keep_text), "| dropped:", len(dropped))
print("parser ne yeh merchants nikaale (pehle 8):", keep_text[:8])
for d in dropped:
    print("  dropped:", d)

real_text = pd.Series(keep_text)
real_label = pd.Series(keep_label)
X_train = pd.concat([X_train] + [real_text] * REPEAT, ignore_index=True)
y_train = pd.concat([y_train] + [real_label] * REPEAT, ignore_index=True)

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