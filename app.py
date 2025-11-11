from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import joblib

app = Flask(__name__)

# Load the trained model and pipeline
MODEL_FILE = "model.pkl"
PIPELINE_FILE = "pipeline.pkl"
model = joblib.load(MODEL_FILE)
pipeline = joblib.load(PIPELINE_FILE)

# Home route — show HTML form
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = {
            'longitude': float(request.form['longitude']),
            'latitude': float(request.form['latitude']),
            'housing_median_age': float(request.form['housing_median_age']),
            'total_rooms': float(request.form['total_rooms']),
            'total_bedrooms': float(request.form['total_bedrooms']),
            'population': float(request.form['population']),
            'households': float(request.form['households']),
            'median_income': float(request.form['median_income']),
            'ocean_proximity': request.form['ocean_proximity']
        }

        # Convert input to DataFrame
        input_df = pd.DataFrame([input_data])

        # Apply preprocessing
        transformed_input = pipeline.transform(input_df)

        # Make prediction
        prediction = model.predict(transformed_input)[0]

        return render_template('index.html', 
                               prediction_text=f"Predicted Median House Value: ${prediction:,.2f}")

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
