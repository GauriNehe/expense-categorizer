import random
import pandas as pd

random.seed(42)

merchants = {
    "Food": ["Swiggy", "Zomato", "Dominos", "McDonalds", "KFC", "Starbucks",
             "Chai Point", "Haldirams", "Barbeque Nation", "Burger King",
             "Pizza Hut", "Cafe Coffee Day", "Behrouz", "Faasos"],
    "Transport": ["Uber", "Ola", "Rapido", "IRCTC", "RedBus", "Metro Card",
                  "Indian Oil", "HP Petrol Pump", "FASTag", "MakeMyTrip",
                  "Bharat Petroleum", "Shell", "Delhi Metro", "Ixigo"],
    "Bills": ["Jio", "Airtel", "Vi", "Electricity Board", "BSNL Broadband",
              "Tata Power", "Gas Cylinder", "Water Bill", "Mahanagar Gas",
              "ACT Fibernet", "Adani Electricity", "Hathway", "LIC"],
    "Shopping": ["Amazon", "Flipkart", "Myntra", "Ajio", "Meesho", "Nykaa",
                 "Decathlon", "Reliance Trends", "DMart", "Croma",
                 "Zara", "Westside", "Pantaloons", "Bata"],
    "Entertainment": ["Netflix", "Spotify", "BookMyShow", "Hotstar", "PVR",
                      "Inox", "YouTube Premium", "Prime Video", "Steam",
                      "SonyLIV", "Gaana", "JioCinema", "Epic Games"],
    "Health": ["Apollo Pharmacy", "1mg", "PharmEasy", "Practo", "Medplus",
               "Netmeds", "Cult Fit", "Lal PathLabs", "Max Hospital",
               "Dr Morepen", "Fortis Hospital", "Medlife", "Thyrocare"],
}

keywords = {
    "Food": ["restaurant", "cafe", "dinner", "lunch", "pizza", "biryani",
             "sandwich", "bakery", "snacks", "tiffin"],
    "Transport": ["ride", "cab", "taxi", "auto", "fuel", "petrol",
                  "toll", "bus", "train", "parking"],
    "Bills": ["recharge", "electricity", "broadband", "postpaid", "prepaid",
              "gas", "water", "dth", "rent", "bill"],
    "Shopping": ["clothes", "shoes", "shirt", "fashion", "gadgets",
                 "furniture", "jewellery", "watch", "bag", "store"],
    "Entertainment": ["subscription", "movie", "streaming", "music", "gaming",
                      "concert", "show", "ott", "premium", "tickets"],
    "Health": ["pharmacy", "hospital", "clinic", "doctor", "medicine",
               "lab", "diagnostics", "dental", "checkup", "tablets"],
}

templates = [
    "UPI-{m}-{n}", "Paid to {m}", "{m} order {a}", "POS {n} {m}",
    "{m} payment Rs {a}", "Debited Rs {a} at {m}", "{m} {a}",
    "UPI/{n}/{m}", "{m} online payment", "Txn at {m} Rs {a}",
    "{k} {a}", "Paid for {k} Rs {a}", "{k} payment {a}", "UPI-{k}-{n}",
    "Debited Rs {a} {k}", "{m} {k} {a}", "POS {n} {m} {k}", "{m} {k}",
]

rows = []
for category in merchants:
    for i in range(120):
        text = random.choice(templates).format(
            m=random.choice(merchants[category]),
            k=random.choice(keywords[category]),
            n=random.randint(1000, 9999),
            a=random.randint(50, 2500),
        )
        rows.append((text, category))

df = pd.DataFrame(rows, columns=["description", "category"])
df = df.drop_duplicates().sample(frac=1, random_state=42)
df.to_csv("data/transactions.csv", index=False)
print(df.shape)
print(df["category"].value_counts())
print(df.head(10))