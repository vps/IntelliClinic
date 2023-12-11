# ai/note_generation_model.py

import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

class NoteGenerationModel:
    def __init__(self):
        # Load the trained model
        self.model = load_model('path_to_your_model.h5')
        # Initialize the TfidfVectorizer
        self.vectorizer = TfidfVectorizer(stop_words=stopwords.words('english'))

    def preprocess(self, patient_data):
        # Convert patient data to pandas DataFrame
        df = pd.DataFrame([patient_data])

        # Tokenize and vectorize the symptoms
        df['symptoms'] = df['symptoms'].apply(word_tokenize)
        df['symptoms'] = df['symptoms'].apply(self.vectorizer.fit_transform)

        # Convert DataFrame to numpy array
        return df.to_numpy()

    def generate(self, patient_data):
        # Preprocess the patient data
        data = self.preprocess(patient_data)

        # Generate a note
        note = self.model.predict(data)

        # Return the note
        return note
