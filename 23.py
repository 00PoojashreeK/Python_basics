#FUNCTIONS

def greet():
    print("Hello Good Morning!")
greet()
greet()
greet()
greet()

def marriage(boy , girl="Girl"):  #parameters
    print(f"Boy is {boy}")
    print(f"Girl is {girl}")
    print(f"{boy} married {girl}")
marriage("chandan", "chandana") #positional arguments
marriage(boy="Narendra", girl="chandana") #keyword arguments
marriage("Chandan") #default parameters


""" for i in range(1,11):
    print(f"2X{i} = {2*i}")
    print(f"3X{i} = {3*i}")
"""
def tables(num):
    for i in range(1,11):
        print(f"{num}X{i} = {num*i}")
tables(5)
tables(15)

#Returning a value from a function
def func(num):
    return int(str(num)*5)
a = 100
b = func(20)
c = a + b
print(c)

#Local and global variable
def func():
    x = "chandan" #local variable
    print("hello world!")
    print(y)
y = "darshan" #global variable
print(y)

#Basic function to greet user
def greet():
    print("Hello! Welcome to python course.")
greet()

#Function with parametrs
def greet_user(name):
    print(f"Hello ,{name}! Welcome to python course.")
greet_user("Pooja")

#Returning values from a function
def add_numbers(a , b):
    return a + b
result = add_numbers(5, 10)
print(result)

#Default parameter values
def greet(name="Student"):
    print(f"Hello, {name}! Welcome to the python course.")
greet()
greet("Geetha")

#LOcal and global variables.
name = "Global name"
def greet():
    name = "Local Name"
    print(name)
greet()# prints local name
print(name) # prints global name

