from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User

if __name__ == "__main__":
    engine = create_engine("sqlite:///data.db")

    Session = sessionmaker(bind=engine)
    session = Session()

    faker = Faker()

    for x in range(20):
        new_user = User (full_name=faker.name(), age=18)

        session.add(new_user)
        session.commit()
