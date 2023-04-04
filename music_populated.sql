DROP TABLE IF EXISTS Artist;
CREATE TABLE Artist (id INTEGER PRIMARY KEY, name TEXT);
INSERT INTO Artist(name) VALUES ('Megadeth');

DROP TABLE IF EXISTS Albums;
CREATE TABLE Albums (id INTEGER PRIMARY KEY, album_title TEXT, artist_id INT);
INSERT INTO Albums(album_title, artist_id) VALUES ('Rust In Peace', 1);

DROP TABLE IF EXISTS Songs;
CREATE TABLE Songs (song_name TEXT, artist_id INT, album_ID INT, track_num INT, length INT);
INSERT INTO Songs VALUES('Holy Wars... The Punishment Due', 1, 1, 1, 396);
INSERT INTO Songs VALUES('Hangar 18', 1, 1, 2, 314);
INSERT INTO Songs VALUES('Take No Prisoners', 1, 1, 3, 208);
INSERT INTO Songs VALUES('Five Magics', 1, 1, 4, 342);
INSERT INTO Songs VALUES('Poison Was The Cure', 1, 1, 5, 178);
INSERT INTO Songs VALUES('Lucretia', 1, 1, 6, 238);
INSERT INTO Songs VALUES('Dawn Patrol', 1, 1, 7, 110);
INSERT INTO Songs VALUES('Rust In Peace... Polaris', 1, 1, 8, 336);
