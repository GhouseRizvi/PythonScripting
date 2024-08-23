# Exploring Data types in Python
#Numbers
num1=3452
flt1=35.23

#List / Collection of multi datatype, enclosed in square brackets.
str1="alpha"
first_list=[str1, "devops",47,num1,flt1]
#printing list
print(first_list)

#tuple / Collection of multi datatypes, enclosed in round bracket
#Tuple will be immutable we can override but cannot edit the content.
first_tuple=(str1, "devops",47,num1,flt1)
#printing tuple
print(first_tuple)

#Dictionary it is a collection of key value pairs{key:value}
first_dictionary={"Name":"Alex", "Age":"30", "weight":"80","fruits":["Banana","Mango","Orange","Apple","Banana"],}
print(first_dictionary)
print("Variable List Type is :",type(first_list))
print("Variable Tuple Type is :",type(first_tuple))
print("Variable Dictionary Type is :",type(first_dictionary))

#Boolean
x=True
y=False
print(x)
print(y)
print(type(x))
