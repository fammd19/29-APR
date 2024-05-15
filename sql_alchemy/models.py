from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Book(Base):
    __tablename__ = "books"

    id = Column ( Integer(), primary_key=True )
    title = Column ( String(), nullable=False )
    author = Column ( String(), nullable=False )

    def __repr__(self):
        return f"{self.id}: {self.title} written by {self.author}"


class Song(Base):
    __tablename__ = "songs"

    id = Column (Integer(), primary_key=True)
    title = Column (String(), nullable=False)
    artist = Column (String(), nullable=False)

    def __repr__(self):
        return f"{self.id}: {self.title} sung by {self.artist}"


#note - doing actual execution in app.py
