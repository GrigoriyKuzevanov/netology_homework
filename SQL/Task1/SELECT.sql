SELECT name, year_release FROM albums
	WHERE year_release = 2018;
	
SELECT name, duration_sec FROM tracks
	ORDER BY duration_sec DESC 
	LIMIT 1;
	
SELECT name FROM tracks
	WHERE duration_sec >= 210;
	
SELECT name FROM compilations
	WHERE year_release BETWEEN 2018 AND 2020;
	
SELECT name FROM artists
	WHERE name NOT LIKE '% %';
	
SELECT name FROM tracks
	WHERE name iLIKE '%my%';
