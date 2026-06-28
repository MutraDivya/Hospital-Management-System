from models.patient import Patient
from services.database import Database
from utils.validation import get_int, get_non_empty, get_contact

class PatientService:
    def __init__(self):
        self.db = Database()
        self.db.create_patient_table()
        self.db.create_appointment_table()
    
    def add_patient(self):
        name = get_non_empty("\nEnter Patient Name: ")
        if name is None:
            return
        age = get_int("Enter Patient Age: ")
        if age is None:
            return True
        gender = input("Enter Patient Gender: ")
        contact = get_contact("Enter Patient Contact: ")
        if contact is None:
            return
        address = input("Enter Address: ")
        disease = input("Enter Disease: ")
        symptoms = input("Enter Symptoms: ")
        medical_history = input("Enter Medical History: ")

        patient = Patient(name,age,gender,contact,address,disease,symptoms,medical_history)

        self.db.insert(
            "patients",
            ["name", "age", "gender", "contact", "address", "disease", "symptoms", "medical_history"],
            (patient.name,patient.age,patient.gender,patient.contact,patient.address,patient.disease,patient.symptoms,patient.medical_history)
        )
        print("\nPatient added successfully")
        print('=' * 40)
    

    def view_patients(self):
        patients = self.db.fetch_all("SELECT * FROM patients")
        if not patients:
            print("\nNo patients found.")
            return 
        for patient in patients:
            print("-" * 40)
            print(f"Patient ID      : {patient[0]}")
            print(f"Name            : {patient[1]}")
            print(f"Age             : {patient[2]}")
            print(f"Gender          : {patient[3]}")
            print(f"Contact         : {patient[4]}")
            print(f"Address         : {patient[5]}")
            print(f"Disease         : {patient[6]}")
            print(f"Symptoms        : {patient[7]}")
            print(f"Medical History : {patient[8]}")
            print('=' * 40)
    
    def update_patient(self):
        patient_id = get_int("Enter Patient ID: ")
        if patient_id is None:
            return
        
        patient = self.db.fetch_one("SELECT * FROM patients WHERE patient_id = ?",(patient_id,))
        if not patient:
            print("Patient not found.")
            return

        if patient_id <= 0:
            print("Invalid Patient ID")
            return

        print("\nWhat do you want to update?")
        print("1. Name\n2.Age\n3.Gender\n4.Contact\n5.Address\n6.Disease\n7.Symptoms\n8.Medical History")

        choice = input("Enter your choice: ")
        if choice == "1":
            new_name = get_non_empty("Enter New Name: ")
            if new_name is None:
                return
            self.db.update(
                "patients",
                "name = ?",
                "patient_id = ?",
                (new_name, patient_id)
            )
            print("Name updated successfully!")
        
        elif choice == "2":
            new_age = get_int("Enter New Age: ")
            if new_age is None:
                return
            self.db.update(
                "patients",
                "age = ?",
                "patient_id = ?",
                (new_age, patient_id)
            )
            print("Age updated successfully!")
        
        elif choice == "3":
            new_gender = input("Enter New Gender: ")
            self.db.update(
                "patients",
                "gender = ?",
                "patient_id = ?",
                (new_gender, patient_id)
            )
            print("Gender updated successfully!")

        elif choice == "4":
            new_contact = get_contact("Enter New contact: ")
            if new_contact is None:
                return
            
            self.db.update(
                "patients",
                "contact = ?",
                "patient_id = ?",
                (new_contact, patient_id)
            )
            print("Contact updated successfully!")

        elif choice == "5":
            new_address = input("Enter New Address: ")
            self.db.update(
                "patients",
                "address = ?",
                "patient_id = ?",
                (new_address, patient_id)
            )
            print("Address updated successfully!")

        elif choice == "6":
            new_disease = input("Enter New Disease: ")
            self.db.update(
                "patients",
                "disease = ?",
                "patient_id = ?",
                (new_disease, patient_id)
            )
            print("Disease updated successfully!")

        elif choice == "7":
            new_symptoms = input("Enter New Symptoms: ")
            self.db.update(
                "patients",
                "symptoms = ?",
                "patient_id = ?",
                (new_symptoms, patient_id)
            )
            print("Symptoms updated successfully!")

        elif choice == "8":
            new_history = input("Enter New Medical History: ")
            self.db.update(
                "patients",
                "medical_history = ?",
                "patient_id = ?",
                (new_history, patient_id)
            )
            print("Medical History updated successfully!")

        else:
            print("Invalid Choice")

    
    def delete_patient(self):
        patient_id = get_int("\nEnter Patient ID to delete: ")
        if patient_id is None:
            return
        
        patient = self.db.fetch_one("SELECT * FROM patients WHERE patient_id = ?",(patient_id,))
        if not patient:
            print("Patient not found.")
            return
        
        self.db.delete(
            "patients",
            "patient_id = ?",
            (patient_id,)
        )
        print("\nPatient deleted successfully!")
        print('=' * 40)

    
    def search_patient(self):
        patient_id = get_int("Enter Patient ID: ")
        if patient_id is None:
            return

        patient = self.db.fetch_one(
            "SELECT * FROM patients WHERE patient_id = ?",
            (patient_id,)
        )
        if patient:
            print("-" * 40)
            print(f"Patient ID      : {patient[0]}")
            print(f"Name            : {patient[1]}")
            print(f"Age             : {patient[2]}")
            print(f"Gender          : {patient[3]}")
            print(f"Contact         : {patient[4]}")
            print(f"Address         : {patient[5]}")
            print(f"Disease         : {patient[6]}")
            print(f"Symptoms        : {patient[7]}")
            print(f"Medical History : {patient[8]}")
        else:
            print("Patient not found.")

    
    
