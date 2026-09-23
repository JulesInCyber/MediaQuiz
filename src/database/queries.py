import sqlite3

test_db = "testing/test.db"
live_db = "data/quiz.db"

def random_media():
    connection = sqlite3.connect(test_db)
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

