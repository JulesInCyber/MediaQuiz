-- "Shuffle" Database and select first entry
SELECT *
FROM media
ORDER BY RANDOM()
LIMIT 1;

