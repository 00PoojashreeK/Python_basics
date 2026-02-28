#variables

a = 10
b = 20
name = "pooja"
is_switch_on = True
print(a)
print("a")
print(a+b)

# Assigning values to multiple variable

a, b, c = 10, 20, 30
print(a,b,c)

#data type

name="pooja" #string
age=19 #integer
is_student=True #boolean
weight=41.75 #float
print(type(weight))
print(type(age))
print(type(is_student))
print(type(name))

is_student="yes"
print(type(is_student))

#type conversion

age_float = float(age)
print(float(age))

s = "100"
print(int(s)+age)

#Arithmetic operator

a = 10
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)

print(a+b-a**b-a+a//b+a)

#variable reassignment

x = 5
print(x)
x = 10
print(x)

#swapping of two variables with temp

a = 10
b = 20
print("before swapping:")
print("a=", a)
print("b=", b)
temp = a
a = b
b = temp
print("after swapping:")
print("a=", a)
print("b=", b)

#swapping of two varibles without temp

a = 20
b = 10
print("before swapping:")
print("a=", a)
print("b=", b)
a = a+b
b = a-b
a = a-b
print("after swapping:")
print("a=", a)
print("b=", b)