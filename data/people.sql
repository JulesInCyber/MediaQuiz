--Filling up People-Table
INSERT INTO people (name)
VALUES
    ('Keanu Reeves'),
    ('Laurence Fishburne'),
    ('Hugo Weaving'),
    ('Lana Wachowski'),
    ('Lilly Wachowski')
ON CONFLICT (name) DO NOTHING;
