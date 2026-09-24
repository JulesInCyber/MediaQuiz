INSERT INTO media_genres
    (media_id, genre_id)
VALUES
    (1, 1),
    (1, 2),
    (2, 3)
ON CONFLICT (media_id, genre_id)
DO NOTHING;
