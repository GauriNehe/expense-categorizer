import re

CITIES = ["NEW DELHI", "DELHI", "KOLKATA", "KOLKATTA", "MUMBAI", "NOIDA", "BANGALORE", "PUNE"]

NARRATION_HINTS = r"(?i)(by debit card|to transfer|by transfer|bulk posting|UPI/|\bINB\b|\bATM\b|OTHPOS|OTHPG|SBIPG)"


def clean_narration(text):
    t = text.strip()

    # UPI/<ref>/<name>@bank  -> take the name; digits-only name means a person
    m = re.search(r"UPI/\d+/([^@\s]+)@", t, re.I)
    if m:
        name = m.group(1)
        return "" if name.isdigit() else name

    t = re.sub(r"(?i)(by debit card|to transfer|by transfer|bulk posting)\s*-?", " ", t)
    t = re.sub(r"(?i)\bINB\b", " ", t)
    t = re.sub(r"\b(?:OTHPOS|OTHPG|SBIPG)\s*(?:LU)?\d+", " ", t)
    t = re.sub(r"-{2,}\s*$", "", t)
    t = re.sub(r"\d{4,}", " ", t)
    for c in CITIES:
        t = re.sub(r"(?i)\b" + c + r"\b", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def parse_sms(text):
    amt = re.search(r"(?:Rs\.?|INR|₹)\s*([\d,]+(?:\.\d+)?)", text, re.I)
    amount = float(amt.group(1).replace(",", "")) if amt else None

    low = text.lower()
    if re.search(r"debited|spent|paid|withdrawn", low):
        kind = "debit"
    elif re.search(r"credited|received|deposited", low):
        kind = "credit"
    else:
        kind = None

    merchant = ""
    m = re.search(r"VPA\s+([\w.\-]+)@", text, re.I)
    if m:
        merchant = m.group(1)
    else:
        stop = r"(?:\s+on\b|\s+Ref\b|\(|\.\s|\.$|$)"
        m = re.search(r"\bat\s+([A-Za-z][A-Za-z0-9 &.\-]*?)" + stop, text)
        if not m:
            m = re.search(r"\bto\s+([A-Za-z][A-Za-z0-9 &.\-]*?)" + stop, text)
        if m:
            merchant = m.group(1).strip()
    if merchant.isdigit():
        merchant = ""

    return {"merchant": merchant, "amount": amount, "type": kind}


def parse(text):
    if re.search(r"(?:Rs\.?|INR|₹)\s*\d", text, re.I):
        return parse_sms(text)
    if re.search(NARRATION_HINTS, text) or len(text.split()) <= 6:
        return {"merchant": clean_narration(text), "amount": None, "type": None}
    return {"merchant": "", "amount": None, "type": None}