import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect("database/hospital.db")
        self.connection.execute("PRAGMA foreign_keys = ON")
        self.cursor = self.connection.cursor()

    def create_patient_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT NOT NULL,
            contact TEXT NOT NULL,
            address TEXT,
            disease TEXT,
            symptoms TEXT,
            medical_history TEXT
        )
        """)
        self.connection.commit()

    
    def create_appointment_table(self):
        self.cursor.execute("""
    CREATE TABLE IF NOT EXISTS appointments (
        appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER NOT NULL,
        doctor_name TEXT NOT NULL,
        appointment_date TEXT NOT NULL,
        appointment_time TEXT NOT NULL,
        FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
    )
    """)
        self.connection.commit()

    
    def create_doctor_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS doctors(
        doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        specialization TEXT NOT NULL,
        contact TEXT NOT NULL
    )
    """)
        self.connection.commit()

    
    def execute(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        self.connection.commit()


    def fetch_all(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()

   
    def fetch_one(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchone()

   
    def insert(self, table, columns, values):
        placeholders = ", ".join(["?"] * len(values))
        cols = ", ".join(columns)

        query = f"INSERT INTO {table} ({cols}) VALUES ({placeholders})"
        self.execute(query, values)

    
    def update(self, table, set_clause, condition, params):
        query = f"UPDATE {table} SET {set_clause} WHERE {condition}"
        self.execute(query, params)

    
    def delete(self, table, condition, params):
        query = f"DELETE FROM {table} WHERE {condition}"
        self.execute(query, params)

    
    def close(self):
        self.connection.close()