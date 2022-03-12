import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

heartdiseaseapp = Flask(__name__)
model = pickle.load(open('heartdiseasemodel.pkl', 'rb'))

@heartdiseaseapp.route('/')
def home():
    return render_template('heartdiseaseindex.html')

@heartdiseaseapp.route('/predict',methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    if prediction=="Absence":
        data="Not Affected By Heart Disease"
    elif prediction=="Presence":
        data="Affected By Heart Disease"
    return render_template('heartdiseaseindex.html', prediction_text='Health Status: {}'.format(data))

if __name__ == "__main__":
    heartdiseaseapp.run(debug=True)