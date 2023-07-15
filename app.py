import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)#name of directory
model = pickle.load(open('model.pkl','rb'))

#route
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # for rendering results on html gui

    int_features = [int(x) for x in request.form.values()]


    return render_template('index.html', prediction_text="Employee Salary should be ${}".format())
    
if __name__ == "__main__":
    app.run(debug=True)