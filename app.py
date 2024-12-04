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


n = "visitor"
print("Hello " + n)


def square(x): return x + 2


print(square(4))

print('swapping variables:  ')
ax = 10
by = 11
print(f"before swap: x = {ax}, y = {by}")
ax, by = (by, ax)
print(f"after swap: x = {ax}, y = {by}")

print('variable args')


def greet(name):
    print("hello, " + name)


greet('bharat')


def some_fxn(*args):
    print(f"Type of args: {type(args)}")
    print(args)


some_fxn(12, 14, "asdf")


def var_args(**args):
    print(f"Type of args: {type(args)}")
    print(args)


var_args(name='bharat', age=40, sex='Male', height='4ft.', weight=71.5)


def decorator(func):
    def wrapper():
        print("before function call")
        func()
        print("after function call")
    return wrapper


@decorator
def say_hello():
    print('hello!!')


say_hello()


def annotation_fxn(name: str, age: int) -> str:
    """this function also defines the type of argument it expects. They aren't enforced though"""
    return f"name = {name}, age = {age}"


print(annotation_fxn(name=20, age='50'))

print('list in action')
l1 = [1, 32, 12, 34, 40]
print(l1)

print('set in action')
s1 = {1, 42, 3, 2, 'a', 'h'}
print(s1)


print('tuple in action')
t1 = (1, 42, 3, 2, 42, 'a', 'b')
print(t1)


async def fxn_name():
    """I have no idea what this is!!!"""
    print('bruhh')


fxn_name()
