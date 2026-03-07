# Print even numbers from 1 to 50
i = 0
while i <=50:
    print(i)
    i = i + 2

#Print odd numbers from 1 to 30
i = 1
while i<= 30:
    print(i)
    i = i + 2

#Sum of first 10 natural numbers
i = 1
sum = 0
while i<=10:
    sum = sum + i
    i = i + 1
print("Sum = ", sum)

#Reversing a number
i = 20
while i>=1:
    print(i)
    i = i - 1

#Sum of digits of number
num = int(input("Enter a number : "))
sum = 0
while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10
print("Sum of digits : ", sum)

#Reverse a number
num = int(input("Enter a number :"))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
print("Reverse of the number is : ", rev )

#Factorial of a number
n = int(input("Enter a number : "))
fact = 1
i = 1
while i <= n:
    fact = fact * i
    i += 1
print("Factorial of a number is : ", fact)

#Count number until user enters zero
count = 0
num = int(input("Enter the number (0 to stop) : "))
while num != 0:
    count += 1
    num = int(input("Enter the number (0 to stop) :"))
print("Total numbers entered : ", count)

#Countdown timer
i = 10
while i >= 1:
    print(i)
    i -= 1
print("Happy New Year!!")

#Password checker
password = "python123"
user = input("Enter a password : ")
while user != password:
    print("Wrong password! Try again.")
    user = input("Enter password : ")
print("Access granted.")