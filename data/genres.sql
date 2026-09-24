INSERT INTO genres (name)
VALUES
    ('Action'),
    ('Science Fiction'),
    ('Drama'),
    ('Romance'),
    ('Comedy'),
    ('Tragedy')
ON CONFLICT (name)
DO NOTHING;
