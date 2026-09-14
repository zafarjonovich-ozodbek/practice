print("============= Iterable objects & RANGE =============")
# ITERABLE OBJ - talrorlanish xususiyatiga ega bo'lgan objectlar
# Iterable objects > string dict tuple randge list map filter

range_obj = range(3)  # [0, 3)
print("range_obj:", range_obj)


for ele in range_obj:
    print(f"the element: {ele}")  # 0, 1, 2
for letter in "MIT":
    print(f" the letter: {letter}")  # M I T


print("============ DICTIONARY ================")
# DICTIONARY bizga o'zimiz "object" yaratish uchun kerak bo'ladi
# Dictionary is JSON object
person = {"name": "Justin", "age": 25, "single": True}
person_obj = dict(name="Justin", age=25, single=True)
print(f"the person: {person}")
print(f"the person_obj: {person_obj}")


# METHOD: get()
# name = person_obj["name"]

# hobby = person_obj["hobby"]  # bu "Error", sabab "hobby" degan "state" yo'q
name = person_obj.get("name")
hobby = person_obj.get("hobby")  # "hobby" uchun "Error"emas "None"
balance = person_obj.get("balance", 0)  # "None" o'rniga qiymat kiritdik
print(f"the name: {name}, hobby: {hobby} and balance: {balance}")

del person_obj["single"]  # "key va value"ni o'chirish uchun
for key in person_obj:
    print(
        f"the key: {key} > value {person_obj[key]}")  # or {person_obj.get(key)
