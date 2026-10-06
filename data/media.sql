INSERT INTO media (title, release_year, type)
VALUES
    ('The Matrix', 1999, 'movie'),
    ('The Shawshank Redemption', 1994, 'movie'),
    ('Inception', 2010, 'movie'),
    ('The Godfather', 1972, 'movie'),
    ('Pulp Fiction', 1994, 'movie'),
    ('The Dark Knight', 2008, 'movie'),
    ('Forrest Gump', 1994, 'movie'),
    ('Fight Club', 1999, 'movie'),
    ('Titanic', 1997, 'movie'),
    ('Jurassic Park', 1993, 'movie'),
    ('Gladiator', 2000, 'movie'),
    ('The Silence of the Lambs', 1991, 'movie'),
    ('Schindler''s List', 1993, 'movie'),
    ('Star Wars', 1977, 'movie'),
    ('Back to the Future', 1985, 'movie'),
    ('Alien', 1979, 'movie'),
    ('Interstellar', 2014, 'movie'),
    ('The Lion King', 1994, 'movie'),
    ('Toy Story', 1995, 'movie'),
    ('Goodfellas', 1990, 'movie'),
    ('Parasite', 2019, 'movie'),
    ('Saving Private Ryan', 1998, 'movie'),
    ('Casablanca', 1942, 'movie'),
    ('Unforgiven', 1992, 'movie'),
    ('The Shining', 1980, 'movie')
ON CONFLICT (title)
DO UPDATE SET
    release_year = excluded.release_year,
    type = excluded.type;
