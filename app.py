from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    try:
        val = [float(x) for x in request.form.values()]
        features = np.array(val).reshape(1,-1)
        prediction = model.predict(features)
        result = prediction[0]

        return render_template('index.html', prediction_text = np.round(result, 2), input_data = np.round(features, 2))

    except Exception as e:
        return render_template('index.html', error_found = f"Error While Predicting, Error is, {e}")

if __name__ == "__main__":
    app.run(debug=True)