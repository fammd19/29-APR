from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Order

engine = create_engine("sqlite:///demo.db")

Session = sessionmaker(bind=engine)
session = Session()

if __name__ == "__main__":

    orders = session.query(Order).all()

    for order in orders:
        print(order.user)














    # user1 = session.query(User).filter(User.id==1).first()
    # user2 = session.query(User).filter(User.id==2).first()

    # order1 = Order(details="food", total=20, user_id=user1.id)
    # order2 = Order(details="game", total=110, user_id=user1.id)
    # order3 = Order(details="camera", total=200, user_id=user2.id)


    # session.add_all([order1,order2,order3])

    # session.commit()

    # print(f"{user1.username}")
    # print(user1.orders)

    # print(f"{user2.username}")
    # print(user2.orders)

