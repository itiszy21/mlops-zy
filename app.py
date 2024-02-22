from flask import Flask,request, url_for, redirect, render_template, jsonify
from pycaret.regression import *
import pandas as pd
import pickle
import numpy as np
from joblib import load


app = Flask(__name__)

model = load('resort_regression_zy.pkl')
cols = ['accommodates', 'amenities', 'bedrooms', 'beds', 'bathrooms', 'bed_type', 'cancellation_policy', 'property_type', 'room_type', 'has_availability', 'host_is_superhost', 'instant_bookable']

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [x for x in request.form.values()]
    final = np.array(int_features)
    data_unseen = pd.DataFrame([final], columns = cols)
    prediction = predict_model(model, data=data_unseen, round = 0)
    prediction_value = int(prediction.prediction_label[0])
    return render_template('home.html',pred='Expected Price will be {}'.format(prediction_value))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    data_unseen = pd.DataFrame([data])
    prediction = predict_model(model, data=data_unseen)
    output = prediction.Label[0]
    return jsonify(output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
