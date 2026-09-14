# Dunder(dubble underscore) "PYTHON"da juda muxum ro'l o'ynaydi, "PYTHON"ning ishlashi quyidagilarga bog'liq:

# --> dunder variable ("__builtins__") - bu "PYTHON"ning sistem variablesi xisoblanadi
# --> dunder methods ("__init__") - bu maxsus method bo'lib, "PYTHON"ning negizi xisoblanadi

# PYTHONning ishlashi "Dunder"ning maxsus
# 'variable' va 'method'lariga asoslanadi

message = "in PYTHON: everything is OBJECT"
print(message)

result = type(message)
print(result)


'''Python BUILTIN tools:
-1) TYPES > int; float; str; list; dict;
-2) FUNCTIONS > print(); len(); input(); type();
-3) CONSTANTS > True; False; None;
'''

# "Dunder"larni ko'rish uchun:
print(dir(__builtins__))
