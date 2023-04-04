DROP TABLE IF EXISTS Artist;
CREATE TABLE Artist (id INTEGER PRIMARY KEY, name TEXT);

DROP TABLE IF EXISTS Albums;
CREATE TABLE Albums (id INTEGER PRIMARY KEY, album_title TEXT, artist_id INT);

DROP TABLE IF EXISTS Songs;
CREATE TABLE Songs (song_name TEXT, artist_id INT, album_ID INT, track_num INT, length INT);