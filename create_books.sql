CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    genre TEXT DEFAULT 'Non-Fiction'
);

INSERT INTO books (title, author, genre) VALUES 
("1984", "Stacee Ianitti", "Self-Help"),
("Brave New World", "Vinnie McKane", "Historical Fiction"),
("To Kill a Mockingbird", "Mohandas Lavis", "Thriller"),
("Lord of the Flies", "Latashia Itscowics", "Non-Fiction"),
("The Grapes of Wrath", "Issi Heinz", "Fiction"),
("Brave New World",	"Damara Oldroyde", "Fiction"),
("The Great Gatsby", "Anthiathia Molesworth", "Fantasy"),
("Moby Dick", "Issi Heinz", "Mystery"),
("Pride and Prejudice", "Carita Croy", "Thriller");


