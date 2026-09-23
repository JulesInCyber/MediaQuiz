INSERT INTO media_people
    (media_id, person_id, role)
VALUES
    (1, 1, 'actor'),
    (1, 2, 'actor'),
    (1, 3, 'actor'),
    (1, 4, 'director'),
    (1, 5, 'director'),
    (2, 6, 'director'),
    (2, 7, 'actor'),
    (2, 8, 'actor')
ON CONFLICT (media_id, person_id, role)
DO NOTHING;
