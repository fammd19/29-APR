from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column( Integer(), primary_key=True )
    full_name = Column ( String(), nullable=False )
    age = Column (Integer())

    def __repr__(self):
        return f"{self.id}: {self.name}"