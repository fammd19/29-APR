from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, create_engine, and_, or_

#Instantiates a base object
Base = declarative_base()

class User(Base):
    #rule of thumb, pluralise the model name
    __tablename__ = "users"

    #creates an instance from the column class
    id = Column( Integer(), primary_key=True)
    #nullable as false is like not null
    name = Column ( String(), nullable=False)
    #location has no constraints beyond being a string
    location = Column ( String() )

    def __repr__(self):
        return f"{self.id}: {self.name}, {self.location}"

#Have to declar the mapping to ensure gets created into the database table
#Checks running an executable programme i.e. if a moduel or a simple script, will not return true
if __name__ == "__main__":
    #engine serves as the connection to the database
    engine = create_engine("sqlite:///demo.db")
    #using base object, refer to its metadata property and call create_all
    Base.metadata.create_all(engine)

    #create a class object and bind it to the databse connection
    Session = sessionmaker(bind=engine)
    #create an instance from this class
    session = Session()

    # new_user = User(name="fi", location="sydney")

    # session.add(new_user)
    # session.commit()

    # user1 = User(name="frae", location="manilla")
    # user2 = User(name="sara", location="melbourne")

    # session.add_all( [user1, user2] )
    # session.commit()

    # #to query the database
    # users = session.query(User)

    # print([user for user in users])

    # new_user_1 = User(name="mack", location="sydney")

    # session.add(new_user_1)
    # session.commit()

    # non_sydney_users = session.query(User).filter(User.location != "sydney")

    # print( [user for user in non_sydney_users] )

    # user4 = User(name="cherly", location="sydney")
    # user5 = User(name="emily", location="melbourne")
    # user6 = User(name="miguel", location="adelaide")

    # session.add_all( [user4, user5, user6] )
    # session.commit()

    # #get all users whos names start with F
    # f_names = session.query(User).filter(User.name.like("f%"))

    # print( [name for name in f_names] )

    # # get all users who are in malbourne or manilla
    # f_names = session.query(User).filter(or_(User.location == "melbourne", User.location == "manilla"))

    # print( [name for name in f_names] )

    # frae = session.query(User).get(2)
    # print(frae)

    # frae.location = "tokyo"
    # session.commit()

    # print(frae)

    # # Delete
    # frae = session.query(User).get(2)
    # print(frae)

    # session.delete(frae)
    # session.commit()

    # print(frae)

    # users = session.query(User).filter(User.id >= 7)

    # print( [user for user in users] )

    # session.delete(frae)
    # session.commit()