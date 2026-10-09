import re

def clean_text(s):
    return re.sub(r"\d+", " ", s)