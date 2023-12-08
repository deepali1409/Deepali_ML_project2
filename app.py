from flask import Flask, request, Response, render_template, jsonify
from joblib import load
import requests
import numpy as np

# # Loading my model
my_rf_model = load('model.joblib')

# Initialising
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Predicting the species using values entered by user
@app.route("/predict", methods = ["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = my_rf_model.predict(features)
    return render_template("index.html", prediction_text = "The Species is {}".format(prediction))


if __name__ == '__main__':
    app.run(debug=True)


