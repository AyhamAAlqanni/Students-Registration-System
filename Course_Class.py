
class Course:

    def __init__(self, number, name, credits):

        self.__number = number
        self.__name = name
        self.__credits = credits

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