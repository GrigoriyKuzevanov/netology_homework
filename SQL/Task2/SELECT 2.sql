SELECT id, "name", count(artist_id) FROM genres g
	JOIN artistgenre a ON g.id = a.genre_id
GROUP BY id;

SELECT a.id, a."name", count(t.id) FROM albums a
	JOIN tracks t ON a.id = t.album_id
	WHERE year_release BETWEEN 2019 AND 2020
	GROUP BY a.id;
	
SELECT a.id, a."name", round(avg(duration_sec), 2)  FROM albums a
	JOIN tracks t ON a.id = t.album_id
	GROUP BY a.id;
	
SELECT DISTINCT a."name" FROM artists a
	WHERE a."name" NOT IN (
		SELECT DISTINCT a."name" FROM artists a
			LEFT JOIN artistalbum a2 ON a.id = a2.artist_id
			LEFT JOIN albums a3 ON a3.id = a2.album_id
			WHERE a3.year_release = 2020
	)
	ORDER BY a."name"
	
SELECT c."name"  FROM compilations c
	JOIN compilationtrack c2 ON c.id = c2.compilation_id
	JOIN tracks t ON c2.track_id = t.id
	JOIN albums a ON t.album_id = a.id 
	JOIN artistalbum a2 ON a.id = a2.album_id 
	JOIN artists a3 ON a2.artist_id = a3.id
	WHERE a3."name" = 'Nirvana';
	
SELECT a.id, a."name", count(a4.genre_id)  FROM albums a
	JOIN artistalbum a2 ON a.id = a2.album_id 
	JOIN artists a3 ON a2.artist_id = a3.id 
	JOIN artistgenre a4 ON a3.id = a4.artist_id
	GROUP BY a.id
	HAVING count(a4.genre_id) > 1;
	
SELECT t."name" FROM tracks t 
	LEFT JOIN compilationtrack c ON t.id = c.track_id
	WHERE c.track_id IS NULL;
	
SELECT a."name", t.duration_sec FROM artists a 
	JOIN artistalbum a2 ON a.id = a2.artist_id 
	JOIN albums a3 ON a2.album_id = a3.id 
	JOIN tracks t ON a3.id = t.album_id
	WHERE t.duration_sec = (
		SELECT min(duration_sec) FROM tracks
		);
		
SELECT a.id, a."name", count(t.album_id) FROM albums a
	JOIN tracks t ON a.id = t.album_id 
	GROUP BY a.id
	HAVING count(t.album_id) = (
		SELECT min(s.myc) FROM (
			SELECT count(album_id) myc FROM tracks
				GROUP BY tracks.album_id 
			) s		
		);