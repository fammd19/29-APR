from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Task, Base

from task import ( create_table, save, get_all, find_by_id, update_description )

engine = create_engine("sqlite:///demo3.db")

Session = sessionmaker(bind=engine)
session = Session()

create_table(Base, engine)

task1 = Task(task_title="laundy")
save(session,task1)

task2 = Task(task_title="dishes", task_description="empty dishwasher")
save(session,task2)

tasktoupdate = find_by_id(session,1)

update_description(session,tasktoupdate, "New descrip")

tasks=get_all(session)
print( [task for task in tasks] )



