import re

CITIES = ["NEW DELHI", "DELHI", "KOLKATA", "KOLKATTA", "MUMBAI", "NOIDA", "BANGALORE", "PUNE"]

NARRATION_HINTS = r"(?i)(by debit card|to transfer|by transfer|bulk posting|UPI/|\bINB\b|\bATM\b|OTHPOS|OTHPG|SBIPG)"


def is_person_transfer(text):
    if re.search(r"VPA\s+\d{8,}@", text, re.I):
        return True
    if re.search(r"UPI/\d+/\d{8,}@", text, re.I):
        return True
    if re.search(r"(?i)\b(IMPS|NEFT|RTGS)", text):
        return True
    return False


def narration_type(text):
    if re.search(r"(?i)\bby transfer|\bcsh dep|\bcredit interest", text):
        return "credit"
    if re.search(r"(?i)\bto transfer|\bby debit card|\batm wdl", text):
        return "debit"
    return None


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
    transfer = is_person_transfer(text)
    if re.search(r"(?:Rs\.?|INR|₹)\s*\d", text, re.I):
        info = parse_sms(text)
    elif re.search(NARRATION_HINTS, text) or len(text.split()) <= 6:
        info = {"merchant": clean_narration(text), "amount": None, "type": narration_type(text)}
    else:
        info = {"merchant": "", "amount": None, "type": narration_type(text)}
    info["transfer"] = transfer
    return info