
class Student:

    def __init__(self, id, name, mobile):

        self.__id = id
        self.__name = name
        self.__mobile = mobile
        self.__gpa = 0.0

    def set_id(self, id):

        self.__id = id

    def get_id(self):

        return self.__id
    
    def set_name(self, name):

        self.__name = name

    def get_name(self):

        return self.__name
    
    def set_mobile(self, mobile):

        self.__mobile = mobile

    def get_mobile(self):

        return self.__mobile