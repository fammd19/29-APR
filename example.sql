--Select the titles of all songs on the album "Forbidden"
SELECT title FROM songs JOIN albums on songs.album = albums._id WHERE albums.name = "Forbidden";

--Select the titles of all songs on the album "Forbidden" ordered by track orders
SELECT track, title FROM songs JOIN albums on songs.album = albums._id WHERE albums.name = "Forbidden" ORDER BY track ASC;

--Display all songs for the band "Deep Purple"
SELECT title FROM songs JOIN albums on songs.album = albums._id JOIN artists ON albums.artist = artists._id WHERE artists.name = "Deep Purple";

--Rename the band "Mehitabel" to "Mehitabel_MODIFIED". NOTE that this is an exception to the advice to always fully qualify your column names. SET artists.name won't work, you just need to specify name.
--Check that the record was correctly renamed. 

--Select the titles of all the songs by Aerosmith in alphabetical order. Include only the title in the output.

--Replace the column that you used in the previous answer with count(title) to get just a count of the number of songs.


-- Get the same list as from step 6 but without any duplicates.


--Repeat the previous query to find the number of artists (which, obviously, should be one) and the number of albums.
SELECT COUNT (*) FROM (SELECT DISTINCT * FROM songs);

-- Display all artists and how many songs
SELECT ar.name, COUNT (s.title) AS song_count 
FROM songs s 
JOIN albums A on s.album = a._id 
JOIN artists ar on a.artist = ar._id 
GROUP BY ar.name;


