from student import Student
Student.create_table()

# student1 = Student("Frae","CS",2)
# student2 = Student("Fi","CS",1)
# student3 = Student("Mack","Maths",4)
# student4 = Student("Rachel","Law",2)

# #student1.save()
# #student2.save()
# #student3.save()
# #print(student3.id)
# student4.save()
# print(student4.id)


# for student in Student.get_all():
#     print(student)


# student_found = Student.find_by_id(2)
# print(student_found)

# student_found_by_name = Student.find_by_name("Mack")
# print(student_found_by_name)

# student.create("John", "Math", 1)

# student_lara = Student.create("Lara", "History", 4)
# student_sara = Student.create("Sara", "History", 4)
# student_cara = Student.create("Cara", "History", 4)
# student_cara.save()

# student_earl = Student.find_or_create_by("Earl", "Maths", 1)
# student_sara=Student.find_or_create_by("Sara", "History", 4)

student_earl = Student.find_or_create_by("Earl", "Maths", 1)
student_earl.degree="English"
student_earl.save()

for student in Student.get_all():
    print(student)