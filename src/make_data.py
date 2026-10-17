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
    "Education": ["Byjus", "Unacademy", "Coursera", "Udemy", "Vedantu", "upGrad",
                  "Physics Wallah", "Chegg", "Simplilearn", "Great Learning",
                  "Coding Ninjas", "Testbook", "Toppr", "Scaler", "NPTEL", "Skillshare",
                  "Symbiosis Institute", "Allen Career Institute", "St Xavier College",
                  "FIITJEE", "Amity University", "Manipal University",
                  "Christ University", "VIT University"],
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
    "Education": ["tuition", "course", "exam fee", "college fee", "school fees",
                  "admission", "semester fee", "stationery", "textbook",
                  "coaching", "certification", "workshop",
                  "college", "university", "institute"],
}

templates = [
    "UPI-{m}-{n}", "Paid to {m}", "{m} order {a}", "POS {n} {m}",
    "{m} payment Rs {a}", "Debited Rs {a} at {m}", "{m} {a}",
    "UPI/{n}/{m}", "{m} online payment", "Txn at {m} Rs {a}",
    "{k} {a}", "Paid for {k} Rs {a}", "{k} payment {a}", "UPI-{k}-{n}",
    "Debited Rs {a} {k}", "{m} {k} {a}", "POS {n} {m} {k}", "{m} {k}",
]

first_names = ["Rahul", "Priya", "Amit", "Neha", "Rohan", "Sneha", "Vikram",
               "Anjali", "Karan", "Pooja", "Arjun", "Meera", "Sanjay", "Kavita",
               "Deepak", "Ritu", "Manish", "Divya", "Suresh", "Nisha"]
last_names = ["Sharma", "Verma", "Gupta", "Singh", "Patel", "Reddy", "Das",
              "Mehta", "Nair", "Joshi"]


def random_name():
    return random.choice(first_names) + " " + random.choice(last_names)


transfer_keywords = ["IMPS", "NEFT", "RTGS", "transfer", "fund transfer",
                     "sent", "pocket money", "family", "friend", "split"]

transfer_templates = [
    "UPI-{p}-{n}", "Paid to {p}", "{p} UPI", "Sent to {p} Rs {a}", "{p} {a}",
    "IMPS {n} {p}", "NEFT {n} {p}", "TO TRANSFER-INB {p}",
    "Fund transfer {p} Rs {a}", "UPI/{n}/{p}", "RTGS {p} {a}",
    "Transfer to {p}", "{k} {p}", "{k} {a}", "Paid to {p} {k}",
]

received_keywords = ["salary", "stipend", "refund", "cashback", "interest",
                     "received", "credited", "deposit", "scholarship",
                     "reward", "reimbursement", "payout"]

received_templates = [
    "Received Rs {a} from {p}", "Credited Rs {a} {k}", "{k} credited {a}",
    "{k} {a}", "UPI-{p}-{n} credited", "Received from {p}",
    "{p} sent you Rs {a}", "BY TRANSFER-INB {p}", "{k} received",
    "Refund from {m} Rs {a}", "{m} refund {a}", "{m} cashback {a}",
    "Cr Rs {a} {k}", "{k} from {p}",
]

all_merchants = [m for names in merchants.values() for m in names]

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

for i in range(120):
    text = random.choice(transfer_templates).format(
        p=random_name(),
        k=random.choice(transfer_keywords),
        n=random.randint(1000, 9999),
        a=random.randint(50, 5000),
    )
    rows.append((text, "Money Transfer"))

for i in range(120):
    text = random.choice(received_templates).format(
        p=random_name(),
        m=random.choice(all_merchants),
        k=random.choice(received_keywords),
        n=random.randint(1000, 9999),
        a=random.randint(50, 20000),
    )
    rows.append((text, "Money Received"))

df = pd.DataFrame(rows, columns=["description", "category"])
df = df.drop_duplicates().sample(frac=1, random_state=42)
df.to_csv("data/transactions.csv", index=False)
print(df.shape)
print(df["category"].value_counts())
print(df.head(10))