# tests/test_views.py

import unittest
from flask import url_for
from app import create_app
from app.models import db, Patient
from config.settings import TestingConfig

class TestViews(unittest.TestCase):

    def setUp(self):
        self.app = create_app(TestingConfig)
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_index_view(self):
        response = self.client.get(url_for('app_views.index'))
        self.assertEqual(response.status_code, 200)

    def test_report_view_without_patient(self):
        response = self.client.get(url_for('app_views.report', patient_id=1))
        self.assertEqual(response.status_code, 302)

    def test_report_view_with_patient(self):
        patient = Patient(first_name='John', last_name='Doe', dob='1980-01-01', gender='Male', symptoms='Cough')
        db.session.add(patient)
        db.session.commit()

        response = self.client.get(url_for('app_views.report', patient_id=patient.id))
        self.assertEqual(response.status_code, 200)

    def test_patient_intake_form_submission(self):
        response = self.client.post(url_for('app_views.index'), data={
            'first_name': 'John',
            'last_name': 'Doe',
            'dob': '1980-01-01',
            'gender': 'Male',
            'symptoms': 'Cough'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
