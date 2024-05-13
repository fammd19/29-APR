from config import CONN, CURSOR

class Book:

    all=[]

    def __init__(self, title, genre, author_id):
        self.id=None
        self.title = title
        self.genre = genre
        self.author_id = author_id

    def __str__(self):
        return f"{self.id} - {self.name}"

    def save(self):

        if not self.id: 
            sql = """
                INSERT INTO books (title, genre, author_id) VALUES
                (?,?,?)
            """

            CURSOR.execute(sql, (self.title, self.genre, self.author_id))
            CONN.commit()

            self.id = CURSOR.execute("SELECT last_insert_rowid() FROM books").fetchone()[0]

    def author_name(self):
        sql = """
            SELECT name FROM authors JOIN books ON 
            author_id = authors.id
            WHERE books.id = ?
        """

        author_name = CURSOR.execute(sql, (self.id,)).fetchone()[0]

        return author_name

    @classmethod
    def find_by_author(cls, name):
        sql = """
            SELECT books.id, title, genre, author_id FROM authors JOIN books ON 
            author_id = authors.id
            WHERE name = ?
        """

        books_by_name = CURSOR.execute(sql, (name,)).fetchall()

        return [cls.new_from_db(row) for row in books_by_name]


    @classmethod
    def create(cls, title, genre, author_id):
        book = cls(title, genre, author_id)

        book.save()

        return book

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM books"

        all_books = CURSOR.execute(sql).fetchall()

        cls.all = [cls.new_from_db(row) for row in all_books]
        return cls.all

    @classmethod
    def find_by_id(cls):
        sql = "SELECT * FROM books WHERE id = ?"

        book = CURSOR.execute(sql, (id,)).fetchone()

        return book

    @classmethod
    def find_by_title(cls):
        sql = "SELECT * FROM books WHERE title = ?"

        books = CURSOR.execute(sql, (title,)).fetchall()

        return books

    @classmethod
    def find_by_genre(cls):
        sql = "SELECT * FROM books WHERE genre = ?"

        books = CURSOR.execute(sql, (genre,)).fetchall()

        return books

    @classmethod
    def find_by_author_id(cls):
        sql = "SELECT * FROM books WHERE author_id = ?"

        books = CURSOR.execute(sql, (author_id,)).fetchall()

        return books
    
    @classmethod
    def new_from_db(cls, row):
        book = cls(row[1], row[2], row[3])
        book.id = row[0]
        return book

    @classmethod
    def create_table(cls):
        sql="""CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            genre TEXT NOT NULL,
            author_id INTEGER NOT NULL REFERENCES authors(id)
            )
        """
        CURSOR.execute(sql)

    