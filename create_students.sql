CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    first TEXT NOT NULL,
    last TEXT NOT NULL,
    degree TEXT NOT NULL
);

INSERT INTO students (first, last, degree) VALUES 
("Fi", "M", "CS"),
("Mack", "F", "Maths");