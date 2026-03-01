"""
Write a Python program that:
Takes a string as input from the user.
Checks if the letter 'a' is in the string (using in).
Checks if the string doesn't contain the word "Python" (using not in).
"""
s = input("Enter a string : ")
if "a" in s :
    print("a is in the string.")
else :
    print("a is not in the string.")

if "python" not in s:
    print("Python is not present in s.")
else:
    print("Python is present in s.")

"""
Given two integers, write a Python program that:
Prints the result of a & b, a | b, and a ^ b.
Shifts the bits of a two positions to the left (a << 2).
Shifts the bits of b one position to the right (b >> 1).
"""
a = int(input("Enter the first integer a : "))
b = int(input("Enter the second integer b : "))
print("a & b =", a & b)
print("a | b =", a | b)
print("a ^ b =", a ^ b)
print("a << 2 =", a << 2)
print("b >> 2 =", b >> 2)