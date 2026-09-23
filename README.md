## Database Scheme

### Table `media`
This table is the main piece of information used.
Every media is listet with basic information. 

**Example**

id | title          | release_year | type
---|----------------|--------------|-------
1  | The Matrix     | 1999         | movie
2  | Inception      | 2010         | movie
3  | The Witcher 3  | 2015         | game

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
