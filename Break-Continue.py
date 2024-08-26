#Break statement is used to break out of the loop
#Continue statement is used to skip the statement is looped
#Break
import random
for i in "Devops":
    print(i)
    if i == "o":
        print("Found ",i)
        break
print("Out of the loop")

#Continue

for i in "Development":
    if i == "o":
        print("Skipping ")
        continue
    print(f"Value od i : {i}")
print("Out of the loop")


####################################################
fruits = ["Orange","Banana","Apple","mango","grapes","kiwi"]
random.shuffle(fruits)
print(fruits)
luck = random.choice(fruits)
print(luck)

for frt in fruits:
    print(f"Fruites Are Healthy {frt}")
    if frt == luck:
        print("#######################")
        print(f"{luck} , Fruit Found")
        print("#######################")
        print()
        break
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("Fruit not found!!!")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print()

for frt in fruits:
    print(f"Fruites Are Healthy {frt}")
    if frt == luck:
        print("#######################")
        print(f"{luck} , Fruit Found")
        print("#######################")
        print()
        continue
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("Fruit not found!!!")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print()