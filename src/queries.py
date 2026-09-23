import sqlite3

def random_media():
    connection = sqlite3.connect("data/quiz.db")
    cursor = connection.cursor()

    cursor.execute("""
                   SELECT title
                   FROM media
                   ORDER BY random()
                   LIMIT 1;
                   """)

    media = cursor.fetchone()
    connection.close()

    return media 

random_media = random_media()

print(random_media[0])
