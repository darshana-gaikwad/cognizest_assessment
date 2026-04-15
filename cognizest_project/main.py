from fastapi import FastAPI
from vanna_setup import run_sql

app = FastAPI()

@app.get("/")
def home():
    return {"message": "NL2SQL API running"}

@app.get("/ask")
def ask(question: str):

    if "all patients" in question.lower():
        sql = "SELECT * FROM patients"

    elif "pune" in question.lower():
        sql = "SELECT * FROM patients WHERE city='Pune'"

    elif "count" in question.lower():
        sql = "SELECT COUNT(*) FROM patients"

    else:
        sql = "SELECT * FROM patients LIMIT 5"

    result = run_sql(sql)

    return {
        "question": question,
        "sql": sql,
        "result": result
    }