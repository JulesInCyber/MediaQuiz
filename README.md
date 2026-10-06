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

> **Note:** Run the scripts in the order shown above.
> `media_people.sql` and `media_genres.sql` link entries by title and name, so they only work after `media.sql`, `people.sql` and `genres.sql` have been loaded.
> If one of them is skipped, the game still starts, but the matching hints stay empty (e.g. "It was directed by " with no name).
>
> To check that the links were loaded, both counts should be greater than 0:
>
> ```shell
> sqlite3 data/quiz.db "SELECT COUNT(*) FROM media_people; SELECT COUNT(*) FROM media_genres;"
> ```
>
> If a count is 0, run the missing script again. It is safe to re-run, since existing links are skipped.
