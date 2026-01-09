from flask import Flask, request, jsonify
from flask_cors import CORS

from signal_labels import HUMAN_READABLE_SIGNALS
from text_signals_detection import detect_scam_signals
from results_page import evaluate_message_risk


from extract_URL import extract_url_and_text
from URL_signals import analyze_url
from cleanText import clean_text




app = Flask(__name__)
CORS(app)
@app.route("/", methods=["GET"])
def index():
    return {"message": "Backend is running"}

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json(force=True)  # force avoids 415 errors
    message = data.get("message", "")
    #doing coding again
    url , text_without_url=extract_url_and_text(message)# extract url from the text 
    user_url=url
    user_url=user_url.strip()
    risk = analyze_url(user_url)#complete of the URL part

    # text_without_url also store the value of the files that does not changes


    #these are the logics of calculations
    url_risk = risk   # assume this is already a number between 0–100

    message = text_without_url
    message = clean_text(message)
    categories = detect_scam_signals(message)
    text_risk_score, text_risk_level = evaluate_message_risk(categories)


    readable_signals = [HUMAN_READABLE_SIGNALS[cat] for cat in categories]

    TEXT_WEIGHT = 0.60
    URL_WEIGHT = 0.40

    final_risk_score = (
        text_risk_score * TEXT_WEIGHT +
        url_risk * URL_WEIGHT
    )

    if final_risk_score >= 75:  
        final_risk_level = "High"
    elif final_risk_score >= 40:    
        final_risk_level = "Medium"
    else:
        final_risk_level = "Low"

    result = {
        "final_risk_score": round(final_risk_score, 2),
        "final_risk_level": final_risk_level,
        "text_risk_score": round(text_risk_score, 2),
        "url_risk_score": round(url_risk, 2),
        "signals_detected": readable_signals
}

    print("Final Risk Evaluation:")
    print(result)


    return jsonify(result)


# @app.route("/check")
# def fun():
#     message = "https://www.youtube.com/watch?v=KDHpOUpPwvQ&list=RDd9WOgugZQm4&index=5" \
#     ""
#     #doing coding again
#     url , text_without_url=extract_url_and_text(message)# extract url from the text 
#     user_url=url
#     user_url=user_url.strip()
#     risk = analyze_url(user_url)#complete of the URL part

#     # text_without_url also store the value of the files that does not changes


#     #these are the logics of calculations
#     url_risk = risk   # assume this is already a number between 0–100

#     message = text_without_url
#     message = clean_text(message)
#     categories = detect_scam_signals(message)
#     text_risk_score, text_risk_level = evaluate_message_risk(categories)


#     readable_signals = [HUMAN_READABLE_SIGNALS[cat] for cat in categories]

#     TEXT_WEIGHT = 0.60
#     URL_WEIGHT = 0.40

#     final_risk_score = (
#         text_risk_score * TEXT_WEIGHT +
#         url_risk * URL_WEIGHT
#     )

#     if final_risk_score >= 75:  
#         final_risk_level = "High"
#     elif final_risk_score >= 40:    
#         final_risk_level = "Medium"
#     else:
#         final_risk_level = "Low"

#     result = {
#         "final_risk_score": round(final_risk_score, 2),
#         "final_risk_level": final_risk_level,
#         "text_risk_score": round(text_risk_score, 2),
#         "url_risk_score": round(url_risk, 2),
#         "signals_detected": readable_signals
# }

#     print("Final Risk Evaluation:")
#     print(result)


#     return jsonify(result)

    

if __name__ == "__main__":
    app.run(debug=True)
