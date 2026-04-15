from vanna_setup import vn

vn.train(ddl="""
CREATE TABLE patients (
patient_id INTEGER PRIMARY KEY,
first_name TEXT,
last_name TEXT,
city TEXT,
gender TEXT
)
""")

vn.train(
question="Show all patients",
sql="SELECT * FROM patients"
)

vn.train(
question="Show patients from Pune",
sql="SELECT * FROM patients WHERE city='Pune'"
)

vn.train(
question="Count patients",
sql="SELECT COUNT(*) FROM patients"
)

print("Training completed")