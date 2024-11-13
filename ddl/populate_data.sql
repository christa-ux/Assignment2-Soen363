--sample movies into the Movie table
INSERT INTO Movie (title, plot, releaseYear, content_Rating, viewerRating, original_language)
VALUES ('The Godfather', 'The aging patriarch...', 1972, 'R', 9.2, 'English');

--data for movies (genres, actors, directors)
INSERT INTO Genre (gname) VALUES ('Drama'), ('Crime') ON CONFLICT DO NOTHING;
INSERT INTO Actor (aAge, aFirst, aMiddle, aLast, aCountry) VALUES (45, 'Al', 'Joseph', 'Pacino', 'USA') ON CONFLICT DO NOTHING;
INSERT INTO Director (dAge, dFirst, dMiddle, dLast, dCountry) VALUES (52, 'Francis', 'Ford', 'Coppola', 'USA') ON CONFLICT DO NOTHING;

-- relationships
INSERT INTO moviegenre (movieID, genreID) VALUES (1, 1), (1, 2);  -- Assuming genre IDs
INSERT INTO movieactor (movieID, actorID) VALUES (1, 1);           -- Assuming actor IDs
INSERT INTO moviedirector (movieID, directorID) VALUES (1, 1);     -- Assuming director IDs

INSERT INTO contentRating (rating) VALUES ('G'), ('PG'), ('PG-13'), ('R'), ('NC-17');
