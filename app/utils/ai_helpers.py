# app/utils/ai_helpers.py

from ai.intake_model import IntakeModel
from ai.note_generation_model import NoteGenerationModel

# Initialize AI models
def init_ai():
    global intake_model
    global note_generation_model
    intake_model = IntakeModel()
    note_generation_model = NoteGenerationModel()

# Process patient intake form using AI
def process_intake(form_data):
    return intake_model.predict(form_data)

# Generate patient note using AI
def generate_note(patient):
    patient_data = {
        'first_name': patient.first_name,
        'last_name': patient.last_name,
        'dob': patient.dob,
        'gender': patient.gender,
        'symptoms': patient.symptoms
    }
    return note_generation_model.generate(patient_data)
