SELECT people.name
FROM people
JOIN media_people
    ON people.id = media_people.person_id
JOIN media
    ON media.id = media_people.media_id
WHERE media.title = ?
    AND media_people.role = 'director';
