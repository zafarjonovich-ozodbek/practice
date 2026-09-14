''' CLASS
    1) What is Class?
    2) Ordinary vs static Properties
    3) Special methods
'''

print("========== What is Class? ===========")


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

    @classmethod
    def explain(cls):
        print("static method property executed!")


# object yasash
person1 = Person("Justin", 25)
person2 = Person("Martin", 35)
person3 = Person("John", 22)

# ordinary(oddiy) state
print("person1.name:", person1.name)

# ordinary(oddiy) method
person1.introduce()
person3.say_age()


# static state
new_message = Person.message
print(new_message)

# static method
Person.explain()
