# Understanding Python functions

def greet(name=''):
    user = name if name else "visitor"
    print(f"hello {user}")


greet()
greet("bharat")
