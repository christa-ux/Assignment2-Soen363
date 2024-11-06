CREATE VIEW movie_summary AS
SELECT
    tmdb_id,
    imdb_id,
    title,
    plot AS description,
    content_rating,
    release_year,
    (SELECT COUNT(*) FROM movie_keyword WHERE movie_id = movies.id) AS keyword_count,
    (SELECT COUNT(*) FROM movie_country WHERE movie_id = movies.id) AS country_count
FROM movies;
