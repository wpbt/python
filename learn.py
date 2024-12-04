"""Importing traceback, math for testing purpose!"""
import math
import traceback
import sys


# List comprehensions
# syntax: [expression for item in iterable if condition]

li1 = [item for item in range(1, 10) if item % 2 == 0]
# same as:
# empty_list = []
# for item in range(1, 10):
#     if item % 2 == 0:
#         empty_list.append(item)

# print(empty_list)
print('list one:')
print(li1)

print('list two')
list2 = [(x, y) for x in range(3) for y in range(3)]
print(list2)

# using loop:
# list2 = []
# for x in range(3):
#     for y in range(3):
#         list2.append((x, y))

# print(list2)

matrix = [[1, 2], [3, 4]]
flat = [num for row in matrix for num in row]
# equivalent loop of above comprehension
# for row in matrix:
#     for num in row:
#         flat.append(num)
print('list three')
print(flat)


try:
    # print(10/0)
    pass
except ZeroDivisionError:
    traceback.print_exc()


# using built-in module
print(math.sqrt(4))  # 2.0
print(math.pow(2, 3))  # 8.0

# looking into path!
print(sys.path)
