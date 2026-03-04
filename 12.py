#If condition.
x = 10
if x == 10:
    print("yes x is 10.")

#If-else condition.
y = 27
if y%2==0:
    print("y is even.")
else:
    print("y id odd.")

#If-elif-else condition.
signal = input("Enter the colour of the signal : ")
if signal == "red":
    print("STOP")
elif signal == "yellow":
    print("READY")
else:
    print("GO")

#Using comparison operators
age = int(input("Enter the age of a person : "))
if age >= 18:
    print("You are eligible to vote.")
else :
    print("You are not eligible to vote.")

#Using logical operators
att = 32
is_teacher_friend = True
if att >= 75 or is_teacher_friend:
    print("Exam")
else :
    print("NO Exam")

#Nested if else
gender = input("Enter you gender : ")
age = int(input("Enter your age : "))
if gender == "female":
    print("Ticket is free.")
else :
    if age < 5:
        print("Ticket is free.")
    elif age <= 12 :
        print("You get a child discount.")
    elif age >= 60 :
        print("You get a senior citizen discount.")
    else : 
        print("You pay the full price.")