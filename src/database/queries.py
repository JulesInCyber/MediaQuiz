import sqlite3

def random_media():
    connection = sqlite3.connect("data/quiz.db")
    cursor = connection.cursor()

    cursor.execute("""
                   SELECT *
                   FROM media
                   ORDER BY random()
                   LIMIT 1;
                   """)

    media = cursor.fetchone()
    connection.close()

    return media 

