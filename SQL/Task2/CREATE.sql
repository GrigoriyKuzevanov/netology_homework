CREATE TABLE IF NOT EXISTS Genres (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS Artists (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS Albums (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	year_release INTEGER CHECK(year_release>1900 AND year_release<2100) NOT NULL
);

CREATE TABLE IF NOT EXISTS Tracks (
	id SERIAL PRIMARY KEY,
	album_id INTEGER REFERENCES Albums(id),
	name VARCHAR(50) NOT NULL,
	duration_sec INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS Compilations (
	id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	year_release INTEGER CHECK(year_release>1900 AND year_release<2100) NOT NULL
);

CREATE TABLE IF NOT EXISTS ArtistGenre (
	artist_id INTEGER REFERENCES Artists(id),
	genre_id INTEGER REFERENCES Genres(id),
	CONSTRAINT artist_genre_pk PRIMARY KEY (artist_id, genre_id)
);

CREATE TABLE IF NOT EXISTS ArtistAlbum (
	artist_id INTEGER REFERENCES Artists(id),
	album_id INTEGER REFERENCES Albums(id),
	CONSTRAINT artist_album_pk PRIMARY KEY (artist_id, album_id)
);

CREATE TABLE IF NOT EXISTS CompilationTrack (
	track_id INTEGER REFERENCES Tracks(id),
	compilation_id INTEGER REFERENCES Compilations(id),
	CONSTRAINT compilation_track_pk PRIMARY KEY (track_id, compilation_id)
);