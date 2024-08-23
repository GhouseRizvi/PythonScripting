from optparse import Option
from platform import system

print("Welcome to the calculator")
a=input("Enter first number \n")
b=input("Enter second number \n")
print("""
1. ADDITION
2. SUBTRACTION
3. MULTIPLICATION
4. DIVISION
5. MODULUS
6. EXIT
""")
operation=input("Please Select your operation \n")

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
if operation !=0:
    if operation == 1:
        print(add(a, b))
    if operation == 2:
        print(sub(a, b))
    if operation == 3:
        print(mul(a, b))
    if operation == 4:
        print(div(a, b))
    if operation == 5:
        print(mod(a, b))
    if operation == 6:
        print(SystemExit)
else:
    print("Invalid Selection")