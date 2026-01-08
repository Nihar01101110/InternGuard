from flask import Flask, request, jsonify
from flask_cors import CORS

from signal_labels import HUMAN_READABLE_SIGNALS
from text_signals_detection import detect_scam_signals
from results_page import evaluate_message_risk


app = Flask(__name__)
CORS(app)
@app.route("/", methods=["GET"])
def index():
    return {"message": "Backend is running"}

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json(force=True)  # force avoids 415 errors
    message = data.get("message", "")

    categories = detect_scam_signals(message)
    risk_score, risk_level = evaluate_message_risk(categories)

    readable_signals = [
        HUMAN_READABLE_SIGNALS[cat] for cat in categories
    ]

    return jsonify({
        "risk_score": round(risk_score, 2),
        "risk_level": risk_level,
        "signals_detected": readable_signals
    })

if __name__ == "__main__":
    app.run(debug=True)
