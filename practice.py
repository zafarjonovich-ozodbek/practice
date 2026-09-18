class Student():
    # state

    # cons
    def __init__(self, name, age, gpa):
        self.__name = name
        self.__age = age
        self.__gpa = gpa

    # method
    def get_info(self):
        print(
            f"My name is {self.__name} and I am {self.__age} years old. My gpa is {self.__gpa}")

    @property
    def info(self):
        return self.__name

    @info.setter
    def info(self, new_info):
        if new_info == "":
            print("Name cannot be empty")
        else:
            self.__name = new_info


student1 = Student("Ron", 21, 4.4)
student1.get_info()

student1.info = "John"

student1.get_info()
