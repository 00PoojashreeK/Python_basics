"""
List Manipulation:
Create a list of Kannada foods. 
Use list comprehension to create a new list where each food name is in uppercase.
"""
foods = ["Pulav", "Dose", "idli", "Bisibele bath", "Paneer"]
upper_foods = [food.upper() for food in foods]
print("Original list :" , foods)
print("Uppercase list : ", upper_foods)


"""
Sum of Prices:
Create a dictionary of 5 items with their prices. 
Write a program that calculates the total price of all items using a for loop.
"""
items = {
    "Rice" : 89,
    "Ragi" : 78,
    "Jowar" : 67,
    "Sugar" : 56,
    "Salt" : 10
}
total = 0
for price in items.values():
    total = total + price
print("Total price of all items : ", total)


"""
List of Squares:
Create a list of numbers from 1 to 10. Use list comprehension to generate a list of their squares.
"""
numbers = list(range(1,11))
squares = [num**2 for num in numbers]
print("Numbers : ", numbers)
print("Squares : ", squares)


"""
Student Data Task:
Create a list of 3 dictionaries, where each dictionary contains the name, age, and marks of a student. 
Loop through the list and print each student's information.
"""
students = [
    {"Name" : "Pooja", "age" : 19, "marks" : 89},
    {"Name" : "Neha", "age" : 23, "marks" : 78},
    {"Name" : "Raksha", "age" : 21, "marks" : 90}
]
for student in students :
    print("Name : ", student["Name"])
    print("Age : ", student["age"])
    print("Marks : ", student["marks"])
    print()


"""
Dictionary Comprehension:
Create a dictionary where the keys are Kannada cities, and the values are their populations. 
Use dictionary comprehension to filter out cities with populations below 10 lakhs.
"""
cities = {
    "Bengaluru" : {"population" : 130},
    "Hubbali" : {"population" : 119},
    "Mysuru" : {"population" : 9},
    "Mandya" : {"population" : 8},
    "Gadag" : {"population" : 110}
}
filtered_cities = {city: data for city, data in cities.items() if data["population"] >= 10}
print("Cities with population above 10 lakhs:")
print(filtered_cities)


"""
Nested List Challenge: Write a Python program that takes a list of lists (a 2D list) as input and:
Prints the entire matrix row by row.
Prints the sum of each row in the matrix.
Example:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
"""
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print("Matrix row by row:")
for row in matrix:
    print(row)
print("\n Sum of each row :")
for row in matrix:
    total = sum(row)
    print(total)