"""
Greet Function: 
Write a function greet() that takes no arguments and prints a greeting message
."""
def greet():
    print("Welcome to the Python course!")
greet()

"""
Parameterized Greet:
 Write a function greet_user() that takes a name as input and prints a custom greeting.
 """
def greet_user(name):
    print(f"Hello, {name}! Welcome to the Python course.")
greet_user("Alice")

"""
Sum Function:
 Write a function add_numbers(a, b) that returns the sum of two numbers. 
 Call this function with different values.
"""
def add_numbers(a, b):
    return a + b
print (add_numbers(5, 10))
print (add_numbers(3, 7))
print (add_numbers(-2, 8))

def add_numbers(a, b):
    return a + b
result1 = add_numbers(5, 10)
result2 = add_numbers(3, 7)
result3 = add_numbers(-2, 8)
print(result1)
print(result2)
print(result3)
