# in JAVA & C, variable is a name storage location (ma'lumot manzilining nomlanishi)
# in PYTHON, variable is named reference (manzilning nomlanishi)

print("====== number =====")  # or shorthand > print("="*10)

count = 100
count_type = type(count)
print(f"the count: {count}, and type: {count_type}")  # f = superString

result1 = count.bit_count()  # method
result2 = count.numerator  # state
print(result1, result2)
