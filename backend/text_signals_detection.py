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
          signals.append("Urgent language used")

    if keyword_match(text, PAYMENT_KEYWORDS):
        signals.append("Upfront payment requested")

    if keyword_match(text, GUARANTEE_KEYWORDS):
        signals.append("Unrealistic guarantees")

    if keyword_match(text, BENEFIT_KEYWORDS):
        signals.append("Unrealistic benefits promised")

    if keyword_match(text, AUTHORITY_KEYWORDS):
        signals.append("Unrealistic benefits promised")

    if keyword_match(text, CONTACT_KEYWORDS):
         signals.append("Unprofessional contact method")

    if keyword_match(text, BENEFIT_KEYWORDS):
            signals.append("Unrealistic benefits promised")

    return signals