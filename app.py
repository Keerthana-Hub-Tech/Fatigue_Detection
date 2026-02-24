from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load the trained model
with open("fatigue_model.pkl", "rb") as f:
    model = pickle.load(f)

labels = ["Fresh", "Mild", "Fatigue"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    # Make sure all keys are present
    try:
        typing_speed = float(data["typing_speed"])
        avg_key_interval = float(data["avg_key_interval"])
        backspace_rate = float(data["backspace_rate"])
        avg_mouse_speed = float(data["avg_mouse_speed"])
    except (KeyError, ValueError, TypeError):
        return jsonify({"status": "Error: invalid input"})

    df = pd.DataFrame([[avg_key_interval, typing_speed, backspace_rate, avg_mouse_speed]],
                      columns=["avg_key_interval", "typing_speed", "backspace_rate", "avg_mouse_speed"])

    prediction = model.predict(df)
    status = labels[prediction[0]]

    return jsonify({"status": status})

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
