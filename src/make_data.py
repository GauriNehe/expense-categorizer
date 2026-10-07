import random
import pandas as pd
random.seed(42)

merchants={
    "Food":["Swiggy","Zomato","Dominos","McDonalds","KFC","Starbucks","Chai point","Haldirams","Brbeque nation","Burger King"],
    "Transport":["Uber","Ola","Rapido","IRCTC","Redbus","Metro Card","indian oil","HP Petrol Pump","FASTag","MakeMyTrip"],
    "Bills":["Jio","Airtel","Vi","Electricity Board","BSNL Broadband","Tata Power","Gas Cylinder","Water Bill","Mahanagar Gas","ACT Fibernet"],
    "Shopping":["Amazon","Flipcart","Myntra","Ajio","Nykaa","Big Bazaar","Meesho","Decathlon","Reliance","Trends","DMart","Croma"],
    "Entertainment":["Netflix","Hotstar","Prime Video","Sony Liv","Zee5","Disney+","BookMyShow","PVR Cinemas","Inox Cinemas","IMAX"],
    "Health":["Apollo Pharmacy","Medlife","1mg","Netmeds","PharmEasy","Practo","Fortis Hospital","Max Hospital","AIIMS","Manipal Hospital","Medplus","Cult Fit"],
}
templates=[
    "UPI-{m}-{n}","Paid to {m}","{m}order {a}","POS {n}{m}","{m}payment Rs {a}","Debited Rs {a}at {m}","{m}{a}","UPI/{n}/{m}","{m}online payment","Txn at {m} Rs {a}",
]

rows=[]
for category, names in merchants.items():
    for i in range(40):
        m=random.choice(names)
        t=random.choice(templates)
        text=t.format(m=m,n=random.randint(1000,9999),a=random.randint(50,2500))
        rows.append((text,category))

df=pd.DataFrame(rows,columns=["description","category"])
df=df.drop_duplicates().sample(frac=1,random_state=42)
df.to_csv("data/transactions.csv",index=False)
print(df.shape)
print(df["category"].value_counts())
print(df.head(10))