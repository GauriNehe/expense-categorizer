import csv
import os
from flask import Flask, render_template, request, redirect, url_for
from predict import predict_with_confidence, THRESHOLD
from parser import parse

app = Flask(__name__, template_folder="../templates", static_folder="../static")

CATEGORIES = ["Food", "Transport", "Bills", "Shopping", "Entertainment", "Health"]
CORRECTIONS_FILE = "data/corrections.csv"


def save_correction(text, category):
    new_file = not os.path.exists(CORRECTIONS_FILE)
    with open(CORRECTIONS_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if new_file:
            writer.writerow(["description", "category"])
        writer.writerow([text, category])


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        raw = request.form["text"].strip()
        info = parse(raw)
        merchant = info["merchant"]
        if merchant:
            category, conf = predict_with_confidence(merchant)
            if conf < THRESHOLD:
                category = "Not sure"
            conf = round(float(conf), 2)
        else:
            category, conf = "No merchant found", None
        result = {
            "merchant": merchant,
            "amount": info["amount"],
            "type": info["type"],
            "category": category,
            "confidence": conf,
        }
    saved = request.args.get("saved")
    if saved not in CATEGORIES:
        saved = None
    return render_template("index.html", result=result, categories=CATEGORIES, saved=saved)


@app.route("/correct", methods=["POST"])
def correct():
    text = request.form["text"].strip()
    category = request.form["category"]
    if text and len(text) <= 60 and category in CATEGORIES:
        save_correction(text, category)
        return redirect(url_for("home", saved=category))
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)