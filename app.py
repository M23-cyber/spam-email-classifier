from flask import Flask, render_template, request, jsonify
import pickle
import re

app = Flask(__name__)

# Load vectorizer and model
with open("spam_classifier.pkl", "rb") as f:
    vectorizer, clf = pickle.load(f)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/classifier")
def classifier():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("email", "").strip()

    if not text:
        return jsonify({"error": "Please enter some text or a URL"}), 400

    # Preprocess: detect links
    if re.match(r'https?://', text):
        email_text = f"This link was submitted: {text}"
    else:
        email_text = text

    try:
        X = vectorizer.transform([email_text])
        prediction = clf.predict(X)[0]
        confidence = clf.predict_proba(X)[0][prediction]

        result = "Spam" if prediction == 1 else "Not Spam"

        return jsonify({
            "prediction": result,
            "confidence": f"{confidence * 100:.2f}%"
        })
    except Exception:
        return jsonify({"error": "Something went wrong during prediction."}), 500

if __name__ == "__main__":
    app.run(debug=True)
