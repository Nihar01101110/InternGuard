# Checking message and detecting them from predefined lists

from preProcessing import clean_text
from text_signals import (
    URGENT_KEYWORDS,
    PAYMENT_KEYWORDS,
    GUARANTEE_KEYWORDS,
    BENEFIT_KEYWORDS,
    AUTHORITY_KEYWORDS,
    CONTACT_KEYWORDS,
    LANGUAGE_PATTERNS
)
def keyword_match(text,keywords):
    return any(word in text for word in keywords) # Checking text by using keywords
def detect_scam_signals(text):
    text = clean_text(text) # cleaning the text
    signals = [] #  empty list that will store scam warnings

    if keyword_match(text, URGENT_KEYWORDS):
          signals.append("URGENT_KEYWORDS")

    if keyword_match(text, PAYMENT_KEYWORDS):
        signals.append("PAYMENT_KEYWORDS")

    if keyword_match(text, GUARANTEE_KEYWORDS):
        signals.append("GUARANTEE_KEYWORDS")

    if keyword_match(text, BENEFIT_KEYWORDS):
        signals.append("BENEFIT_KEYWORDS")

    if keyword_match(text, AUTHORITY_KEYWORDS):
        signals.append("AUTHORITY_KEYWORDS")

    if keyword_match(text, CONTACT_KEYWORDS):
         signals.append("CONTACT_KEYWORDS")

    if keyword_match(text, BENEFIT_KEYWORDS):
            signals.append("BENEFIT_KEYWORDS")

    return signals
