

msg = "apple everyday keeps Doctors away"
print(msg)
print(msg.capitalize())
Message = msg.upper()
print(Message)

#dir() function
print(dir(Message))
print(dir([]))
print(dir(()))
print(dir({}))

print(Message.islower())
print(Message.isupper())
print(Message.find("DOCTOR"))
print(Message[22:28])
print(Message[::-1])

seq = ("192","168","56","12")
print(".".join(seq))
print("/".join(seq))
print("-".join(seq))

mountains = ["Everest","Himalaya","Sahyadri","Alp","K2","Mt Hood"]
print(mountains)
#adding item to list
mountains.append("Oregon Mount")
print(mountains)
# adding list to list
mountains.extend(["Mt Rainer","Satpuda"])
print(mountains)
#insert item at particular place
mountains.insert(2,"Mt Abu")
print(mountains)
#Remove item
mountains.pop()
print(mountains)
#Remove item from defined place
mountains.pop(3)
print(mountains)

details = {"Name":"Alice","Age":30,"Address":"LA","Skills":["devops","development"],"Number":8765234}
print(details.keys())
print(details.values())
# to clear a dictionary details.clear()







