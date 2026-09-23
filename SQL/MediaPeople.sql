SELECT 
    media.title,
    people.name,
    media_people.role 
FROM media_people
JOIN media 
    ON media.id = media_people.media_id 
JOIN people 
    on people.id = media_people.person_id
;
