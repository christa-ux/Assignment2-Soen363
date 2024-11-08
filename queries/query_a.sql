-- query_a.sql: Count movies with and without IMDb ID
SELECT
    COUNT(*) FILTER (WHERE imdb_id IS NOT NULL) AS with_imdb_id,
    COUNT(*) FILTER (WHERE imdb_id IS NULL) AS without_imdb_id
FROM movies;
