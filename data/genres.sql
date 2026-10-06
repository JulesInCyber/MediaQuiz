INSERT INTO genres (name)
VALUES
    ('Action'),
    ('Science Fiction'),
    ('Drama'),
    ('Romance'),
    ('Comedy'),
    ('Tragedy'),
    ('Thriller'),
    ('Crime'),
    ('Adventure'),
    ('History'),
    ('War'),
    ('Horror'),
    ('Animation'),
    ('Family'),
    ('Western')
ON CONFLICT (name)
DO NOTHING;
