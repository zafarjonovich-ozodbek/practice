''' OPERATOR and CONDITIONS
    1) Opersators
    2) Conditions
    3) Logical Operators
'''

print("========== OPERATORS ============")
# +, -, <, <=, >, >=, *, ==, is, /, //, %, +=, -=, **

a = 19
b = 5

print(a > b)
print(a < b)
print(a / b)
result = a // b
left = a % b
print(result, left)

a += 100
print(a)

print("b**2", b**2)
print("b**4", b**4)

print("="*20)

c = dict(name="Ron", age=21)
d = dict(name="Ron", age=21)
e = c

print(c == d)  # PYTHONdda faqat qiymatlari solishtiriladi, reference emas
print(id(c), id(d))  # buyerda reference(id)ni tekshirsak boshqa boshqa boladi

print("c is d", c is d)  # (false)"is" orqali referenceni tekshirish mumkun ekan
print("c is e", c is e)  # (true) e va c ning qiymatlariham referenceham birxil


print("============ CONDITINS =============")

x = 5

if x > 50:
    print("Case A")
elif x > 10:
    print("Case B")
else:
    print("Case C")


print("============ LOGICAL OPERATORS =============")

age = 20

person = None
# if age > 18:
#     person = "adult"
# else:
#     person = "minor"

# print(person)


# TERNARY OPERATORS
person = "adult" if age > 18 else "minor"

print(person)

print("+++++++++=========")

is_student = True
is_admin = False
is_guest = True
is_parent = False

if not is_student:  # "not" - agar bo'lmasangiz
    print("Welcome here, do you want to be a student?")
elif is_admin:
    print("Please go to this office!")
# elif is_parent or is_guest: #pastdagi togriroq, sabab "or" bitta true'ni topsayoq operatsiyani tugatadi
elif is_guest or is_parent:  # "or" - yoki, "and" - va
    print("Waiting room is over there!")
else:
    print("Other case")
