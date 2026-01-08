import re
from preProcessing import withoutURL_text
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\s+',' ',text)
    text = re.sub(r'[^\w\s₹]', '', text)
    text.strip()
    return text
text=clean_text(withoutURL_text)
print(text)
# aa file ru clean text paibu and tu athire array operation and compairison karibu