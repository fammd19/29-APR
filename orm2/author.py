from config import CONN, CURSOR
from book import Book

class Author:

    all=[]

    def __init__(self, name):
        self.id=None
        self.name = name

    def __str__(self):
        return f"{self.id} - {self.name}"

    def save(self):

        if not self.id: 
            sql = """
                INSERT INTO authors (name) VALUES
                (?)
            """

            CURSOR.execute(sql, (self.name, ))
            CONN.commit()

            self.id = CURSOR.execute("SELECT last_insert_rowid() FROM authors").fetchone()[0]


    def add_book(self, title, genre):
        if self.id:
            book = Book.create(title, genre, self.id)
            return book

    @classmethod
    def create(cls, name):
        author = cls(name)

        author.save()

        return author

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM authors"

        all_authors = CURSOR.execute(sql).fetchall()

        cls.all = [cls.new_from_db(row) for row in all_authors]
        return cls.all

    @classmethod
    def find_by_id(cls):
        sql = "SELECT * FROM authors WHERE id = ?"

        author = CURSOR.execute(sql, (id,)).fetchone()

        return author

    @classmethod
    def find_by_name(cls):
        sql = "SELECT * FROM authors WHERE name = ?"

        author = CURSOR.execute(sql, (name,)).fetchone()

        return author
    
    @classmethod
    def new_from_db(cls, row):
        author = cls(row[1])
        author.id = row[0]
        return author

    @classmethod
    def create_table(cls):
        sql="""CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
            )
        """
        CURSOR.execute(sql)

    