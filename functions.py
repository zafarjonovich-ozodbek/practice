'''FUNCTIONS
(1) DEFINE vs CALL
(2) Parametr vs Argument
(3) Kewword & default arguments
(4) Scope
'''

print("============ DEFINE vs CALL =============")
# FUNCTION - bu ma'lum bir mantiqni ishka tushirib beruvchi "code block"
# build in function - bu "builtins dunder" tomonidan qurib berilgan functionlar > type(), print() ...
# boshqa tillarda "function" {} bilan belgilanadi, ammo PYTHON "indentations"dan foydalanadi

# DEFINE -  build


# "define" qismi umuman bo'sh bo'lmasligi kerak, xech bo'lmasa "pass" deb yo'zib qo'yish kerak
def greet(a):
    print(f"How do you do, {a}?")  # (1) void function


def greeting(b):
    return f"hi, {b}"  # (2) return function


# CALL - chaqirish
greet("Ron")  # (1)

result = greeting("Nate")  # (2)
print(result)
