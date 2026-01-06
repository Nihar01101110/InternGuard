from flask import Flask
from flask import request,jsonify
from flask_cors import CORS

app =Flask(__name__)
CORS(app)

@app.route('/',methods =["GET"])
def index():
    return {"message":"Hello World"}

@app.route("/analyze",methods=["GET","POST"])
def analyze():
    data =request.get_json()
    return jsonify({
        "risk_score":70,
        "risk_level":"SUSPICIOUS",
        "signals_detected":["Dummy Signals"],
        "explanation" : "This is placeholder response",
        "advice": ["Do not pay money upfront"]
    })
if __name__ == '__main__':
    app.run(debug=True)