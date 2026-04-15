import sqlite3

def run_sql(query):
    conn = sqlite3.connect("clinic.db")
    cursor = conn.cursor()

    cursor.execute(query)

    results = cursor.fetchall()

    conn.close()

    return results