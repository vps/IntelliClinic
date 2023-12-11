# app/views.py

from flask import Blueprint, render_template, request, redirect, url_for
from .models import Patient, db
from .utils.ai_helpers import process_intake, generate_note
from .forms import PatientIntakeForm

app_views = Blueprint('app_views', __name__)

@app_views.route('/', methods=['GET', 'POST'])
def index():
    form = PatientIntakeForm()
    if form.validate_on_submit():
        # Process patient intake form
        patient_data = form.data
        patient = Patient(**patient_data)
        db.session.add(patient)
        db.session.commit()

        # Generate patient note using AI
        note = generate_note(patient)

        # Redirect to report page
        return redirect(url_for('app_views.report', patient_id=patient.id, note=note))

    return render_template('index.html', form=form)

@app_views.route('/report/<int:patient_id>', methods=['GET'])
def report(patient_id):
    # Retrieve patient data from database
    patient = Patient.query.get(patient_id)
    if not patient:
        return redirect(url_for('app_views.index'))

    # Retrieve note from request args
    note = request.args.get('note', '')

    return render_template('report.html', patient=patient, note=note)
