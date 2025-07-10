
# A grade class with student_id (int), course_number (string) and grade_letter (string) attributes.
class Grade:

    # Constuctor Method.
    def __init__(self, student_id, course_number, grade_letter):

        self.__student_id = student_id
        self.__course_number = course_number
        self.__grade_letter = grade_letter

    # Adding getters and stters methods for each attribute.

    def set_student_id(self, student_id):

        self.__student_id = student_id

    def get_student_id(self):

        return self.__student_id
    
    def set_course_number(self, course_number):

        self.__course_number = course_number

    def get_course_number(self):

        return self.__course_number
    
    def set_grade_letter(self, grade_letter):

        self.__grade_letter = grade_letter

    def get_grade_letter(self):

        return self.__grade_letter