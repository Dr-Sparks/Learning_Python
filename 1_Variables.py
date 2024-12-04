# Variables = reusable container for a value (string, integer, float, boolean)
#             Its behaves as the value it contains

# Strings
first_Name = "Mark"
food = "Tiramisu"
email = "ahdfkh@gmail.com"

print(first_Name)
print(f"first_Name is {first_Name}") #f-string 

# Integers
age = 24
quantity = 3

print(f"You are {age} years old") #f-string 

# Float
price = 10.99
gpa = 3.2

print(f"The price is £{price}")

# Boolean 
is_student = True
for_sale = False

if is_student:
    print("You are a student")
else:
    print("You are not a student")

print(f"Are you a Student?: {is_student}")
