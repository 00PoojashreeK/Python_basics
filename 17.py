#FOR LOOP

#To print numbers from 1 to 10
for i in range(1,11):
    print(i, end="  ")

bag = ["red", "green", "blue", "pink"]
for ball in bag:
    print(ball)

for i in range(1,11,2):
    print(i)

for i in range(2,12,2):
    print(i)

#Looping over strings
name = "pooja"
for letter in name:
    print(letter) # To print letters
    print(letter*2) # to print a letter 2 times

#Enumerate
name = "karnataka"
(1,2)
for index, letter in enumerate(name):
    print(letter*index) 

l = [12, 1323, 14, 122]
for index, num in enumerate(l):
    print(f"{num} is in {index}th index") # To print along with mentioning index

#Using break in for loop
countries = ["India", "England", "Australia", "Japan"]
for country in countries:
    if country == "India":
        print(f"Found {country}!")
        break
    print(country)

#Using continue in for loop
countries = ["India", "England", "Australia", "Japan"]
for country in countries:
    if country == "India":
        continue
    print(country)

#Using else in for loop
a = [12, 1232, 14, 122]
for num in a:
    print(num)
else:
    print("All printed")

#Iteration using dictionary
d = {"name" : "Pooja", "age" : 19, "income" : 1}
for key, value in d.items(): # to convert into tuples
    print(key, "  ", value)

#Nested loops
#To print multiplication table
for i in range(2,11):
    for j in range(1,11):
        print(f"{i}X{j}={i*j}")
        