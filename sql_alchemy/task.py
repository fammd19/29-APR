from models import Task

def create_table(base, engine):
    base.metadata.create_all(engine)

def save(session,task):
    #session serves as a middleware. Add is a method of session
    #have to ensure task is an instance of Task. Note, won't get an error
    session.add(task)
    session.commit()

def get_all(session):
    return session.query(Task).all()

def find_by_id(session, id):
    return session.query(Task).filter(Task.id==id).first()

def update_description(session,task,new_descrip):
    task.task_description = new_descrip
    session.commit()
