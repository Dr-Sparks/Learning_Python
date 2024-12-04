# Typecasting = the process of converting a variable from one data type to another 
#               str(), int(), float(), bool()

name = "Mark"
age = 25
gpa = 3.2
is_student = True

print(type(age)) # int
print(type(is_student)) # bool

gpa = int(gpa)

age = str(age)

age += "1" # from 25 to 251

print(gpa)
print(age)

