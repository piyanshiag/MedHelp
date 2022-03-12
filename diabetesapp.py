
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

diabetesapp = Flask(__name__)
model = pickle.load(open('diabetesmodel.pkl', 'rb'))

@diabetesapp.route('/')
def home():
    return render_template('diabetesindex.html')

@diabetesapp.route('/predict',methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    if prediction=='No':
        data="Not Affected By Diabetes"
    elif prediction=="Yes":
        data="Affected By Diabetes"
    return render_template('diabetesindex.html', prediction_text='Health Status: {}'.format(data))


if __name__ == "__main__":
    diabetesapp.run(debug=True)