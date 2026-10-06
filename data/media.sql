INSERT INTO media (title, release_year, type, franchise)
VALUES
    ('The Matrix', 1999, 'movie', 'The Matrix'),
    ('The Shawshank Redemption', 1994, 'movie', NULL),
    ('Inception', 2010, 'movie', NULL),
    ('The Godfather', 1972, 'movie', 'The Godfather'),
    ('Pulp Fiction', 1994, 'movie', NULL),
    ('The Dark Knight', 2008, 'movie', 'Batman'),
    ('Forrest Gump', 1994, 'movie', NULL),
    ('Fight Club', 1999, 'movie', NULL),
    ('Titanic', 1997, 'movie', NULL),
    ('Jurassic Park', 1993, 'movie', 'Jurassic Park'),
    ('Gladiator', 2000, 'movie', 'Gladiator'),
    ('The Silence of the Lambs', 1991, 'movie', 'Hannibal Lecter'),
    ('Schindler''s List', 1993, 'movie', NULL),
    ('Star Wars', 1977, 'movie', 'Star Wars'),
    ('Back to the Future', 1985, 'movie', 'Back to the Future'),
    ('Alien', 1979, 'movie', 'Alien'),
    ('Interstellar', 2014, 'movie', NULL),
    ('The Lion King', 1994, 'movie', 'The Lion King'),
    ('Toy Story', 1995, 'movie', 'Toy Story'),
    ('Goodfellas', 1990, 'movie', NULL),
    ('Parasite', 2019, 'movie', NULL),
    ('Saving Private Ryan', 1998, 'movie', NULL),
    ('Casablanca', 1942, 'movie', NULL),
    ('Unforgiven', 1992, 'movie', NULL),
    ('The Shining', 1980, 'movie', 'The Shining')
ON CONFLICT (title)
DO UPDATE SET
    release_year = excluded.release_year,
    type = excluded.type,
    franchise = excluded.franchise;
