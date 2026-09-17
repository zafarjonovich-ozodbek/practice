''' OBJECTS

1) What is object - ma'lum bir maqsadda ishlatiladigan va o'zining birqancha maxsus "Method" va "State"lariga ega bo'lgan "DataType"
2) Iterable obj & RANGE
3) DICTIONARY
4) Error handling system 
'''

import array
import math  # Pythonda "package" yuklash
# "math" package ichidagi faqat "methodn yoki "state"ni yuklaydi
from math import ceil, asin
print("============ What is OBJECT ==============")
# Object - method va statelariga ega bo'lgan property
# In Python everything is Object

print(type("Hello World!"))
print(type(100))
print(type(True))
print(type(array))
print(type(math))


# PARADIGMA > Functional Programming & OOP
# OOP 4 Concepts > Abstraction | Encapsulation | Inheritance | Polymorphism
result1 = math.ceil(97.6)  # CALL
print(result1)
# "method"ni oziniham "CALL" qilishimizham mumkun, sabab "method"ni ozini "import" qilib oldik

result2 = ceil(99.2)
print(result2)


print("============ Error handling system  ==============")
car = dict(name="Tayota", year=2026, electric=True)

# Agar bizga "Error" yoki "None" emas, xato payiti o'zimiz xoxlagan xato qiymat chiqishi uchun "Try & Except" blogi kerak bo'ladi
try:
    print("passed here")  # shunchaki shuyerdan o'tkanligi
    result = car["speed"]
    print("result:", result)
except KeyError as err:  # xato payiti qanday javob kelishi
    print("No speed state property found:", err)
else:  # to'g'ri payiti
    print("Executed successfully without errors")
finally:  # xato/togri bolsaham oxirida chiqadi, buni yozmasakham bo'ladi
    print("Final closing logic")
