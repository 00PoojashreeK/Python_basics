"""
Multiples of 3:
Write a for loop that prints all multiples of 3 between 1 and 30.
"""
for i in range(1,31):
    if i % 3 == 0:
        print(i)

"""
Sum of First 10 Numbers:
Write a program using a for loop that calculates the sum of numbers from 1 to 10.
"""
sum = 0
for i in range(1,11):
    sum = sum + i
print("Sum = ", sum)

"""
Print Your Name Letter by Letter:
Write a program that takes your name as input and prints each letter of your name using a for loop.
"""
name = input("Enter the name : ")
for letter in name:
    print(letter)

"""
Count Vowels in a String:
Write a program that counts how many vowels are in a given string using a for loop.
"""
text = input("Enter a string : ")
count = 0
for ch in text:
    if ch in "aeiouAEIOU" :
        count += 1
print("Number of vowels : ", count)