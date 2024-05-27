from config import session
from models import Student, Course, Enrolment
from colorama import Back, Fore, Style
import os

#can put the clear command in another file for cleanliness
def clear(): 
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")



def main_menu():
    print("*"*40)
    print("Menu options:")
    print("*"*40)

    print(Back.GREEN + "add" + Style.RESET_ALL +"\tAdd a new student to the app")
    print(Back.GREEN + "students" + Style.RESET_ALL +"\tDisplay all students")
    print(Back.GREEN + "courses" + Style.RESET_ALL +"\tEnrole a student to a course")
    print(Back.RED + "quit/exit" + Style.RESET_ALL +"\tExit this programme")

    print("="*40) 


def add_student():
    loop = True

    while loop:
        clear()

        print("-"*30)
        print("Add student")
        print("-"*30)

        print("\nPlease enter the student\'s name")
        name = input()

        print("\nPlease enter the student\'s degree")
        degree = input()

        new_student = Student(name=name, degree=degree)
        session.add(new_student)
        session.commit()

        print(Fore.GREEN + f"\n{new_student.name}" + Style.RESET_ALL + " has been added")

        while True:
            print("\nDo you want to add another student? Y or N")
            choice = input()

            if choice.lower() == "y":
                break
            elif choice.lower() == "n":
                loop=False
                break
            else:
                print (Back.RED + "Invalid choice. Please select Y or N" + Style.RESET_ALL)
        
def display_students():
    loop = True

    while loop:
        clear()

        print("-"*30)
        print("Display students")
        print("-"*30)

        students = session.query(Student).all()

        # print(f"ID\tNAME\t\tDEGREE")
        for student in students:
            print(student)

        student_loop = True

        while student_loop:
            print("\nEnter the students ID to view their enrolment:")
            student_id = int (input())

            student = session.query(Student).filter(Student.id==student_id).first()
            
            if student:
                if (len(student.courses))>0:
                    print(f"{student.name}'s enrolled courses:")
                    
                    count = 1
                    for course in student.courses:
                        print(f"{count}. {course.title}")
                        count = count+1

                else:
                    print(f"{student.name} is not enrolled in any courses")

            else:
                print(Fore.RED + f"No student found with the id {student_id}"+ Style.RESET_ALL)

            while True:
                print("\nDo you want to view another student? Y or N")
                choice = input()

                if choice.lower() == "y":
                    break
                elif choice.lower() == "n":
                    student_loop=False
                    loop=False
                    break
                else:
                    print (Back.RED + "Invalid choice. Please select Y or N" + Style.RESET_ALL)


def enrol_student():
    clear()

    print("-"*30)
    print("Enrol a student")
    print("-"*30)

    courses = session.query(Course).all()

    for c in courses:
        print (c)

    print("\nPlease enter the course ID you'd like to enrol the student into:")
    course_id = int(input())

    course = session.query(Course).filter(Course.id == course_id).first()

    if course:
        print("\nPlease enter the student ID to enrol")
        student_id = int(input())

        new_enrolment = Enrolment (course_id = course.id, student_id = student_id)
        session.add(new_enrolment)
        session.commit()

        print(f"{new_enrolment}")

    else:
        print("Invalid input")

def start():
    #app_loop is a control value for the looping
    app_loop = True

    while app_loop:
        main_menu()

        #Manages if user selects an invalid option.
        option_loop=True

        while option_loop:
            print("Please select an option")
            choice = input()
            
            if choice.lower() == "add":
                option_loop = False
                add_student()
            elif choice.lower() == "students":
                option_loop = False
                display_students()
            elif choice.lower() == "courses":
                option_loop = False
                enrol_student()
            elif choice.lower() == "quit" or choice.lower() == "exit":
                option_loop = False
                app_loop = False
            else:
                print (Back.RED + "Invalid choice. Please select a valid option" + Style.RESET_ALL)

    print(Back.RED + "Thank you for using the school management app. Goodbye." + Style.RESET_ALL)


def greet():
    #will run greet at the start so can have clear in the greet function
    clear()
    print(Back.YELLOW+"Welcome to the school management app!"+ Style.RESET_ALL)

if __name__ == "__main__":
    
    greet()
    start()

