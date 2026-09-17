'''
    OOP 4 Concepts >
    Abstraction - qanday ishlatishni bilamiz ammo qanday ishlayotkanini bilmaymiz
    Encapsulation - kapsulalash, yani tashqaridan uzish, ximoyalash
    Inheritance - meros olish, "parent" va "child" classlarida
    Polymorphism - bixil nomdagi xarxil operatsiyalar '''

# =========== ENCAPSULATION =============
# public(); private(__); protected(_)


class Account():
    # state

    # constructor
    def __init__(self, owner, amount):
        self.__owner = owner
        self.__amount = amount

    # method
    def get_balance(self):
        print(f"the owner {self.__owner} has {self.__amount} usd")

    def deposit(self, amount):
        print("deposit:", amount)
        self.__amount += amount

    def withdraw(self, amount):
        print("withdraw:", amount)
        self.__amount -= amount

    @property
    def holder(self):  # getter - private malumotlarni tashqariga ochish uchun
        return self.__owner

    @holder.setter
    def holder(self, new_owner):
        self.__owner = new_owner


my_account = Account("Shawn", 1000)
my_account.get_balance()

print("=============")
my_account.deposit(3000)
my_account.withdraw(500)
my_account.get_balance()

print("==============")
my_account.amount = 10000000
my_account.get_balance()

print("================")
try:
    result = my_account.__amount
    print("result:", result)
except Exception as err:
    print("No target state fount:",  err)

print(my_account.holder)  # state
my_account.holder = "Ron"
print(my_account.holder)  # state
