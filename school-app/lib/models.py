from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.ext.associationproxy import association_proxy

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"
    
    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    degree = Column(String())

    enrolments = relationship("Enrolment", back_populates="student")
    courses = association_proxy("enrolments", "course", creator=lambda c: Enrolment(course=c))

    def __repr__(self):
        return f"{self.id}: {self.name} - {self.degree}"

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer(), primary_key=True)
    title = Column(String(), nullable=False)

    enrolments = relationship("Enrolment", back_populates="course")
    students = association_proxy("enrolments", "student", creator=lambda s: Enrolment(student=s))

    def __repr__(self):
        return f"{self.id}: {self.title}"


class Enrolment(Base):
    __tablename__ = "enrolments"

    id = Column(Integer(), primary_key=True)
    course_id = Column (Integer(), ForeignKey("courses.id"))
    student_id = Column (Integer(), ForeignKey("students.id"))

    course = relationship("Course", back_populates="enrolments")
    student = relationship("Student", back_populates="enrolments")

    def __repr__(self):
        return f"{self.student.name} is enrolled in {self.course.title}"