'''LOOP operators:
   1) for
   2) reak/else
   3) while
'''

print("============ FOR operators =============")
# Iterable objects > string dict tuple randge list map filter
text = "MIT"
numbs = [10, 7, 3, 6]
car_obj = dict(brand="Porsche", year=2026)
range_obj = range(5)

for letter in text:
    print(f"the letter: {letter}")

print("---------")
for number in numbs:
    print(f"the number: {number}")

print("---------")
for key in car_obj:
    print(f"the key: {key} => value: {car_obj.get(key)}")

print("---------")
for x in range_obj:
    print(f"the x: {x}")


print("============ BREAK/ELSE =============")
for x in range(1, 21, 4):
    print(f"the x: {x}")
    if x > 10:
        print("Reached break")
        break
else:
    print("Executed successfully")

print("+++++++")


print("============ WHILE operators =============")
i = 0
while i < 10:
    print(i)
    i += 1

print("============")
numb = 40
while numb > 0:
    numb -= 5
    print(f"the number {numb}")


print("============")
count = 0
while True:
    count += 1
    x = int(input("Find number "))

    if x == 41:
        print(f"You found number in {count} steps")
        break
    else:
        print("Wrong, please find again!")
