import random
import sqlite3

test_db = "testing/test.db"
live_db = "data/quiz.db"

def get_random_media():
    connection = sqlite3.connect(test_db)
    with open ("SQL/RandomMedia.sql", "r") as file:
        query = file.read()

    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    random_media = cursor.fetchone()
    connection.close()

    return random_media
    
def get_media_actors(media):
    connection = sqlite3.connect(test_db)
    with open ("SQL/MediaActors.sql", "r") as file:
        query = file.read()

    cursor = connection.cursor()
    cursor.execute(query, (media,))
    actors = cursor.fetchall()
    connection.close()

    return [actor[0] for actor in actors]

def get_media_director(media):
    connection = sqlite3.connect(test_db)
    with open ("SQL/MediaDirector.sql") as file:
        query = file.read()

    cursor = connection.cursor()
    cursor.execute(query, (media,))
    directors = cursor.fetchall()
    connection.close()

    return [director[0] for director in directors]
