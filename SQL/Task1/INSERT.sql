INSERT INTO albums (name, year_release)
	VALUES ('Bleach', 2017);

INSERT INTO albums (name, year_release)
	VALUES ('Sweet Oblivion', 2018);

INSERT INTO albums (name, year_release)
	VALUES ('Mudhoney', 2020);

INSERT INTO albums (name, year_release)
	VALUES ('Ten', 2018);

INSERT INTO albums (name, year_release)
	VALUES ('Dirt', 2017);

INSERT INTO albums (name, year_release)
	VALUES ('Seaweed', 2021);

INSERT INTO albums (name, year_release)
	VALUES ('Damaged', 2020);

INSERT INTO albums (name, year_release)
	VALUES ('Goo', 2018);

INSERT INTO artists (name)
	VALUES ('Nirvana');

INSERT INTO artists (name)
	VALUES ('Alice in Chains');

INSERT INTO artists (name)
	VALUES ('Pearl Jam');

INSERT INTO artists (name)
	VALUES ('Screaming Trees');

INSERT INTO artists (name)
	VALUES ('Mudhoney');

INSERT INTO artists (name)
	VALUES ('The Gits');

INSERT INTO artists (name)
	VALUES ('Black Flag');

INSERT INTO artists (name)
	VALUES ('Sonic Youth');

INSERT INTO genres (name)
	VALUES ('Pop');

INSERT INTO genres (name)
	VALUES ('Rock');

INSERT INTO genres (name)
	VALUES ('Indie');

INSERT INTO genres (name)
	VALUES ('Alternative');

INSERT INTO genres (name)
	VALUES ('Punk');

INSERT INTO tracks (album_id, name, duration_sec)
	VALUES (1, 'Blew', 225);

INSERT INTO tracks (album_id, name, duration_sec)
	VALUES (1, 'School', 350);

INSERT INTO tracks (album_id, name, duration_sec)
	VALUES (2, 'Nearly lost you', 430);

INSERT INTO tracks (album_id, name, duration_sec)
	VALUES (2, 'Dollar bill', 363);

INSERT INTO tracks (album_id, name, duration_sec)
	VALUES (3, 'The gift', 430);

INSERT INTO tracks (album_id, name, duration_sec)
	VALUES (3, 'My year', 267);

INSERT INTO tracks (album_id, name, duration_sec)
	VALUES (4, 'Black', 214);

INSERT INTO tracks (album_id, name, duration_sec)
	VALUES (4, 'Alive', 289);

INSERT INTO tracks (album_id, name, duration_sec)
	VALUES (5, 'Them Bones', 350);

INSERT INTO tracks (album_id, name, duration_sec)
	VALUES (5, 'Rooster', 267);

INSERT INTO tracks (album_id, name, duration_sec)
	VALUES (6, 'My king', 278);

INSERT INTO tracks (album_id, name, duration_sec)
	VALUES (6, 'Seaweed', 208);

INSERT INTO tracks (album_id, name, duration_sec)
	VALUES (7, 'No more', 154);

INSERT INTO tracks (album_id, name, duration_sec)
	VALUES (7, 'TV party', 140);

INSERT INTO tracks (album_id, name, duration_sec)
	VALUES (8, 'My friend goo', 285);

INSERT INTO tracks (album_id, name, duration_sec)
	VALUES (8, 'The bedroom', 186);

INSERT INTO compilations (name, year_release)
	VALUES ('Best of the best', 2016);

INSERT INTO compilations (name, year_release)
	VALUES ('Classics Mixtape', 2018);

INSERT INTO compilations (name, year_release)
	VALUES ('Women of rock', 2020);

INSERT INTO compilations (name, year_release)
	VALUES ('Summer rockin', 2021);

INSERT INTO compilations (name, year_release)
	VALUES ('Indie bands', 2019);

INSERT INTO compilations (name, year_release)
	VALUES ('Upbeat', 2021);

INSERT INTO compilations (name, year_release)
	VALUES ('Freedom of choice', 2022);

INSERT INTO compilations (name, year_release)
	VALUES ('The best of rocks', 2021);

INSERT INTO artistalbum
	VALUES (1, 1);

INSERT INTO artistalbum
	VALUES (2, 5);

INSERT INTO artistalbum
	VALUES (3, 4);

INSERT INTO artistalbum
	VALUES (4, 2);

INSERT INTO artistalbum
	VALUES (5, 3);

INSERT INTO artistalbum
	VALUES (6, 6);

INSERT INTO artistalbum
	VALUES (7, 7);

INSERT INTO artistalbum
	VALUES (8, 8);

INSERT INTO artistgenre
	VALUES (1, 1);

INSERT INTO artistgenre
	VALUES (1, 2);

INSERT INTO artistgenre
	VALUES (2, 2);

INSERT INTO artistgenre
	VALUES (2, 4);

INSERT INTO artistgenre
	VALUES (3, 2);

INSERT INTO artistgenre
	VALUES (4, 2);

INSERT INTO artistgenre
	VALUES (4, 4);

INSERT INTO artistgenre
	VALUES (5, 4);

INSERT INTO artistgenre
	VALUES (6, 4);

INSERT INTO artistgenre
	VALUES (6, 5);

INSERT INTO artistgenre
	VALUES (7, 5);

INSERT INTO artistgenre
	VALUES (8, 1);

INSERT INTO artistgenre
	VALUES (8, 3);

INSERT INTO artistgenre
	VALUES (8, 4);

INSERT INTO compilationtrack
	VALUES (1, 1);

INSERT INTO compilationtrack
	VALUES (2, 1);

INSERT INTO compilationtrack
	VALUES (3, 1);

INSERT INTO compilationtrack
	VALUES (4, 2);

INSERT INTO compilationtrack
	VALUES (5, 3);

INSERT INTO compilationtrack
	VALUES (6, 1);

INSERT INTO compilationtrack
	VALUES (7, 4);

INSERT INTO compilationtrack
	VALUES (8, 5);

INSERT INTO compilationtrack
	VALUES (9, 5);

INSERT INTO compilationtrack
	VALUES (10, 6);

INSERT INTO compilationtrack
	VALUES (11, 7);

INSERT INTO compilationtrack
	VALUES (12, 8);

INSERT INTO compilationtrack
	VALUES (13, 8);

INSERT INTO compilationtrack
	VALUES (14, 2);

INSERT INTO compilationtrack
	VALUES (15, 7);

INSERT INTO compilationtrack
	VALUES (16, 1);
