SELECT address
FROM STUDIO
WHERE name = "MGM"


SELECT birthdate
FROM MOVIESTAR
WHERE name = "Kim Basinger"


SELECT name
FROM MOVIEEXEC
WHERE networth > 10000000


SELECT name
FROM MOVIESTAR
WHERE gender = 'M' AND address LIKE "%Prefect Rd%"


INSERT INTO MOVIESTAR
VALUES ("Zahari Baharov", "St. Vitosha", "M", "1970-01-01")


DELETE FROM STUDIO
WHERE address LIKE "%5%"


UPDATE MOVIE
SET studioname = "Fox"
WHERE title LIKE "%star%"


SELECT starname
FROM STARSIN S JOIN MOVIESTAR M On S.STARNAME = M.NAME
WHERE S.movietitle = "Terms of Endearment" AND M.gender = 'M'


SELECT starname
FROM STARSIN S JOIN MOVIE M On S.MOVIETITLE = M.TITLE
WHERE M.YEAR = 1995 And M.STUDIONAME = 'MGM'


ALTER TABLE STUDIO
ADD COLUMN president_name VARCHAR(30)


UPDATE STUDIO
SET president_name = 'George Bush'
WHERE name = 'MGM'


UPDATE STUDIO
SET president_name = 'George Leo'
WHERE name = 'USA Entertainm.'


SELECT president_name
FROM STUDIO
WHERE name = 'MGM'