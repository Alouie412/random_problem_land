#!/usr/bin/python3
# Test

# Importing math. Unfortunately anything with math
# only works with Python 3.8 and up. Python 3.7
# and below will have to use the self defined function instead
import math

new_arr = []
arr = [1, 2, 3, 4, 5]
length = len(arr)
hashTable = {}
copy = []

"""
Self defined function. Used to bypass the issue of 
Python 3.4 not supporting the math.prod function
"""
def mult(arr):
    product = 1
    length = len(arr)
    for i in range(length):
        product *= arr[i]
    return product

"""
The naive solution. Utilizes nested loops, so it is time complex.
Also uses division. Works with Python 3.4
Commented out as to not interfere with other sections of code


for i in range(length):
    product = 1
    for j in range(length):
        product *= arr[j]
    new_arr.append(product/arr[i])
print(new_arr)
"""

"""
The solution that attempts to resolve the time complexity.
Still uses division. Does not run for Python 3.7 and lower
Commented out as to not interfere with other sections of code


for i in range(length):
    product = 1
    # product = math.prod(arr)
    product = mult(arr)
    new_arr.append(product/arr[i])
print(new_arr)
"""

"""
The solution for when division is forbidden.
Unfortunately, it reintroduces time complexity.
Runs on Python 3.4
This block of code also appears to have some logic error


for i in range(length):
    product = 1
    temp = 0
    for temp in range(length):
        if temp == i:
            continue
        else:
            product *= arr[i]
    new_arr.append(product)
print(new_arr)
"""

"""
This solution may be the ideal solution as this has a workaround
for the restriction of using Python 3.4, while still not being
time complex nor does it use division
"""

for i in range(length):
    copy = arr.copy()
    del copy[i]
    # product = math.prod(copy)
    product = mult(copy)
    new_arr.append(product)
print(new_arr)
