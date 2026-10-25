from models.doctor import Doctor
from services.database import Database
from utils.validation import get_non_empty,get_contact,get_int

class DoctorService:

    def __init__(self):
        self.db = Database()
        self.db.create_doctor_table()


    def add_doctor(self):
    
        name = get_non_empty("\nEnter Doctor Name: ")
        if name is None:
            return
        specialization = get_non_empty("Enter Specialization: ")
        if specialization is None:
            return
        contact = get_contact("Enter Contact: ")
        if contact is None:
            return        

        doctor = Doctor(name, specialization, contact)

        self.db.insert(
            "doctors",
            ["name", "specialization", "contact"],
            (
                doctor.name,
                doctor.specialization,
                doctor.contact
            )
        )
        print("\nDoctor added successfully!")

    def view_doctors(self):
    
        doctors = self.db.fetch_all("SELECT * FROM doctors")
        if not doctors:
            print("\nNo doctors found.")
            return

        for d in doctors:
            print("-" * 40)
            print(f"Doctor ID      : {d[0]}")
            print(f"Name           : {d[1]}")
            print(f"Specialization : {d[2]}")
            print(f"Contact        : {d[3]}")
            print("=" * 40)


    def update_doctor(self):
    
        doctor_id = get_int("\nEnter Doctor ID: ")
        if doctor_id is None:
            return
        
        doctor = self.db.fetch_one("SELECT * FROM doctors WHERE doctor_id = ?",(doctor_id,))
        if not doctor:
            print("Doctor not found.")
            return
            
        print("1. Name")
        print("2. Specialization")
        print("3. Contact")

        choice = input("\nWhat do you want to update? ")

        if choice == "1":
            new_value = get_non_empty("Enter new name: ")
            if new_value is None:
                return
            column = "name"
        elif choice == "2":
            new_value = input("Enter new specialization: ")
            column = "specialization"
        elif choice == "3":
            new_value = get_contact("Enter new contact: ")
            if new_value is None:
                return
            column = "contact"
        else:
            print("Invalid choice")
            return

        self.db.update(
            "doctors",
            f"{column} = ?",
            "doctor_id = ?",
            (new_value, doctor_id)
        )
        print("\nDoctor updated successfully!")


    def delete_doctor(self):
    
        doctor_id = get_int("\nEnter Doctor ID to delete: ")
        if doctor_id is None:
            return

        doctor = self.db.fetch_one("SELECT * FROM doctors WHERE doctor_id = ?",(doctor_id,))
        if not doctor:
            print("Doctor not found.")
            return

        self.db.delete(
            "doctors",
            "doctor_id = ?",
            (doctor_id,)
        )
        print("\nDoctor deleted successfully!")

    def get_all_doctors(self):
        return self.db.fetch_all("SELECT * FROM doctors")

    def create_doctor(self, name, specialization, contact):
        doctor = Doctor(name, specialization, contact)

        self.db.insert(
            "doctors",
            ["name", "specialization", "contact"],
            (doctor.name, doctor.specialization, doctor.contact)
        )

    def update_doctor_record(self, doctor_id, name, specialization, contact):
        self.db.update(
            "doctors",
            "name = ?, specialization = ?, contact = ?",
            "doctor_id = ?",
            (name, specialization, contact, doctor_id)
        )

    def delete_doctor_by_id(self, doctor_id):
        self.db.delete(
            "doctors",
            "doctor_id = ?",
            (doctor_id,)
        )