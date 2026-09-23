--Filling up People-Table
INSERT INTO people (name)
VALUES
    ('Keanu Reeves'),
    ('Laurence Fishburne'),
    ('Hugo Weaving'),
    ('Lana Wachowski'),
    ('Lilly Wachowski'),
    ('Frank Darabont'),
    ('Tim Robbins'),
    ('Morgan Freeman')
ON CONFLICT (name) DO NOTHING;
