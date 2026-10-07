import pandas as pd

rows = [
    ("Swiggy order 450","Food"),
    ("Zomato payment 320","Food"),
    ("Uber ride to college","Transport"),
    ("Ola Cab 180","Transport"),
    ("Metro card recharge","Transport"),
    ("Jio recharge 299","Bills"),
    ("Electricity bill paid","Bills"),
    ("Amazon purchase shoes","Shopping"),
    ("Myntra order 1200","Shopping"),
    ("Netflix subscription","Entertainment"),
    ("BookMyShow movie tickets","Entertainment"),
    ("Apollo Pharmacy","Health"),
]
df=pd.DataFrame(rows, columns=["description","category"])
df.to_csv("data/transactions.csv",index=False)
print(df)