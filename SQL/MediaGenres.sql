SELECT genres.name
FROM genres
JOIN media_genres
    ON genres.id = media_genres.genre_id
JOIN media
    ON media.id = media_genres.media_id
WHERE media.title = ?
