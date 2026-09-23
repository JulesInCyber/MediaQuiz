-- Creating tables
CREATE TABLE IF NOT EXISTS media (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    release_year INTEGER,
    type TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS people (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS genres (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS media_people (
    media_id INTEGER NOT NULL,
    person_id INTEGER NOT NULL,
    role TEXT NOT NULL,

    PRIMARY KEY (media_id, person_id, role),

    FOREIGN KEY (media_id) REFERENCES media(id),
    FOREIGN KEY (person_id) REFERENCES people(id)
);

CREATE TABLE IF NOT EXISTS media_genres (
    media_id INTEGER NOT NULL,
    genre_id INTEGER NOT NULL,

    PRIMARY KEY (media_id, genre_id),

    FOREIGN KEY (media_id) REFERENCES media(id),
    FOREIGN KEY (genre_id) REFERENCES genres(id)
);

CREATE TABLE IF NOT EXISTS quotes (
    id INTEGER PRIMARY KEY,
    media_id INTEGER NOT NULL,
    quote TEXT NOT NULL,

    FOREIGN KEY (media_id) REFERENCES media(id)
);
