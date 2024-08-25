#Python Operators
#Arithemetic Operator
x=2
y=3
print(f"Addition {x} + {y} :", x+y)
print(f"Subtracting {x} - {y} :", x-y)
print(f"Multiplication {x} * {y} :", x*y)
print(f"Division {x} / {y} :", x/y)
print(f"Modulus {x} % {y} :", x%y)
print(f"Exponent {x} ** {y} :", x**y)

#Comparision Operators it is going to return a boolean value

a = 30
b = 60

print(a<b)
print(a>b)
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)

# Assignment Operators
c = 0
d = 10
c = c+d #c +=d
print(c)

c -=d
print(c)


#logical Operator
a=40
b=60

x=2
y=3

print((a<b)|(x>y))
print((a>b)|(x<y))
print((a>b)|(x>y))
print((a>b)&(x<y))
print((a<b)&(x<y))
print((a<b)&(x>y))
print(not(a<b))
print(not(a>b))

## Membership Operators
devops=('linux','vagrant','bash scripting','aws','jenkins','python')
print('linux' in devops)
print('banana' in devops)
print('banana' not in devops)
print('linux' not in devops)
print('nux' in devops[0])
### Identity operator
a = 12
b = 15

print(a is b) #its li ==
print(a is not b) #its like !=








