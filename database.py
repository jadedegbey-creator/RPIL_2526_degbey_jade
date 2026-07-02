import psycopg
from psycopg.rows import dict_row

def get_connection():
    return psycopg.connect(
        host="localhost",
        user="postgres",
        password="Brivin",
        dbname="mentorlink",
        port=5432,
        row_factory=dict_row
    )

def recuperer_mentors():
    """Récupère tous les mentors depuis la base de données."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mentors")
    mentors = cursor.fetchall()
    cursor.close()
    conn.close()
    return mentors