import sqlite3
from tabulate import tabulate

# CONNECT TO THE DATABASE OR CREATE IT DOES NOR EXIST
conn = sqlite3.connect('clinic reservation.db')

# CREATE A CURSOR TO PERFORM DATABASE OPERATIONS
cursor = conn.cursor()

# CREATE USER TABLE
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        user_type TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')

# CREATE A TABLE OF RATING
cursor.execute('''
    CREATE TABLE IF NOT EXISTS rating (
        clinic_id INTEGER PRIMARY KEY AUTOINCREMENT,
        rate TEXT NOT NULL,
        opinion TEXT NOT NULL,
        FOREIGN KEY (clinic_id) REFERENCES clinics(id)
    )
''')

# CREATE USER TABLE MEDICATION RECORD
cursor.execute('''
    CREATE TABLE IF NOT EXISTS medication_record (
        user_id INTEGER PRIMARY KEY,
        user_name TEXT NOT NULL,
        clinic_id TEXT NOT NULL,
        name_medicine TEXT NOT NULL,
        medicine_id TEXT NOT NULL,
        status TEXT NOT NULL,
        instructions TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
''')

# CREATE AN APPOINTMENT SCHEDULE
cursor.execute('''
    CREATE TABLE IF NOT EXISTS appointments (
        appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        clinic_name TEXT NOT NULL,
        datetime TEXT NOT NULL,
        status TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
''')

# CREATE A TABLE OF CLINIC
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clinics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        contact_number TEXT NOT NULL,
        address TEXT NOT NULL,
        email TEXT NOT NULL,
        times TEXT NOT NULL
    )
''')

# APPLY CHANGES
conn.commit()

#
# # ADD ROW
# cursor.execute("INSERT INTO users (name, address,email, user_type, password) "
#                "VALUES ('john', '123 Main St', 'zahrahm2004@gmail.com','user_type', 'password_value')")
#
# # COMMIT THE INSERTION
# conn.commit()

cursor.execute("select * from users")

rows = cursor.fetchall()

headers = ["name", "email", "user_type", "password"]


table = tabulate(rows, headers, tablefmt="grid")

# Print the table
print(table)

# # CLOSE THE CONNECTION
# conn.close()
