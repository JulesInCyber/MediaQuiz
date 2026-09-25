from queries import *

def normalize_answer(answer):
    normalized = answer.strip().casefold()
    return normalized

def check_answer(answer, title):
    result = None
    normalized_answer = normalize_answer(answer)
    normalized_title = normalize_answer(title)
    if normalized_answer == normalized_title:
        result = True
    else:
        result = False

    return result

def get_clues():
    media = get_random_media()

    media_id = media[0]
    media_title = media[1]
    media_release = media[2]

    genres = get_media_genres(media_id)
    director = get_media_director(media_id)
    actors = get_media_actors(media_id)

    clues = [
        f"Year of release was {media_release}",
        f"The media has the following genre(s): {', '.join(genres)}",
        f"It was directed by {', '.join(director)}",
        f"The actors {', '.join(actors)} are part of the cast.",
        ]

    return clues


# all_clues = get_clues()
#
# for i, clue in enumerate(all_clues):
#     print(i+1, clue)
#
