# ============ INHERITANCE =============
# meros olish
# faqat public va protected larnigina neros qlib ola oladi

class Animal():
    description = "this class is parent for animals"

    def __init__(self, voice):
        self.message = "animal is alive"
        self.voice = voice

    def make_voice(self):
        print(f"the animal can make voice: {self.voice}")


class Dog(Animal):

    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def protect(self):
        print("Yes, I can protect you")

    def make_voice(self):
        print(f"the {self.name} says {self.sound}")


class Cat(Animal):

    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def play(self):
        pass


class Fish(Animal):

    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def swim(self):
        print("Yes, I can swim")


dog = Dog("Rex", "wow", True)
cat = Cat("Tom", "myeow", True)
fish = Fish("Nemo", "zzz", False)

fish.introduce()
cat.introduce()
dog.introduce()

print(Animal.description)
print(Dog.description)


# ============ POLYMORPHISM =============

dog.make_voice()
cat.make_voice()

print("==============")

# fish -> Fish -> Animal -> object
a = isinstance(fish, Fish)
b = isinstance(fish, Animal)
c = isinstance(Animal, object)
print(a, b, c)

# Fish -> Animal -> object
data1 = issubclass(Fish, Animal)
data2 = issubclass(Animal, object)
print(data1, data2)
