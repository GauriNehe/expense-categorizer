from parser import parse

samples = [
    "Rs 450.00 debited from A/c XX1234 on 07-10-26 to VPA swiggy@icici (UPI Ref 123456789).",
    "Rs.250 spent on your card XX1234 at ZOMATO on 07-10-26.",
    "Paid Rs 180 to Rapido",
    "INR 1,299.00 credited to your A/c XX1234 on 07-10-26",
    "Rs 500 debited from A/c XX1234 on 07-10-26 to VPA 9999999999@ybl",
    "by debit card-OTHPOS803014290736SAGAR RATNA KOLKATTA--",
    "TO TRANSFER-INB Zomato Media Private Limi--",
    "by debit card-OTHPG 806417410043FREECHARGE MUMBAI--",
    "TO TRANSFER-UPI/802512286191/MYNTRA@ybl--",
    "TO TRANSFER-UPI/802834824589/9999999999@ybl--",
]

for s in samples:
    print(s)
    print("   ->", parse(s))