--script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT a.name FROM tv_genres a, tv_show_genres b, tv_shows c
WHERE a.id = b.genre_id AND b.show_id = c.id AND c.title = 'Dexter'
ORDER BY a.name ASC;
