# Understanding Python functions

def greet(name=''):
    user = name if name else "visitor"
    print(f"hello {user}")


greet()
greet("bharat")

# variable arguments


def multiply(*number):
    total = 1
    for num in number:
        total *= num

    return total


print(multiply(1, 2, 3, 4))

# keyword argument


def increment(number, by):
    return number + by


print(increment(23, by=22))

# variable keyword arguments


def save_user(**user):
    print(user)


save_user(id=1, name="John", role="Admin")
