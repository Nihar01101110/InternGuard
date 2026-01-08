from URL_signals import risk
url_risk=risk




from signal_labels import HUMAN_READABLE_SIGNALS
from text_signals_detection import detect_scam_signals
from results_page import evaluate_message_risk
message="Hello i am the main risk give me money do the payments and internships scam fast limited offers"

categories = detect_scam_signals(message)
risk_score, risk_level = evaluate_message_risk(categories)

readable_signals = [
        HUMAN_READABLE_SIGNALS[cat] for cat in categories
    ]

a={
        "risk_score": round(risk_score, 2),
        "risk_level": risk_level,
        "signals_detected": readable_signals
    }
print(a)