# tests/test_models.py

import unittest
from datetime import datetime
from app.models import db, Patient
from app import create_app

class TestModels(unittest.TestCase):

    def setUp(self):
        self.app = create_app('config.settings')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_patient_model(self):
        # Create a new patient
        new_patient = Patient(first_name='John', last_name='Doe', dob=datetime(1990, 5, 17), gender='Male', symptoms='Fever, cough')
        db.session.add(new_patient)
        db.session.commit()

        # Check if the patient is added
        patient = Patient.query.filter_by(first_name='John').first()
        self.assertIsNotNone(patient)

        # Check if the patient data is correct
        self.assertEqual(patient.first_name, 'John')
        self.assertEqual(patient.last_name, 'Doe')
        self.assertEqual(patient.dob, datetime(1990, 5, 17))
        self.assertEqual(patient.gender, 'Male')
        self.assertEqual(patient.symptoms, 'Fever, cough')

if __name__ == "__main__":
    unittest.main()
