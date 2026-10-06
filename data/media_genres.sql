-- Links are resolved by title and genre name, so the ids
-- do not depend on the order in which rows were inserted.
WITH links (title, genre) AS (
    VALUES
        ('The Matrix', 'Action'),
        ('The Matrix', 'Science Fiction'),
        ('The Shawshank Redemption', 'Drama'),
        ('Inception', 'Action'),
        ('Inception', 'Science Fiction'),
        ('Inception', 'Thriller'),
        ('The Godfather', 'Crime'),
        ('The Godfather', 'Drama'),
        ('Pulp Fiction', 'Crime'),
        ('Pulp Fiction', 'Drama'),
        ('The Dark Knight', 'Action'),
        ('The Dark Knight', 'Crime'),
        ('The Dark Knight', 'Drama'),
        ('Forrest Gump', 'Drama'),
        ('Forrest Gump', 'Romance'),
        ('Forrest Gump', 'Comedy'),
        ('Fight Club', 'Drama'),
        ('Fight Club', 'Thriller'),
        ('Titanic', 'Drama'),
        ('Titanic', 'Romance'),
        ('Jurassic Park', 'Adventure'),
        ('Jurassic Park', 'Science Fiction'),
        ('Gladiator', 'Action'),
        ('Gladiator', 'Adventure'),
        ('Gladiator', 'Drama'),
        ('The Silence of the Lambs', 'Crime'),
        ('The Silence of the Lambs', 'Thriller'),
        ('Schindler''s List', 'Drama'),
        ('Schindler''s List', 'History'),
        ('Schindler''s List', 'War'),
        ('Star Wars', 'Science Fiction'),
        ('Star Wars', 'Adventure'),
        ('Star Wars', 'Action'),
        ('Back to the Future', 'Science Fiction'),
        ('Back to the Future', 'Adventure'),
        ('Back to the Future', 'Comedy'),
        ('Alien', 'Horror'),
        ('Alien', 'Science Fiction'),
        ('Interstellar', 'Science Fiction'),
        ('Interstellar', 'Adventure'),
        ('Interstellar', 'Drama'),
        ('The Lion King', 'Animation'),
        ('The Lion King', 'Family'),
        ('The Lion King', 'Drama'),
        ('Toy Story', 'Animation'),
        ('Toy Story', 'Family'),
        ('Toy Story', 'Comedy'),
        ('Toy Story', 'Adventure'),
        ('Goodfellas', 'Crime'),
        ('Goodfellas', 'Drama'),
        ('Parasite', 'Thriller'),
        ('Parasite', 'Drama'),
        ('Parasite', 'Comedy'),
        ('Saving Private Ryan', 'War'),
        ('Saving Private Ryan', 'Drama'),
        ('Casablanca', 'Drama'),
        ('Casablanca', 'Romance'),
        ('Casablanca', 'War'),
        ('Unforgiven', 'Western'),
        ('Unforgiven', 'Drama'),
        ('The Shining', 'Horror'),
        ('The Shining', 'Drama')
)
INSERT INTO media_genres
    (media_id, genre_id)
SELECT media.id, genres.id
FROM links
JOIN media ON media.title = links.title
JOIN genres ON genres.name = links.genre
WHERE true
ON CONFLICT (media_id, genre_id)
DO NOTHING;
