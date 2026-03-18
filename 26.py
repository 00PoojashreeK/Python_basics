"""
Lambda Function: Write a lambda function that multiplies two numbers.
"""
multiply = lambda x, y: x * y
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("Multiplication:", multiply(x, y))

"""
Recursive Function: 
Write a recursive function that calculates the sum of the first n numbers.
"""
def sum_n(n):
    if n==0:
        return 0
    else:
        return n + sum_n(n-1)
    num = int(input("Enter a number: "))
    print("Sum = ", sum_n(num))

"""
Variable-Length Arguments: 
Write a function that accepts any number of arguments and returns their average.
"""
def find_average(*numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count
nums = list(map(int, input("Enter numbers separated by space: ").split()))
print("Average =", find_average(*nums))