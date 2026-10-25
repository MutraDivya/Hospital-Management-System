from services.patient_service import PatientService
from services.appointment_service import AppointmentService
from services.doctor_service import DoctorService

patient_service = PatientService()
appointment_service = AppointmentService()
doctor_service = DoctorService()

while True:
    print("\n" + "=" * 55)
    print("\nHospital Management System\n")
    print("=" * 55)
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Update Patient")
    print("4. Delete Patient")
    print("5. Search Patient")
    print("-" * 55)
    print("6. Book Appointment")
    print("7. View Appointments")
    print("8. Cancel Appointment")
    print("-" * 55)
    print("9. Add Doctor")
    print("10. View Doctors")
    print("11. Update Doctor")
    print("12. Delete Doctor")
    print("-" * 55)
    print("13. Exit")
    print("=" * 55)

    choice = input("\n---Enter your choice: ")

    if choice == "1":
        patient_service.add_patient()

    elif choice == "2":
        patient_service.view_patients()

    elif choice == "3":
        patient_service.update_patient()
    
    elif choice == "4":
        patient_service.delete_patient()

    elif choice == "5":
        patient_service.search_patient()

    elif choice == "6":
        appointment_service.book_appointment()

    elif choice == "7":
        appointment_service.view_appointments()

    elif choice == "8":
        appointment_service.cancel_appointment()

    elif choice == "9":
        doctor_service.add_doctor()

    elif choice == "10":
        doctor_service.view_doctors()

    elif choice == "11":
        doctor_service.update_doctor()

    elif choice == "12":
        doctor_service.delete_doctor()

    elif choice == "13":
        print("\nThank you!")
        break

    else:
        print("\nInvalid choice! Please enter a number between 1 & 13.")











