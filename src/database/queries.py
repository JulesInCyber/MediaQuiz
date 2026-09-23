import random
import sqlite3

test_db = "testing/test.db"
live_db = "data/quiz.db"

def get_random_media():
    connection = sqlite3.connect(test_db)
    with open ("SQL/RandomMedia.sql", "r") as file:
        sql_script = file.read()

    cursor = connection.cursor()
    cursor.execute(sql_script)
    connection.commit()
    random_media = cursor.fetchone()
    connection.close()

    return random_media
    
