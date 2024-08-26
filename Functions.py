def add(a,b):
    return a + b
print(add(2,3))

def sum(a,b):
    total= a + b
    print(total)
sum(10,20)

def summ(arg):
    x=0
    for i in arg:
        x = x + i
    return x
out = summ([1,2,3,4,5])
print(out)

#default arguments
def greetings(msg='Morning'):
    print(f"Good {msg}")
    print("Welcome to function")

greetings("Morning")
greetings()
greetings('Evening')

def fruits(name,nutrition_value):
    print(f"Fruit {name} is having high nutrient {nutrition_value} value")
    if (nutrition_value >= 50) and (nutrition_value <= 70):
        print(f"{name} is very healthy")
    elif (nutrition_value >= 90) & (nutrition_value <= 70):
        print(f"{name} has a High nutrient value ")
    else:
        print(f"{name} is unhealthy")

#fruits("Apple",90)
#fruits('Banana',45)
fruits('Jamun',50)

#Keyword argument
