
# A course class with number (string), name (string) and credits (int) attributes.
class Course:

    # Constuctor Method.
    def __init__(self, number, name, credits):

        self.__number = number
        self.__name = name
        self.__credits = credits

    # Adding getters and stters methods for each attribute.

    def set_number(self, course_number):

        self.__number = course_number

    def get_number(self):

        return self.__number
    
    def set_name(self, course_name):

        self.__name = course_name

    def get_name(self):

        return self.__name
    
    def set_credits(self, course_credits):

        self.__credits = course_credits

    def get_credits(self):

        return self.__credits