from flask import Flask, render_template, request, jsonify
import pickle
import re
import traceback
import os

app = Flask(__name__)

import joblib

model = joblib.load('spam_classifier.pkl')

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/classifier")
def classifier():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data['email']

    if not text:
        return jsonify({"error": "Please enter some text or a URL"}), 400

    # Preprocess: detect links
    if re.match(r'https?://', text):
        email_text = f"This link was submitted: {text}"
    else:
        email_text = text

    try:
        X = model.named_steps['tfidfvectorizer'].transform([email_text])
        prediction = model.predict([email_text])[0]
        proba = model.predict_proba([email_text])[0].max()


        result = "Spam" if prediction == 1 else "Not Spam"

        return jsonify({
            "prediction": result,
            "confidence": f"{proba * 100:.2f}%"
        })
    except Exception as e:
        print("Exception occurred:")
        traceback.print_exc()
        return jsonify({"error": "Something went wrong during prediction."})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # required for Railway
    app.run(debug=True, host="0.0.0.0", port=port)