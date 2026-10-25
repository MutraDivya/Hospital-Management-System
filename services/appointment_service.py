from models.appointment import Appointment
from services.database import Database
from utils.validation import get_int, get_non_empty

class AppointmentService:

    def __init__(self):
        self.db = Database()
        self.db.create_appointment_table()

    
    def book_appointment(self):
    
        patient_id = get_int("\nEnter Patient ID: ")
        if patient_id is None:
            return
        if patient_id <= 0:
            print("Invalid Patient ID")
            return
        
        doctor_name = get_non_empty("\nEnter Doctor Name: ")
        if doctor_name is None:
            return
        appointment_date = get_non_empty("Enter Appointment Date (YYYY-MM-DD): ")
        if appointment_date is None:
            return
        appointment_time = get_non_empty("Enter Appointment Time (HH:MM): ")
        if appointment_time is None:
            return
        
        patient = self.db.fetch_one("SELECT * FROM patients WHERE patient_id = ?",(patient_id,))
        if not patient:
            print("Patient does not exist!")
            return
        
        appointment = Appointment(
            patient_id,
            doctor_name,
            appointment_date,
            appointment_time
        )
        self.db.insert(
            "appointments",
            ["patient_id", "doctor_name", "appointment_date", "appointment_time"],
            (
                appointment.patient_id,
                appointment.doctor_name,
                appointment.appointment_date,
                appointment.appointment_time
            )
        )
        print("\nAppointment booked successfully!")


    def view_appointments(self):
    
        appointments = self.db.fetch_all("SELECT * FROM appointments")
        if not appointments:
            print("\nNo appointments found.")
            return

        for appointment in appointments:
            print("-" * 50)
            print(f"Appointment ID : {appointment[0]}")
            print(f"Patient ID     : {appointment[1]}")
            print(f"Doctor Name    : {appointment[2]}")
            print(f"Date           : {appointment[3]}")
            print(f"Time           : {appointment[4]}")
            print("=" * 50)

        
    def cancel_appointment(self):
    
        appointment_id = get_int("\nEnter Appointment ID to cancel: ")
        if appointment_id is None:
            return

        appointment = self.db.fetch_one("SELECT * FROM appointments WHERE appointment_id = ?",(appointment_id,))
        if not appointment:
            print("Appointment not found.")
            return
        
        self.db.delete(
            "appointments",
            "appointment_id = ?",
            (appointment_id,)
        )
        print("\nAppointment cancelled successfully!")


    def get_all_appointments(self):
        return self.db.fetch_all("SELECT * FROM appointments")

    def create_appointment(self, patient_id, doctor_name, appointment_date, appointment_time):
        patient = self.db.fetch_one(
            "SELECT * FROM patients WHERE patient_id = ?",
            (patient_id,)
        )

        if not patient:
            return False, "Patient ID not found."

        self.db.insert(
            "appointments",
            ["patient_id", "doctor_name", "appointment_date", "appointment_time"],
            (patient_id, doctor_name, appointment_date, appointment_time)
        )
        return True, None

    def cancel_appointment_by_id(self, appointment_id):
        appointment = self.db.fetch_one(
            "SELECT * FROM appointments WHERE appointment_id = ?",
            (appointment_id,)
        )

        if not appointment:
            return False

        self.db.delete(
            "appointments",
            "appointment_id = ?",
            (appointment_id,)
        )
        return True