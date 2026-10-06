from src.res.queries import *

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

SEQUEL_MARKERS = {
    "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x",
    "part", "chapter", "episode",
}

def get_franchise(title):
    # "Toy Story 2" -> "toy story", "Star Wars: A New Hope" -> "star wars"
    normalized = normalize_answer(title)
    base = normalized.split(":")[0].split(" - ")[0]
    words = base.split()

    while words and (words[-1].isdigit() or words[-1] in SEQUEL_MARKERS):
        words.pop()

    # Titles that are only a number (e.g. "1917") have no franchise part
    if not words:
        return normalized

    return " ".join(words)

def check_franchise(answer, title):
    if check_answer(answer, title):
        return False

    return get_franchise(answer) == get_franchise(title)

def get_clues(media):
    # media = get_random_media()

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
