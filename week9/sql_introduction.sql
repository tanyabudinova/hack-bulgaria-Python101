CREATE TABLE Languages(
  id InTEGER PRIMARY KEY,
  language VARCHAR(20),
  answer VARCHAR(100),
  answered INTEGER,
  guide VARCHAR(100)
);

INSERT INTO Languages
VALUES (1, "Python", "google", 0, "A folder named Python was created. Go there and fight with program.py!"),
(2, "Go", "200 OK", 0, "A folder named Go was created. Go there and try to make Google Go run."),
(3, "Java", "object oriented programming", 0, "object oriented programming"),
(4, "Haskell", "Lambda", 0, "Something pure has landed. Go to Haskell folder and see it!"),
(5, "C#", "NDI=", 0, "Do you see sharp? Go to the C# folder and check out."),
(6, "Ruby", "https://www.ruby-lang.org/bg/", 0, "Ruby, ruby, rubyyy, aaahaaaahaa! (music). Go to Ruby folder!"),
(7, "C++", "header files", 0, "Here be dragons! It's C++ time. Go to the C++ folder."),
(8, "JavaScript", "Douglas Crockford", 0, "NodeJS time. Go to JavaScript folder and Node your way!")


ALTER TABLE Languages
ADD COLUMN rating INTEGER
CONSTRAINT rating_con CHECK (rating >=1 AND rating <=9)


UPDATE Languages
SET rating = 1
Where language = "JavaScript"


UPDATE Languages
SET rating = 2
Where language = "C++"


UPDATE Languages
SET rating = 3
Where language = "Ruby"


UPDATE Languages
SET rating = 4
Where language = "C#"


UPDATE Languages
SET rating = 5
Where language = "Haskell"


UPDATE Languages
SET rating = 6
Where language = "Java"


UPDATE Languages
SET rating = 7
Where language = "Go"


UPDATE Languages
SET rating = 8
Where language = "Python"


UPDATE Languages
SET answered = 1
Where language = "Python" OR language = "Go"


SELECT language
FROM Languages
WHERE answer = "200 OK" OR answer = "Lambda" 

