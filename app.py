import joblib
import numpy as np

from flask import Flask, request, jsonify
model=joblib.load('iris_model.pkl')
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Iris Prediction API!"

@app.route('/compute', methods=['POST'])
def compute():
    data = request.get_json(force=True)
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)[0]
    class_names = ['setosa', 'versicolor', 'virginica']
    result = {"prediction": class_names[prediction]}
    return jsonify(result)

if __name__=='__main__':
    app.run(debug=True  , host='0.0.0.0'   ,port=5000)