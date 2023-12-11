# ai/intake_model.py

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import load_model

class IntakeModel:
    def __init__(self):
        # Load the trained model
        self.model = load_model('path_to_your_model.h5')
        # Initialize the label encoder
        self.encoder = LabelEncoder()

    def preprocess(self, form_data):
        # Convert form data to pandas DataFrame
        df = pd.DataFrame([form_data])

        # Encode categorical data
        for column in df.columns[df.dtypes == 'object']:
            df[column] = self.encoder.fit_transform(df[column])

        # Convert DataFrame to numpy array
        return df.to_numpy()

    def predict(self, form_data):
        # Preprocess the form data
        data = self.preprocess(form_data)

        # Make a prediction
        prediction = self.model.predict(data)

        # Return the prediction
        return prediction
