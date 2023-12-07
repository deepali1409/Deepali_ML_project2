from flask import Flask, request, Response, render_template, jsonify
from joblib import load
import requests
import numpy as np

# # Loading my model
my_dt_model = load('my_decision_tree_model.joblib')

# Initialising
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/predict", methods = ["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = my_dt_model.predict(features)
    return render_template("index.html", prediction_text = "The Species is {}".format(prediction))


if __name__ == '__main__':
    app.run(debug=True)


