"""
This Script will implement our knowledge on conditions
and different datatypes
"""
print("This IT organization has various skill sets")
print("Find out your match")
print("Enter Capitalized Values: ")

devops = ['linux','vagrant','bash scripting','aws','jenkins','python']
development = ("Nodejs", "Angularjs", "Java", ".net")
cntr_emp1 = {"Name":"Santa","Skill":"Blockchain","Code":1024}
cntr_emp2 = {"Name":"Rocky","Skill":"AI","Code":1218}

user_skill = input("Enter your desired skill: \n")
#print(user_skill)
#CHeck in the Database if we've the skill

if user_skill in devops:
    print(f"We've {user_skill} in devops Team.")
elif user_skill in development:
    print(f"We've {user_skill} in Development Team")
elif (user_skill in cntr_emp1.values()) or (user_skill in cntr_emp2.values()):
    print(f"We have contract employee with {user_skill} skill.")
else:
    print("Skill not found")


