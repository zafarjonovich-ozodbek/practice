# Dunder(dubble underscore) --> dunder variable ("__builtins__"), dunder methos ("__init__")
# "__builtins__ dunder" - bu "PYTHON"ning sistem variablesi xisoblanadi
# "__init__ dunder" - bu maxsus method bo'lib, "PYTHON"ning negizi xisoblanadi

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
