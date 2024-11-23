# Hello Wordl Program!
print("hello developer!")

# Declaring variables
# Primitive Types: number, boolean, string
firstName = 'Bharat'
lastName = 'Thapa'
age = 78
weight = 70.5
isAgoodDeveloper = False
print(F"{firstName} {lastName}")  # Or f""

# Falsy values
print(bool(""))
print(bool(0))
print(bool(None))

# Comparison operators
print(1 > 2)
print(2 > 1)

xyz = 123
if xyz > 2:
    print("It's greater than 2")
elif xyz > 200:
    print("It's greater than 200")
else:
    print("It's less")

# ternary operator
result = "Greater" if xyz > 100 else "Less"
print(result)
