import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

covid19app = Flask(__name__)
model = pickle.load(open('covid19model.pkl', 'rb'))

@covid19app.route('/')
def home():
    return render_template('covid19index.html')

@covid19app.route('/predict',methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    if prediction==0:
        data="Not Affected By Covid-19"
    elif prediction==1:
        data="Affected By Covid-19"
    return render_template('covid19index.html', prediction_text='Health Status: {}'.format(data))

if __name__ == "__main__":
    covid19app.run(debug=True)