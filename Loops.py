"""
Loops let you repeat block of code multiple times.
There are two main loops in python:
1. while
2 for

A for loop repeat block of code for each item in sequence
"""
from ListType import number

print(number)
for i in number:
    print(i)

#A while loop repeats a block of code as long as certain condition is true
i = 1
while i<=10:
    print(i)
    i=i+1
    