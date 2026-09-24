## Initializing
Before the game is ready to play you have to initialize the Database that holds all information used in the game.

```shell
sqlite3 data/quiz.db < data/tables.sql
sqlite3 data/quiz.db < data/media.sql
sqlite3 data/quiz.db < data/people.sql
sqlite3 data/quiz.db < data/genres.sql
sqlite3 data/quiz.db < data/media_people.sql
sqlite3 data/quiz.db < data/media_genres.sql
```

These Commands will Create or Update the Database.
After that you can execute `run.py` from the base directory.
