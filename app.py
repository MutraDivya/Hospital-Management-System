from flask import Flask, render_template, request, redirect
from services.patient_service import PatientService
from services.doctor_service import DoctorService
from services.appointment_service import AppointmentService

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/patients", methods=["GET", "POST"])
def patients():
    service = PatientService()
    error = None

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        age_text = request.form.get("age", "").strip()
        gender = request.form.get("gender", "").strip()
        contact = request.form.get("contact", "").strip()
        address = request.form.get("address", "").strip()
        disease = request.form.get("disease", "").strip()
        symptoms = request.form.get("symptoms", "").strip()
        medical_history = request.form.get("medical_history", "").strip()

        try:
            age = int(age_text)
            if age <= 0:
                raise ValueError
        except ValueError:
            error = "Enter a valid age."
        else:
            if not name or not gender or not contact:
                error = "Name, gender, and contact are required."
            else:
                service.create_patient(
                    name, age, gender, contact, address,
                    disease, symptoms, medical_history
                )
                return redirect("/patients")

    patients = service.get_all_patients()
    return render_template("patients.html", patients=patients, error=error)

@app.route("/patients/<int:patient_id>/update", methods=["POST"])
def update_patient_record(patient_id):
    service = PatientService()
    form = request.form

    try:
        age = int(form.get("age", ""))
        if age <= 0:
            raise ValueError
    except ValueError:
        return render_template(
            "patients.html",
            patients=service.get_all_patients(),
            error="Enter a valid age."
        )

    service.update_patient_record(
        patient_id,
        form.get("name", "").strip(),
        age,
        form.get("gender", "").strip(),
        form.get("contact", "").strip(),
        form.get("address", "").strip(),
        form.get("disease", "").strip(),
        form.get("symptoms", "").strip(),
        form.get("medical_history", "").strip()
    )
    return redirect("/patients")


@app.route("/patients/<int:patient_id>/delete", methods=["POST"])
def delete_patient_record(patient_id):
    service = PatientService()

    if not service.delete_patient_by_id(patient_id):
        return render_template(
            "patients.html",
            patients=service.get_all_patients(),
            error="This patient has appointments and cannot be deleted."
        )

    return redirect("/patients")

@app.route("/patients/search")
def search_patient_web():
    service = PatientService()
    patient_id = request.args.get("patient_id", "").strip()

    if not patient_id.isdigit():
        return render_template(
            "patients.html",
            patients=[],
            error="Enter a valid patient ID."
        )

    patient = service.get_patient_by_id(int(patient_id))
    results = [patient] if patient else []

    return render_template(
        "patients.html",
        patients=results,
        error=None
    )


@app.route("/doctors", methods=["GET", "POST"])
def doctors():
    service = DoctorService()
    error = None

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        specialization = request.form.get("specialization", "").strip()
        contact = request.form.get("contact", "").strip()

        if not name or not specialization or not contact:
            error = "Fill in all fields."
        else:
            service.create_doctor(name, specialization, contact)
            return redirect("/doctors")

    doctors = service.get_all_doctors()
    return render_template("doctors.html", doctors=doctors, error=error)

@app.route("/doctors/<int:doctor_id>/update", methods=["POST"])
def update_doctor(doctor_id):
    service = DoctorService()
    service.update_doctor_record(
        doctor_id,
        request.form.get("name", "").strip(),
        request.form.get("specialization", "").strip(),
        request.form.get("contact", "").strip()
    )
    return redirect("/doctors")


@app.route("/doctors/<int:doctor_id>/delete", methods=["POST"])
def delete_doctor(doctor_id):
    service = DoctorService()
    service.delete_doctor_by_id(doctor_id)
    return redirect("/doctors")


@app.route("/appointments", methods=["GET", "POST"])
def appointments():
    service = AppointmentService()
    error = None

    if request.method == "POST":
        patient_id = request.form.get("patient_id", "").strip()
        doctor_name = request.form.get("doctor_name", "").strip()
        appointment_date = request.form.get("appointment_date", "").strip()
        appointment_time = request.form.get("appointment_time", "").strip()

        if not patient_id.isdigit():
            error = "Choose a valid patient."
        elif not doctor_name or not appointment_date or not appointment_time:
            error = "Fill in every field."
        else:
            success, error = service.create_appointment(
                int(patient_id), doctor_name, appointment_date, appointment_time
            )
            if success:
                return redirect("/appointments")

    patients = PatientService().get_all_patients()
    doctors = DoctorService().get_all_doctors()
    appointments = service.get_all_appointments()

    return render_template(
        "appointments.html",
        appointments=appointments,
        patients=patients,
        doctors=doctors,
        error=error
    )


@app.route("/appointments/cancel/<int:appointment_id>", methods=["POST"])
def cancel_appointment(appointment_id):
    service = AppointmentService()
    service.cancel_appointment_by_id(appointment_id)
    return redirect("/appointments")


if __name__ == "__main__":
    app.run(debug=True,port=5001)