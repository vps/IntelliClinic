# app/utils/db_helpers.py

from flask import current_app
from .models import db, Patient
from sqlalchemy.exc import SQLAlchemyError

def init_db():
    with current_app.app_context():
        db.create_all()

def add_patient(first_name, last_name, dob, gender, symptoms):
    new_patient = Patient(first_name=first_name, last_name=last_name, dob=dob, gender=gender, symptoms=symptoms)
    try:
        db.session.add(new_patient)
        db.session.commit()
        return True
    except SQLAlchemyError as e:
        db.session.rollback()
        print(str(e))
        return False

def get_all_patients():
    try:
        patients = Patient.query.all()
        return patients
    except SQLAlchemyError as e:
        print(str(e))
        return None

def get_patient_by_id(patient_id):
    try:
        patient = Patient.query.get(patient_id)
        return patient
    except SQLAlchemyError as e:
        print(str(e))
        return None
