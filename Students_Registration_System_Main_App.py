
# Importing Classes.
from Student_Class import Student
from Course_Class import Course
from Grade_Class import Grade


# A function that reads a file.
def file_read(file_name):

    read_from_file = open(file_name, "r")

    dictionary_holder = dict()

    grades_list = []

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

            grades_list.append(grade_object)

    read_from_file.close()

    if file_name == "Files/Grades.txt":

        return grades_list
    
    else:

        return dictionary_holder


# A function that writes to a file.
def file_write(file_name, objects):

    write_to_file = open(file_name, "w")

    if file_name == "Files/Grades.txt":

        for grade in objects:

            write_to_file.write(str(grade.get_student_id()) + "," + grade.get_course_number().upper() + "," + grade.get_grade_letter() + "\n")
    
    else:

        for key, value in objects.items():

            if file_name == "Files/Students.txt":

                write_to_file.write(str(key) + "," + value.get_name() + "," + value.get_mobile() + "," + str(value.get_gpa()) + "\n")

            elif file_name == "Files/Courses.txt":

                write_to_file.write(key + "," + value.get_name() + "," + str(value.get_credits()) + "\n")

    write_to_file.close()


# A function that displays the menu.
def menu_display():

    print("Please Select One of The Following:")
    print("\t(1) Add a New Student.")
    print("\t(2) Add a New Course.")
    print("\t(3) Add a New Grade.")
    print("\t(4) Print a Student's Transcript.")
    print("\t(5) Modify Existing Student.")
    print("\t(6) Delete Existing Student.")
    print("\t(0) Exit Program.")

    try:

        user_input = int(input("Enter Option: "))

        while user_input < 0 or user_input > 6:

            print("RESULT: Wrong Input!\nEnter a Valid Option.")

            print("Please Select One of The Following:")
            print("\t(1) Add a New Student.")
            print("\t(2) Add a New Course.")
            print("\t(3) Add a New Grade.")
            print("\t(4) Print a Student's Transcript.")
            print("\t(5) Modify Existing Student.")
            print("\t(6) Delete Existing Student.")
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

            student_mobile = "(" + student_mobile[:3] + ")" + student_mobile[3:6] + "-" + student_mobile[6:]

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
    

# A function that updates a student's GPA.
def gpa_update(students_dictionary, courses_dictionary, grades_list):

    grades_points = {"A" : 4, "B" : 3, "C" : 2, "D" : 1, "F" : 0}

    for student_id in students_dictionary:

        points_credits_sum = 0
        credits_sum = 0

        for course_info in grades_list:

            if course_info.get_student_id() == student_id:

                points_credits_sum += (grades_points[course_info.get_grade_letter()] * courses_dictionary[course_info.get_course_number().upper()].get_credits())

                credits_sum += courses_dictionary[course_info.get_course_number().upper()].get_credits()

        if credits_sum != 0:

            gpa_total = points_credits_sum / credits_sum

            students_dictionary[student_id].set_gpa(format(gpa_total, "0.2f"))


# A function that displays student’s transcript.
def transcript_display(students_dictionary, courses_dictionary, grades_list):

    try:

        student_id = int(input("Enter Student ID: "))

        if student_id in students_dictionary:

            print(f"\nStudent Name: {students_dictionary[student_id].get_name()}")
            print(f"GPA: {students_dictionary[student_id].get_gpa()}")

            print("\nCourses History:")

            for grades in grades_list:

                if grades.get_student_id() == student_id:

                    print(f"Course Name: {grades.get_course_number().upper()} {courses_dictionary[grades.get_course_number().upper()].get_name():<28}" 
                          + f"Grade: {grades.get_grade_letter()}")

        else:

            print("There is No Student With That ID!")
            print("RESULT: Transcript Has Not Been Displayed.")

    except ValueError:

        print("RESULT: Invalid Input!\nEntered a Non Integer Value.")


# A function that modifies an existing student information.
def modify_student(students_dictionary):

    try:

        student_id = int(input("Enter Student ID: "))

        if student_id in students_dictionary:

            print(f"\nStudent Name: {students_dictionary[student_id].get_name()}")

            print("Select One of The Following to Modify:")
            print("\t(1) Modify Name.")
            print("\t(2) Modify Mobile Number.")

            user_selection = int(input("Enter Selection Option: "))

            if user_selection == 1:

                name_modify = input("Enter Modified Name: ")

                students_dictionary[student_id].set_name(name_modify.capitalize())

                print("Name Has Been Modified.")

                return True

            elif user_selection == 2:

                mobile_modify = input("Enter Modified Mobile Number: ")

                mobile_modify = "(" + mobile_modify[:3] + ")" + mobile_modify[3:6] + "-" + mobile_modify[6:]

                students_dictionary[student_id].set_mobile(mobile_modify)

                print("Mobile Number Has Been Modified.")

                return True

            else:

                print("Invalid Input!\nEntered a Number Not in The List.")

                return False

        else:

            print("There is No Student With That ID!")
            print("RESULT: Student Has Not Been Modified.")

            return False

    except ValueError:

        print("RESULT: Invalid Input!\nEntered a Non Integer Value.")

        return False
    

# A function that deletes a student records.
def delete_student(students_dictionary, grades_list):

    try:

        student_id = int(input("Enter Student ID: "))

        if student_id in students_dictionary:

            print(f"\nStudent Name: {students_dictionary[student_id].get_name()}")

            delete_confirmation = input("Delte Student? (Y) or (N): ")

            if delete_confirmation.upper() == "Y":

                del students_dictionary[student_id]

                for grade in range(len(grades_list)):

                    if grades_list[grade].get_student_id() == student_id:

                        del grades_list[grade]

                return True

            else:

                print("RESULT: Student Has Not Been Deleted.")

                return False
        
        else:

            print("There is No Student With That ID!")
            print("RESULT: Student Has Not Been Deleted.")

            return False

    except ValueError:

        print("RESULT: Invalid Input!\nEntered a Non Integer Value.")

        return False


# Main Function
def main():

    students_dictionary = file_read("Files/Students.txt")

    courses_dictionary = file_read("Files/Courses.txt")

    grades_list = file_read("Files/Grades.txt")

    user_input = menu_display()

    print("************************************************************************")

    while user_input != 0:

        if user_input == 1:

            print("OPTION 1: Add Student")

            new_student = add_student(students_dictionary)

            if new_student != None:

                students_dictionary[new_student.get_id()] = new_student

                file_write("Files/Students.txt", students_dictionary)

                print("RESULT: Student Has Been Added.")

            print("************************************************************************")

        elif user_input == 2:

            print("OPTION 2: Add Course")

            new_course = add_course(courses_dictionary)

            if new_course != None:

                courses_dictionary[new_course.get_number()] = new_course

                file_write("Files/Courses.txt", courses_dictionary)

                print("RESULT: Course Has Been Added.")

            print("************************************************************************")

        elif user_input == 3:

            print("OPTION 3: Add Grade")

            new_grade = add_grade(students_dictionary, courses_dictionary)

            if new_grade != None:

                grades_list.append(new_grade)

                file_write("Files/Grades.txt", grades_list)

                print("RESULT: Grade Has Been Added.")

                gpa_update(students_dictionary, courses_dictionary, grades_list)

                file_write("Files/Students.txt", students_dictionary)

            print("************************************************************************")

        elif user_input == 4:

            print("OPTION 4: Student's Transcript")

            transcript_display(students_dictionary, courses_dictionary, grades_list)

            print("************************************************************************")

        elif user_input == 5:

            print("OPTION 5: Modify Student's Information")

            result_flag = modify_student(students_dictionary)

            if result_flag == True:

                file_write("Files/Students.txt", students_dictionary)

                print("RESULT: Student Has Been Modified.")

            print("************************************************************************")

        elif user_input == 6:

            print("OPTION 6: Delete Student")

            result_flag = delete_student(students_dictionary, grades_list)

            if result_flag == True:

                file_write("Files/Students.txt", students_dictionary)

                file_write("Files/Grades.txt", grades_list)

                print("RESULT: Student Has Been Deleted.")

            print("************************************************************************")

        user_input = menu_display()

    print("OPTION 0: Exited Program.")


# Calling Main Function
main()