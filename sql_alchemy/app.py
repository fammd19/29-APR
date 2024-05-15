from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from models import Base, Book, Song


if __name__ == "__main__":

    engine = create_engine("sqlite:///demo2.db")
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    book1 = Book(title="abc", author="John")
    book2 = Book(title="def", author="Mary")
    book3 = Book(title="ghi", author="Doris")

    song1 = Song(title="LaLaLa", artist="Albert")
    song2 = Song(title="ChaChaCha", artist="Victoria")

    session.add_all( [book1, book2, book3, song1, song2])
    session.commit()