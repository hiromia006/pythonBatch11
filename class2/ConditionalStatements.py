# if, if else, if else if, else
# Comparison & logical Operators
from class1.DataType import amount

# Simple if
print("Example of Simple If")
temperature = 15
if temperature > 25:
    print('It is a hot day')

print("Example of  If and else")
age = 10
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor.")

print("Example of  If elif and else")
mark = -70
if mark <= 100 and mark >= 80:
    print("Grad is A+")
elif mark <= 79 and mark >= 60:
    print("Grad is A")
elif mark <= 40 and mark >= 59:
    print("Grad is B")
else:
    print("D")

# nested if
print("Example of nested if")
age = 20
has_ticket = True
amount = 80
if age >= 18:
    print("You are an adult.")
    if has_ticket and amount >= 100:
        print("You may enter the event.")
    else:
        print("You need a ticket and amount greater than 100 to enter.")
else:
    print("Sorry, you must be at least 18 age and amount greater than 100 to enter.")
