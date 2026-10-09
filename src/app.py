from flask import Flask, render_template, request
from predict import predict_with_confidence, THRESHOLD

app = Flask(__name__, template_folder="../templates")

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        text = request.form["text"]
        category, conf = predict_with_confidence(text)
        if conf < THRESHOLD:
            category = "Not sure"
        result = {"text": text, "category": category, "confidence": round(float(conf), 2)}
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)