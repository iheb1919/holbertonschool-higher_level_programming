-- script that lists all Comedy shows in the database hbtn_0d_tvshows
SELECT c.title
FROM tv_genres a, tv_show_genres b, tv_shows c
WHERE a.id = b.genre_id AND b.show_id = c.id AND a.name = 'Comedy'
ORDER BY c.title ASC;
