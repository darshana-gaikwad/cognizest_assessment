import sqlite3
import random

conn = sqlite3.connect("clinic.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS patients (
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    city TEXT,
    gender TEXT
)
""")

cities = ["Pune","Mumbai","Delhi","Nagpur"]

for i in range(200):
    cursor.execute(
        "INSERT INTO patients(first_name,last_name,city,gender) VALUES (?,?,?,?)",
        (f"Name{i}", f"Surname{i}", random.choice(cities), random.choice(["M","F"]))
    )

conn.commit()
conn.close()

print("Database and dummy data created successfully")