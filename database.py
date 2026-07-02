import os
from dotenv import load_dotenv
import psycopg
from psycopg.rows import dict_row

load_dotenv()

def get_connection():
    return psycopg.connect(
        host="localhost",
        user="postgres",
        password=os.getenv("DB_PASSWORD"),
        dbname="mentorlink",
        port=5432,
        row_factory=dict_row
    )

def recuperer_mentors():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mentors")
    mentors = cursor.fetchall()
    cursor.close()
    conn.close()
    return mentors