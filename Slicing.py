# Slicing is a for of slicing the part of data to get hold of the desired data
planet1 = "Pluto is the farthest planet in solar system"
print (planet1)

#Note we can index the String element
print(planet1[0])
print(planet1[1])
print(planet1[2])

#Reverse indexing
print(planet1[-1])
print(planet1[-2])
print(planet1[-3])

# Slicing a String , substring from a String
print(planet1[1:5])
print(planet1[:])
print(planet1[:5])
print(planet1[32:-7])

#Tuples
devops=('linux','vagrant','bash scripting','aws','jenkins','python')
print(devops[0])
print(devops[4:5])
print(devops[:-1])
print(devops[:])
#Revers a string
print(devops[::-1])
print(devops[0][::-1])
print(devops[2:3][0])
#fetching only scripting
print(devops[2:3][0][4:])
print(devops[2:3][0][4:][::-1])
print(devops[2:3][0][4:-3])
print(devops[2:3][0][4:-3][::-1])

#Same Slicing we can also perform on Lists

#Dicttionary
Skills = {"devops":('linux','vagrant','bash scripting','aws','jenkins','python'),"Development":['Java','Node JS','Flutter','go lang','CamelCase']}
print(Skills," \n",type(Skills))
print(Skills["devops"])
print(Skills["Development"])
print(Skills["devops"][-1])
print(Skills["devops"][::-1])
print(Skills["devops"][-1][2:])










