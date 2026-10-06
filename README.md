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

## Movies
The database currently contains 63 movies.
Movies with a franchise number can also be guessed as `<Franchise>: <Number>` (e.g. `Toy Story: 2`),
and the first movie of a franchise by the franchise name alone (e.g. `The Lord of the Rings`).

Title | Year | Franchise | No.
------|------|-----------|----
Alien | 1979 | Alien | 1
Aliens | 1986 | Alien | 2
Avatar | 2009 | Avatar | 1
Back to the Future | 1985 | Back to the Future | 1
Back to the Future Part II | 1989 | Back to the Future | 2
Batman Begins | 2005 | Batman | –
Braveheart | 1995 | – | –
Casablanca | 1942 | – | –
Django Unchained | 2012 | – | –
Dune | 2021 | Dune | 1
Fight Club | 1999 | – | –
Finding Nemo | 2003 | Finding Nemo | 1
Forrest Gump | 1994 | – | –
Get Out | 2017 | – | –
Gladiator | 2000 | Gladiator | 1
Gladiator II | 2024 | Gladiator | 2
Goodfellas | 1990 | – | –
Harry Potter and the Philosopher's Stone | 2001 | Harry Potter | 1
Harry Potter and the Prisoner of Azkaban | 2004 | Harry Potter | 3
Inception | 2010 | – | –
Inglourious Basterds | 2009 | – | –
Interstellar | 2014 | – | –
Joker | 2019 | Joker | 1
Jurassic Park | 1993 | Jurassic Park | 1
Jurassic World | 2015 | Jurassic Park | 4
La La Land | 2016 | – | –
Mad Max: Fury Road | 2015 | Mad Max | 4
Memento | 2000 | – | –
Oppenheimer | 2023 | – | –
Parasite | 2019 | – | –
Pirates of the Caribbean: The Curse of the Black Pearl | 2003 | Pirates of the Caribbean | 1
Pulp Fiction | 1994 | – | –
Saving Private Ryan | 1998 | – | –
Schindler's List | 1993 | – | –
Shrek | 2001 | Shrek | 1
Spirited Away | 2001 | – | –
Star Wars | 1977 | Star Wars | 1
Terminator 2: Judgment Day | 1991 | The Terminator | 2
The Avengers | 2012 | The Avengers | 1
The Dark Knight | 2008 | Batman | –
The Dark Knight Rises | 2012 | Batman | –
The Departed | 2006 | – | –
The Empire Strikes Back | 1980 | Star Wars | 2
The Godfather | 1972 | The Godfather | 1
The Godfather Part II | 1974 | The Godfather | 2
The Green Mile | 1999 | – | –
The Lion King | 1994 | The Lion King | 1
The Lord of the Rings: The Fellowship of the Ring | 2001 | The Lord of the Rings | 1
The Lord of the Rings: The Return of the King | 2003 | The Lord of the Rings | 3
The Matrix | 1999 | The Matrix | 1
The Matrix Reloaded | 2003 | The Matrix | 2
The Prestige | 2006 | – | –
The Shawshank Redemption | 1994 | – | –
The Shining | 1980 | The Shining | 1
The Silence of the Lambs | 1991 | Hannibal Lecter | –
The Sixth Sense | 1999 | – | –
Titanic | 1997 | – | –
Toy Story | 1995 | Toy Story | 1
Toy Story 2 | 1999 | Toy Story | 2
Toy Story 3 | 2010 | Toy Story | 3
Unforgiven | 1992 | – | –
Up | 2009 | – | –
Whiplash | 2014 | – | –
