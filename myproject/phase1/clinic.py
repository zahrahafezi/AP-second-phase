import sqlite3
import random
from sqlite3 import Error
import request


class Clinic:
    connection = sqlite3.connect("C:/Users/TUF/Desktop/Projectphase1/clinic reservation.db")
    cursor = connection.cursor()

    def __init__(self, name, contact_number, address, email, times):
        self.connection = sqlite3.connect("C:/Users/TUF/Desktop/Projectphase1/clinic reservation.db")
        self.cursor = self.connection.cursor()
        self.name = name
        self.address = address
        self.email = email
        self.contact_number = contact_number
        self.times = times

    def add_clinic(self):
        try:
            def generate_random_id():
                random_id = random.randint(1000, 9999)
                return str(random_id)

            clinic_id = generate_random_id()
            self.cursor.execute(
                '''INSERT INTO clinics
                 (id, name, contact_number, address, email, times) 
                 VALUES (?, ?, ?, ?, ?, ?)''',
                (clinic_id, self.name, self.contact_number, self.address, self.email, self.times))

            self.connection.commit()

            api_url = 'http://127.0.0.1:5000/add_clinics'
            clinic_data = {
                "id": clinic_id,
                "name": self.name,
                "contact_number": self.contact_number,
                "address": self.address,
                "email": self.email,
                "times": self.time,
            }
            api_response = requests.post(api_url, json=clinic_data)

            if api_response.status_code == 200:
                print("Clinic data added to API.")
            else:
                print(f"Failed to add clinic data to API. Status code: {api_response.status_code}")
        except Error as e:
            print(f"SQLite error: {e}")

        self.cursor.execute("SELECT * FROM clinics")
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    def update_clinic_info(self):
        try:
            new_name = input("Enter new name (or press Enter to keep current): ")
            if new_name:
                self.name = new_name
                self.cursor.execute('''UPDATE clinics SET name = ?''', (new_name,))
            new_address = input("Enter new address (or press Enter to keep current): ")
            if new_address:
                self.address = new_address
                self.cursor.execute('''UPDATE clinics SET address = ?''', (new_address,))
            new_contact_info = input("Enter new contact_info (or press Enter to keep current): ")
            if new_contact_info:
                self.contact_number = new_contact_info
                self.cursor.execute('''UPDATE clinics SET contact_number = ?''',
                                    (new_contact_info,))
            new_times = input("Enter new time (or press Enter to keep current): ")
            if new_times:
                self.times = new_times
                self.cursor.execute('''UPDATE clinics SET times = ?''',
                                    (new_times,))
            new_email = input("Enter new email (or press Enter to keep current): ")
            if new_email:
                self.email = new_email
                self.cursor.execute('''UPDATE clinics SET email = ?''',
                                    (new_email,))

            self.connection.commit()
            print("Clinic information updated successfully.")
        except Error as e:
            print(f"SQLite error: {e}")

    def view_appointment(self, clinic_id):
        try:
            self.cursor.execute('SELECT user_id and datetime FROM appointments WHERE clinic_id = ?', (clinic_id,))
            appointments = self.cursor.fetchone()
            print(appointments)
        except Error as e:
            print(f"SQLite error: {e}")





#
# clinic1 = Clinic("rose", "here", "email", "0192", "service", True)
# clinic1.update_clinic_info()
