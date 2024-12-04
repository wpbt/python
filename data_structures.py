# Data Structures in Python: Lists, Sets, Tuples, Dictionaries

alphabets = ['a', 'b', 'c', 'd']
coordinates = [[1, 2], [2, 3], [4, 5]]
numbers = [1, 2, 3, 4]

items = list(range(1, 10))
alpha_nums = alphabets + numbers

# print(alpha_nums)
# print(items)

# unpacking (or destructuring) list
one, two, three, four = numbers
# print(one) # prints 1

x, y, *rest = items
# print(x, y, rest)  # 1, 2, [3, ..., 9]

for index, item in enumerate(items):
    print(f"Index: {index} Value: {item}")

# enumerate(items) returns a tuple: (index, value).
# the tuple is then extracted into index (first) and value (second) in the for loop.

# List operations:
# .append(),
# .insert(),
# .pop(),
# .remove(),
# del list_name[index]
# .clear()


products = [
    ("Product One", 21),
    ("Product ABC", 18),
    ("Product XYZ", 91)
]


def sort_my_prod(item):
    return item[1]


# sort method uses lambda as key arg!
# Lambda: lambda parameters:expression
products.sort(key=lambda item: item[1], reverse=True)
# print(products)

cats = [
    ("cat one", 21),
    ("cat two", 29),
    ("cat three", 41)
]
# without map()
# ids = []
# for cat in cats:
#     ids.append(cat[1])

# print(ids)

# with map()
x = list(map(lambda item: item[1], cats))
# print(x)

y = list(filter(lambda item: item[1] > 22, cats))
print(y)


l1 = [1, 3, 5]
l2 = [7, 9, 11]
L3 = 'abc'

res = list(zip(l1, l2, L3))
print(res)

# Tuples, Set, Dictionaries
tuple1 = (1, 2, 4)
set1 = {1, 2, 4}
dict1 = {"x": 1, "y": 2}
dict2 = dict(x=1, y=2)
