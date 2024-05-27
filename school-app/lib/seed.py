from config import session
from models import Course

COURSES = ["Maths", "Phsyics", "Engineering", "Business", "Economics"]

def create_courses(course_list):
    for c in course_list:
        new_course = Course(title=c)
        session.add(new_course)
        session.commit()

if __name__ == "__main__":
    create_courses(COURSES)
    print(f"Seeding complete")
