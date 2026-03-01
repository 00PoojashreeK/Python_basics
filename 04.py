#Concatenation
first_name = "Pooja"
last_name = "shree"
full_name = first_name + " " + last_name
print(full_name)

#Repetition
message = "warning! " * 10
print(message)

#or
message = "warning! "
print(message*10)

#String methods
message = "This is a warning!"
print(message.upper())
print(message.lower())
print(message.strip()*2)
print(message.replace("warning","error"))

#Multi line string
name = '''Pooja said "hello"
        xyz said "hi"
        '''
print(name)

#Length of a string
print(len(message))

#Accessing string character
a = "poojashree"
print(a[4]) # index = position - 1

#String slicing
print(a[2:7])
print(a[:7])
print(a[2:])

#Accessing elements in reverse order
print(a[-5])
print(a[-10])

print(a[0:10:2])

#Escape sequence
s="pooja \n is a good girl"
print(s)

s="pooja \t is a good girl"
print(s)

# Write a Python program that asks the user for their name and age, then prints a personalized greeting message. Use both the + operator and f-strings for output.
name = input("Enter your name : ")
age = int(input("Enter your age : "))
print("Hello" + " "  + name + " " + " ! you are" + " " + str(age) + " " +  "years old .")
print(f"Nice to meet you {name}. Next year you will be {age+1} years old !")

"""Write a Python program that:
Takes a sentence as input from the user.
Prints the sentence in all uppercase and lowercase.
Replaces all spaces with underscores.
Removes leading and trailing whitespace.
"""
a = input("Type a sentence : " )
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace(" ","_"))

"""
Write a Python program that:
Asks the user for a string.
Prints how many characters are in the string, excluding spaces.
"""
b = input("Enter a string : ")
text_without_space = b.replace(" ","")
count = (len(text_without_space))
print("Number of character excluding spaces : ", count)

#Write a Python program that uses escape sequences to print the following output:
print("Hello\n\tWorld\nThis is a backslash: \\")