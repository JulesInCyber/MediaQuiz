INSERT INTO media (title, release_year, type)
VALUES
    ('The Matrix', 1999, 'movie'),
    ('The Shawshank Redemption', 1993, 'movie')
ON CONFLICT (title) DO NOTHING;
