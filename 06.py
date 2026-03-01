"""
Write a Python program that takes two numbers as input from the user and checks if:
Both numbers are greater than 10 (using and).
At least one of the numbers is less than 5 (using or).
The first number is not greater than the second (using not).
"""
a = int(input("Enter number a : "))
b = int(input("Enter number b : "))
if a>10 and b>10:
    print("Both numbers are greater than 10.")
else:
    print("Both numbers are not greater than 10.")

if a<5 or b<5:
    print("Anyone of the number is less than 5.")
else:
    print("None of the number is less than 5.")

if not(a>b):
    print("First number is not greater than second number.")
else:
    print("First number is greater than second number.")

"""
 Create a Python program that asks the user for their age and prints:
"You are an adult" if the age is greater than or equal to 18.
"You are a minor" if the age is less than 18.
Use >= and < comparison operators.
"""
age = int(input("Enter the age : "))
if age>=18 :
    print("You are an adult.")
elif age<18 :
    print("You are an minor.")