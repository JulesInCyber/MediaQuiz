import re

from src.res.queries import *

def normalize_answer(answer):
    normalized = answer.strip().casefold()
    return normalized

ROMAN_NUMERALS = {
    "i": 1, "ii": 2, "iii": 3, "iv": 4, "v": 5,
    "vi": 6, "vii": 7, "viii": 8, "ix": 9, "x": 10,
}

SEQUEL_PATTERN = re.compile(
    r"(?P<base>.+?)(?:\s*:\s*|\s+)(?:(?:part|chapter|episode)\s+)?"
    r"(?P<number>\d+|" + "|".join(sorted(ROMAN_NUMERALS, key=len, reverse=True)) + r")"
)

def strip_article(text):
    return text[4:] if text.startswith("the ") else text

def split_sequel(text):
    # "Toy Story 2" -> ("toy story", 2), "The Godfather Part II" -> ("godfather", 2)
    normalized = normalize_answer(text)
    match = SEQUEL_PATTERN.fullmatch(normalized)

    if match:
        number = match["number"]
        number = int(number) if number.isdigit() else ROMAN_NUMERALS[number]
        return strip_article(match["base"]), number

    # No number means the first movie, e.g. "The Lord of the Rings"
    return strip_article(normalized), 1

def normalize_title(text):
    # Every sequel is written as "<franchise>: <number>"
    base, number = split_sequel(text)
    return f"{base}: {number}"

def check_answer(answer, title, franchise=None, number=None):
    if normalize_answer(answer) == normalize_answer(title):
        return True

    # Also accept "<franchise>: <number>", e.g. "The Lord of the Rings: 1"
    if franchise and number:
        return normalize_title(answer) == normalize_title(f"{franchise}: {number}")

    return False

def get_franchise(title):
    # "Toy Story 2" -> "toy story", "Star Wars: A New Hope" -> "star wars"
    normalized = normalize_answer(title)
    base = normalized.split(":")[0].split(" - ")[0]
    words = base.split()

    while words and (words[-1].isdigit() or words[-1] in ROMAN_NUMERALS
                     or words[-1] in ("part", "chapter", "episode")):
        words.pop()

    # Titles that are only a number (e.g. "1917") have no franchise part
    if not words:
        return strip_article(normalized)

    return strip_article(" ".join(words))

def check_franchise(answer, title, franchise=None, number=None):
    if check_answer(answer, title, franchise, number):
        return False

    # Use the franchise from the database, fall back to the title
    media_franchise = strip_article(normalize_answer(franchise or get_franchise(title)))
    guess_franchise = get_media_franchise(answer) or get_franchise(answer)
    guess_franchise = strip_article(normalize_answer(guess_franchise))

    if guess_franchise == media_franchise:
        return True

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
