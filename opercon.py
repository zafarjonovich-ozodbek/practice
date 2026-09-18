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
