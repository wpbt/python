# Understanding Python functions

def greet(name=''):
    user = name if name else "visitor"
    print(f"hello {user}")


greet()
greet("bharat")


def multiply(*number):
    total = 1
    for num in number:
        total *= num

    return total


print(multiply(1, 2, 3, 4))
