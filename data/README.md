## Starting

from `/MediaQuiz` run `python -m src.game.main`

## Database Scheme

### Table `media`
This table is the main piece of information used.
Every media is listet with basic information. 

**Example**

id | title          | release_year | type  | franchise   | franchise_number
---|----------------|--------------|-------|-------------|-----------------
1  | The Matrix     | 1999         | movie | The Matrix  | 1
2  | Inception      | 2010         | movie | NULL        | NULL
3  | The Witcher 3  | 2015         | game  | The Witcher | 3

`franchise` groups sequels and prequels (e.g. "Toy Story" and "Toy Story 2" both have the franchise `Toy Story`).
It is `NULL` for media that are not part of a franchise.

`franchise_number` is the place of the medium in its franchise, by release order.
It counts all parts of the franchise, also the ones that are not in the database (e.g. "Jurassic World" is `4`).
It lets players guess `<franchise>: <number>`, e.g. `The Lord of the Rings: 3`.
It is `NULL` when there is no franchise or no clear numbering (e.g. the Batman movies).

### Table `people`
This table lists every person that plays a role in any medium.
There are no roles in this table.

**Example**

id | name
---|----------------------
1  | Christopher Nolan
2  | Leonardo DiCaprio
3  | Keanu Reeves
4  | Laurence Fishburne

### Table `media_people`
This table establishes a relation between people and media.

**Example**

media_id | person_id | role
---------|-----------|---------
1        | 1         | director
1        | 2         | actor
1        | 3         | actor
