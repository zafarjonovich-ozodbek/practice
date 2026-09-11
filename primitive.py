# in JAVA & C, variable is a name storage location (ma'lumot manzilining nomlanishi)
# in PYTHON, variable is named reference (manzilning nomlanishi)

print("=========== number ===========")  # or shorthand > print("="*10)

count = 100
count_type = type(count)
print(f"the count: {count}, and type: {count_type}")  # f = superString

result1 = count.bit_count()  # method
result2 = count.numerator  # state
print(result1, result2)


print("============ string =============")
# Usefull Methods: upper(); lower(); title(); find(); replace();

course = "AI Python FullStack"
result = type(course)
print(f"result (1):", {result})

result = course.title()  # method
print(f"result (2):", {result})

result = course.upper()  # method
print(f"result (3):", {result})

result = course.replace("FullStack", "MasterClass")  # method
print(f"result (4):", {result})
# baribir boshlangich qiymati "AI Python FullStack", sabab "reference" boshqa
print(course)

# Agar "reference"ni o'zgartirmoqchi bo'lsak:
course = course.replace("FullStack", "MasterClass")  # method
print(f"result (another reference):", {course})


print("============ boolean =============")
# FUNCTIONS > input(); type(); bool(); int(); str();

y = input("Give the value for y: ")
print("y:", y)

result = y.isnumeric()  # method "isnumeric" - bu "raqammi?" degan method
print(f"the input value is numeric: {result}")


# TRUTHY: True, 100, -100, "mit"
# FALSY: False, 0, None, ""

falsy_test = "" or 0 or False or None
print("falsy_test:", bool(falsy_test))

truthy_test = 'mit'
print("truthy_test:", bool(truthy_test))
