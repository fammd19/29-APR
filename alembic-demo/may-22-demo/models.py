from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, backref
from sqlalchemy.ext.associationproxy import association_proxy

Base = declarative_base()

class Company(Base):

    __tablename__ = "companies"

    id = Column (Integer(), primary_key=True)
    name = Column (String())
    industry = Column (String())
    country = Column (String())

    def __repr__(self):
        return f"{self.id} {self.name}({self.country}) {self.industry}"
        

        
#users have a 1 to many relationship with orders (considering an ecommm user)
class User(Base):

    __tablename__ = "users"

    id = Column (Integer(), primary_key=True)
    username = Column (String())
    type = Column (String())

    #User would be the backreference of order
    orders = relationship("Order",backref=backref("user"))

    def __repr__(self):
        return f"{self.id} {self.username} - {self.type}"



class Order(Base):

    __tablename__ = "orders"

    id = Column (Integer(), primary_key=True)
    details = (String())
    total = Column (Integer())

    user_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return f"{self.id} - {self.total}"


#many-to-many

class Book(Base):

    __tablename__ = "books"

    id = Column (Integer(), primary_key=True)
    title = Column (String())

    book_authors = relationship("BookAuthor", back_populates="book")
    authors = association_proxy("book_authors", "author", creator = lambda a: BookAuthor(author=a))

    def __repr__(self):
        return f"{self.id} - {self.title}"


class Author(Base):

    __tablename__ = "authors"

    id = Column (Integer(), primary_key=True)
    name = Column (String())

    book_authors = relationship("BookAuthor", back_populates="author")
    books = association_proxy("book_authors", "book", creator = lambda b: BookAuthor(book=b))

    def __repr__(self):
        return f"{self.id} - {self.name}"


class BookAuthor(Base):

    __tablename__ = "book_authors"

    id = Column (Integer(), primary_key=True)

    book_id = Column (Integer(), ForeignKey("books.id"))
    author_id = Column (Integer(), ForeignKey("authors.id"))

    book = relationship("Book", back_populates="book_authors")
    author = relationship("Author", back_populates="book_authors")

    def __repr__(self):
        return f"{self.id} {self.book_id} {self.author_id}"