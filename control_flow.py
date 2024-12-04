# Basic of control flow in Python
# if, if...else, if...elif...else
# ternary: result = "True Value" if condition else "Default Value"


xyz = 123
if xyz > 2:
    print("It's greater than 2")
elif xyz > 200:
    print("It's greater than 200")
else:
    print("It's less")

# ternary operator
is_admin = True
user = "Logged In User" if is_admin else "Site Visitor"
print(user)

str_value = "Programming is fun"
for i in str_value:
    if not i.strip():
        continue
    print(i)
