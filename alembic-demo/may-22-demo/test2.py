from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Book, Author, BookAuthor

engine = create_engine("sqlite:///demo.db")

Session = sessionmaker(bind=engine)
session = Session()

if __name__ == "__main__":

    # authors = session.query(Author).all()

    # for author in authors:
    #     print(author.id)

    # books = session.query(Book).all()

    # for book in books:
    #     print(book.id)

    def filter_authors_by_name(name):
        return session.query(Author).filter(Author.name==name).first()

    filtered_authors = filter_authors_by_name("Shannon Jones")
    print(filtered_authors)

    def filter_books_by_author(name):
        return session.query(Book).filter(Author.name==name).all()

    filtered_books = filter_books_by_author("Shannon Jones")
    for book in filtered_books:
        print(book.title)