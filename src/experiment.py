import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

train = pd.read_csv("data/transactions.csv")
test = pd.read_csv("data/real_test.csv")

def clean(s):
    return s.str.replace(r"\d+", " ", regex=True)

train_text = clean(train["description"])
test_text = clean(test["description"])

configs = {
    "words": TfidfVectorizer(token_pattern=r"[A-Za-z]{2,}"),
    "char 2-4": TfidfVectorizer(analyzer="char_wb", ngram_range=(2, 4)),
    "char 3-5": TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 5)),
}

for name, vec in configs.items():
    X_tr = vec.fit_transform(train_text)
    X_te = vec.transform(test_text)
    model = LogisticRegression(C=10, max_iter=1000)
    model.fit(X_tr, train["category"])
    pred = model.predict(X_te)
    correct = (pred == test["category"]).sum()
    print(name, "->", correct, "out of", len(test))