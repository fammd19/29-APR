from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Book, Author, BookAuthor

engine = create_engine("sqlite:///demo.db")

Session = sessionmaker(bind=engine)
session = Session()

if __name__ == "__main__":

