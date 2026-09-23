INSERT INTO media (title, release_year, type)
VALUES
    ('The Matrix', 1999, 'movie')
ON CONFLICT (title) DO NOTHING;
