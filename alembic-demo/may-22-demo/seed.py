from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Company

if __name__ == "__main__":
    engine = create_engine("sqlite:///demo.db")

    Session = sessionmaker(bind=engine)
    session = Session()

    faker = Faker()

    for i in range(20):
        user = User(username=faker.user_name(), type=faker.job())
        session.add(user)
        session.commit()

    for i in range(4):
        company = Company(name=faker.company(), country=faker.country())
        session.add(company)
        session.commit()

    print("Seeding successful")