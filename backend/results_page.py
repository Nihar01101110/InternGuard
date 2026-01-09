import random
from text_signals_detection import detect_scam_signals
from text_signals import (
    URGENT_KEYWORDS,
    PAYMENT_KEYWORDS,
    GUARANTEE_KEYWORDS,
    BENEFIT_KEYWORDS,
    AUTHORITY_KEYWORDS,
    CONTACT_KEYWORDS,
    LANGUAGE_PATTERNS
)

RISK_MEANS = {
    "URGENT_KEYWORDS": 5,
    "PAYMENT_KEYWORDS": 8,
    "GUARANTEE_KEYWORDS": 7,
    "BENEFIT_KEYWORDS": 4,
    "AUTHORITY_KEYWORDS": 3,
    "CONTACT_KEYWORDS": 6,
    "LANGUAGE_PATTERNS": 2
}

RISK_STD = {
    "URGENT_KEYWORDS": 1.0,
    "PAYMENT_KEYWORDS": 1.5,
    "GUARANTEE_KEYWORDS": 1.0,
    "BENEFIT_KEYWORDS": 0.8,
    "AUTHORITY_KEYWORDS": 0.8,
    "CONTACT_KEYWORDS": 1.0,
    "LANGUAGE_PATTERNS": 0.5
}

def sample_risk_score(category):
    score = random.gauss(RISK_MEANS[category], RISK_STD[category])
    return max(0, min(score, 10))

def normalize_score(score):
    return round(score / 10, 3)

def interpret_risk(score):
    if score <= 0.25:
        return "Low Risk"
    elif score <= 0.50:
        return "Medium Risk"
    elif score <= 0.75:
        return "High Risk"
    else:
        return "Scam Likely"

def evaluate_message_risk(categories):
    if not categories:
        return 0.0, "Low Risk"

    scores = [sample_risk_score(cat) for cat in categories]
    raw = sum(scores) / len(scores)
    normalized = normalize_score(raw)

    return normalized, interpret_risk(normalized)