import time
fruits = ["Orange","Banana","Apple","mango","grapes","kiwi"]
food = ("dal","chawal","salad","biryani","Mutton","chicken")

for frt in fruits:
    print("")
    print("Eating fruits are healthy")
    #Nested Loop
    for i in frt:
        print(i)


x = 1
while x <= 1024:
    print("Value of x",x)
    print("Looping")
    x *=2
    time.sleep(1)
