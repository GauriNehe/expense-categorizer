import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

df=pd.read_csv("data/transactions.csv")

vec=TfidfVectorizer()
X=vec.fit_transform(df["description"])

model=LogisticRegression(max_iter=1000)
model.fit(X,df["category"])

tests=["Swiggy dinner 500","Uber ride 250","Netflix payment","Myntra shirt"]
print(model.predict(vec.transform(tests)))