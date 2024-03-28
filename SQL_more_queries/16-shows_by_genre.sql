-- Active: 1710694390878@@127.0.0.1@3306@hbtn_0d_tvshows
-- TASK : oa
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
ORDER BY tv_shows.title, tv_genres.name ASC;
