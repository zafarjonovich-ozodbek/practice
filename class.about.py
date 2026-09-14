''' CLASS
    1) What is Class?
    2) Ordinary vs static Properties
    3) Special methods
'''

print("========== What is Class? ===========")
# CLASS - bu "object" yasovchi shablon, bir-biriga yaqin bo'lgan "Object"larni yasovchi bir shablon qurib olamiz, va bu shablon orqali istalgancha "Object" yaratsak bo'ladi
# STRUCTURE > State; Constructor; Methods


class Person():
    # state
    message = "static property"

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method
    def introduce(self):
        print(f"{self.name} says: How do you do!")

    def say_age(self):
        print(f"{self.name} says I am {self.age}")

    @classmethod  # Static method yasash
    def explain(cls):
        print("static method property executed!")


# object yasash
person1 = Person("Justin", 25)
person2 = Person("Martin", 35)
person3 = Person("John", 22)

# ORDINARY(oddiy) state
# ordinary state - bu "Object" bilan birga yashovchi "state" xisoblanadi, ya'ni "Object" orqali chaqiriladi
print("person1.name:", person1.name)

# ORDINARY(oddiy) method
# ordinary method -  bu "Object" bilan birga yashovchi "method" xisoblanadi, ya'ni "Object" orqali chaqiriladi
person1.introduce()
person3.say_age()


# STATIC state
# static state - bu "Class" bilan yashovchi "state" xisoblanadi,  ya'ni "Class"nomi orqali chaqiriladi
new_message = Person.message
print(new_message)

# STATIC method
# static method -  bu "Class" bilan yashovchi "method" xisoblanadi,  ya'ni "Class"nomi orqali chaqiriladi
Person.explain()


print("========== Special/Magic methods ===========")
# "Python"ning eng kop ishlatiladigan "special/magic" methodlairi:
# __init__, __new__, __str__, __call__, __getitem__, __eq__, __len__ ....
# Browser'dan "python magic methods"deb qidirsa chiqadi


class Car():
    # state
    description = "This class makes cars"

    # constructor
    # def __new__(cls, *args):      #bu  "__new__ method" ishlatilmasada ko'rnmas xolda shuyerda bo'ladi
    #     print("*__new__*")
    #     return super().__new__(cls)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method
    def start_engine(self):
        print(f"the {self.name} started engine!")

    def stop_engine(self):
        print(f"the {self.name} stopped engine!")

    def __str__(self):
        return f"car.name: {self.name} was produced in {self.age} year!"

    def __call__(self):
        print("Object called as function")
        return True


my_car = Car("Ferrari", 2026)
my_car.start_engine()
my_car.stop_engine()


print("==========")
your_car = Car("BMW", 2026)
print(your_car)
response = your_car()
print(response)
