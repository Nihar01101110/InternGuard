import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\s+',' ',text)
    text = re.sub(r'[^\w\s₹]', '', text) # square and negation means anything not in this list
    text.strip()
    return text