#Variable length arguments using *args - only for tuples
def add(*a):
    print(type(a))
add(1,2,3,4,5)

def add(*numbers):
    return sum(numbers)
print(add(1,100,1))

def total_sum(*numbers):
    result = 0
    for num in numbers:
        result += num
    return result
print(total_sum(1, 2, 3, 4, 5))

#Using **kwargs For key-value pairs
def student_info(**details):
    print(type(details))
    for key, value in details.items():
        print(f"{key}: {value}")
student_info(name="Alice", age=20, course="Python")

#Lambda function or anonymous function
def add(x, y):
    return x + y
add = lambda x, y: x + y
print(add(5, 10))
double = lambda p: p * 2
print(double(4))

students = [
    {"name": "Alice", "marks": 20},
    {"name": "Bob", "marks": 22},
    {"name": "Charlie", "marks": 19}
]
students.sort(key = lambda x: x["marks"], reverse = True)
print(students)

#Recursion
def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(3))

def factorial(n):
    if n==1:
        return 1
    else:
        return n + factorial(n-1)
print(factorial(8))

#Nested function
def outer_function(name):
    def inner_function():
        print(f"Hello, {name}!")
    inner_function()
outer_function("ABC")

def calculate(a,b):
    def add():
        print(a + b)
    def subtract():
        print(a - b)
    def multiply():
        print(a * b)
    add()
    subtract()
    multiply()
calculate(5, 3)