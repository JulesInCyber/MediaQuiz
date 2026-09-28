from src.res.queries import *
from src.res.loop import *

def main():
    media = get_random_media()
    media_id = media[0]
    media_title = media[1]
    media_release = media[2]
    media_type = media[3]
    
    actors = get_media_actors(media_id)
    directors = get_media_director(media_id)
    genres = get_media_genres(media_id)

    all_clues = get_clues()

    for i, clue in enumerate(all_clues):
        print(f"Hint {i+1}: {clue}")
        user_input = input("Make a Guess: ")
        user_answer = normalize_answer(user_input)

        result = check_answer(user_answer, media_title)
        if result == True:
            break

    print(f"The secret {media_type} was: {media_title}")

if __name__ == "__main__":
    main()
