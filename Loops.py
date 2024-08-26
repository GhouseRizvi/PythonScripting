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

planet = "Earth"
for i in planet:
    print(f"Value if i now {i}")
print("Rest of the Code")

vaccine = ("Moderna","pfizer","Sputnik","Covaxin","Astrazenica")

for vac in vaccine:
    print(f"Available Vaccine for COVID19 is {vac}")

x = 0
while x <= 10:
    print(f"Value of x:{x}")
    x +=1
print("Rest of the Code")

