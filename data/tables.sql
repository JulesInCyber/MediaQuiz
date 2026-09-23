<<<<<<< HEAD
SQLite version 3.53.4 2026-07-24 19:02:57
Enter ".help" for usage hints.
[?2004hsqlite> ^C[?2004l[?2004h[C[C[C[C[C[C[C[C^C[?2004l
=======
-- Creating tables
CREATE TABLE media (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    release_year INTEGER,
    type TEXT NOT NULL
);

CREATE TABLE people (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE genres (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE media_people (
    media_id INTEGER NOT NULL,
    person_id INTEGER NOT NULL,
    role TEXT NOT NULL,

    PRIMARY KEY (media_id, person_id, role),

    FOREIGN KEY (media_id) REFERENCES media(id),
    FOREIGN KEY (person_id) REFERENCES people(id)
);

CREATE TABLE media_genres (
    media_id INTEGER NOT NULL,
    genre_id INTEGER NOT NULL,

    PRIMARY KEY (media_id, genre_id),

    FOREIGN KEY (media_id) REFERENCES media(id),
    FOREIGN KEY (genre_id) REFERENCES genres(id)
);

CREATE TABLE quotes (
    id INTEGER PRIMARY KEY,
    media_id INTEGER NOT NULL,
    quote TEXT NOT NULL,

    FOREIGN KEY (media_id) REFERENCES media(id)
);
>>>>>>> parent of e6c5012 (Updated to check existing tables)
