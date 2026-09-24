import sqlite3

test_db = "testing/test.db"
live_db = "data/quiz.db"

def connect_db():
    # Change Database after Testing
    connection = sqlite3.connect(test_db)
    return connection

def get_random_media():
    connection = connect_db()
    with open ("SQL/RandomMedia.sql", "r") as file:
        query = file.read()

    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    random_media = cursor.fetchone()
    connection.close()

    return random_media
    
def get_media_actors(media):
    connection = connect_db()
    with open ("SQL/MediaActors.sql", "r") as file:
        query = file.read()

    cursor = connection.cursor()
    cursor.execute(query, (media,))
    actors = cursor.fetchall()
    connection.close()

    return [actor[0] for actor in actors]

def get_media_director(media):
    connection = connect_db()
    with open ("SQL/MediaDirector.sql", "r") as file:
        query = file.read()

    cursor = connection.cursor()
    cursor.execute(query, (media,))
    directors = cursor.fetchall()
    connection.close()

    return [director[0] for director in directors]

def get_media_genres(media):
    connection = connect_db()
    with open ("SQL/MediaGenres.sql", "r") as file:
        query = file.read()

    cursor = connection.cursor()
    cursor.execute(query, (media,))
    genres = cursor.fetchall()
    connection.close()

    return [genre[0] for genre in genres]
