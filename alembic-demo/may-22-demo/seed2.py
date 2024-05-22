from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Book, Author, BookAuthor
from random import choice

engine = create_engine("sqlite:///demo.db")

Session = sessionmaker(bind=engine)
session = Session()

faker = Faker()

def create_authors(num):
    authors = [ Author(name=faker.name()) for i in range (num) ]
    session.add_all(authors)
    session.commit()
    return authors

def create_books(num):
    books = [ Book(title=faker.sentence()) for i in range (num) ]
    session.add_all(books)
    session.commit()
    return books

def create_book_authors(num):
    book_authors = [ BookAuthor() for i in range (num) ]
    session.add_all(book_authors)
    session.commit()
    return book_authors

def create_relations(authors, books, book_authors):
    for ba in book_authors:
        ba.author = choice(authors)
        ba.book = choice(books)

    session.commit()

def delete_records():
    session.query(Author).delete()
    session.query(Book).delete()
    session.query(BookAuthor).delete()

    session.commit()

if __name__ == "__main__":
    delete_records()
    books = create_books(10)
    authors = create_authors (5)
    book_authors = create_book_authors (20)

    create_relations(authors, books, book_authors)