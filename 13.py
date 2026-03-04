"""
Basic Conditions:
Write a program to check if someone is eligible for a bus pass. 
If they are below 5 years, the bus pass is free. 
If they are 60 years or older, they get a senior citizen discount. 
Otherwise, they pay the full price.
"""
age = int(input("Enter your age: "))
if age < 5:
    print("Bus pass is free.")
elif age >= 60:
    print("You get a senior citizen discount.")
else:
    print("You have to pay the full price.")


"""
Meal Time Checker:
Create a program that checks the time of day (24-hour format) and prints whether it's time for breakfast, lunch, or dinner.
Breakfast: 8 AM
Lunch: 1 PM
Dinner: 8 PM
If none of these times, print "It's not meal time."
"""
time = int(input("Enter the time in 24-hour format (only hour): "))
if time == 8:
    print("It's time for Breakfast.")
elif time == 13:
    print("It's time for Lunch.")
elif time == 20:
    print("It's time for Dinner.")
else:
    print("It's not meal time.")


"""
Simple Eligibility Check:
Write a program that checks whether a person is eligible for a library membership. 
If they are under 18, they get a student membership. 
If they are 60 or older, they get a senior citizen membership. 
Otherwise, they get a regular membership.
"""
age = int(input("Enter your age: "))
if age < 18:
    print("You get a Student Membership.")
elif age >= 60:
    print("You get a Senior Citizen Membership.")
else:
    print("You get a Regular Membership.")