
# Importing Classes.
from Student_Class import Student
from Course_Class import Course
from Grade_Class import Grade


# A function that reads a file.
def file_read(file_name):

    read_from_file = open(file_name, "r")

    dictionary_holder = dict()

    for line in read_from_file:

        line = line.rstrip("\n").split(",")

        if file_name == "Files/Students.txt": 

            student_object = Student(int(line[0]), line[1], line[2], float(line[3]))

            dictionary_holder[student_object.get_id()] = student_object

        elif file_name == "Files/Courses.txt":

            course_object = Course(line[0], line[1], int(line[2]))

            dictionary_holder[course_object.get_number()] = course_object

        elif file_name == "Files/Grades.txt":

            grade_object = Grade(int(line[0]), line[1], line[2])

            dictionary_holder[grade_object.get_student_id()] = grade_object

    return dictionary_holder


# A function that displays the menu.
def menu_display():

    print("Please Select One of The Following:")
    print("\t(1) Add a New Student.")
    print("\t(2) Add a New Course.")
    print("\t(3) Add a New Grade.")
    print("\t(4) Print a Student's Transcript.")
    print("\t(0) Exit Program.")

    try:

        user_input = int(input("Enter Option: "))

        while user_input < 0 or user_input > 4:

            print("RESULT: Wrong Input!\nEnter a Valid Option.")

            print("Please Select One of The Following:")
            print("\t(1) Add a New Student.")
            print("\t(2) Add a New Course.")
            print("\t(3) Add a New Grade.")
            print("\t(4) Print a Student's Transcript.")
            print("\t(0) Exit Program.")

            user_input = int(input("Enter Option: "))

        return user_input

    except ValueError:

        print("RESULT: Invalid Input!\nEntered a Non Integer Value.")

        menu_display()


# A function that adds a student.
def add_student(students_dictionary):

    try:

        student_id = int(input("Enter Student ID: "))

        if student_id in students_dictionary:

            print("There is Already a Student With That ID!")
            print("RESULT: Student Has Not Been Added.")
        
        else:

            student_name = input("Enter Student Name: ")
            student_mobile = input("Enter Student Mobile: ")

            student_object = Student(student_id, student_name.capitalize(), student_mobile, 0.0)

            return student_object

    except ValueError:

        print("RESULT: Invalid Input!\nEntered a Non Integer Value.")

        return None
    

# A function that adds a course.
def add_course(courses_dictionary):

    try:

        course_number = input("Enter Course Number: ")

        if course_number.upper() in courses_dictionary:

            print("There is Already a Course With That Number!")
            print("RESULT: Course Has Not Been Added.")
        
        else:

            course_name = input("Enter Course Name: ")
            course_credits = int(input("Enter Course Credits: "))

            course_object = Course(course_number.upper(), course_name, course_credits)

            return course_object

    except ValueError:

        print("RESULT: Invalid Input!\nEntered a Non Integer Value.")

        return None
    

# A function that adds a grade.
def add_grade(students_dictionary, courses_dictionary):

    try:

        student_id = int(input("Enter Student ID: "))

        if student_id in students_dictionary:

            print(f"Student Name: {students_dictionary[student_id].get_name()}")

            course_number = input("Enter Course Number: ")

            if course_number.upper() in courses_dictionary:

                print(f"Course Name: {courses_dictionary[course_number.upper()].get_name()}")

                grade_letter = input("Enter Grade Letter: ")

                grade_check_flag = False

                while grade_check_flag != True:

                    if grade_letter.upper() == "A" or grade_letter.upper() == "B" or grade_letter.upper() == "C" or grade_letter.upper() == "D" or grade_letter.upper() == "F":

                        grade_check_flag = True

                    else:

                        print("RESULT: Invalid Input!")
                        grade_letter = input("Enter Grade Letter: ")

                grade_object = Grade(student_id, course_number, grade_letter.upper())

                return grade_object

            else:

                print("There is No Course With This Number!")
                print("RESULT: Grade Has Not Been Added.")

        else:

            print("There is No Student With This ID!")
            print("RESULT: Grade Has Not Been Added.")

    except ValueError:

        print("RESULT: Invalid Input!\nEntered a Non Integer Value.")

        return None


# Main Function
def main():

    students_dictionary = file_read("Files/Students.txt")

    courses_dictionary = file_read("Files/Courses.txt")

    grades_dictionary = file_read("Files/Grades.txt")

    user_input = menu_display()

    print("************************************************************************")

    while user_input != 0:

        if user_input == 1:

            print("OPTION 1: Add Student")

            new_student = add_student(students_dictionary)

            if new_student != None:

                students_dictionary[new_student.get_id()] = new_student

                print("RESULT: Student Has Been Added.")

            print("************************************************************************")

        elif user_input == 2:

            print("OPTION 2: Add Course")

            new_course = add_course(courses_dictionary)

            if new_course != None:

                courses_dictionary[new_course.get_number()] = new_course

                print("RESULT: Course Has Been Added.")

            print("************************************************************************")

        elif user_input == 3:

            print("OPTION 3: Add Grade")

            new_grade = add_grade(students_dictionary, courses_dictionary)

            if new_grade != None:

                grades_dictionary[new_grade.get_student_id()] = new_grade

                print("RESULT: Grade Has Been Added.")

            print("************************************************************************")

        user_input = menu_display()


# Calling Main Function
main()