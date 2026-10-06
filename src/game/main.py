from src.res.queries import *
from src.res.loop import *
from src.res.menu import *

def main():
    media = get_random_media()
    media_title = media[1]
    media_type = media[3]
    
    all_clues = get_clues(media)

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
