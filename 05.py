#None data type
x = None
print(type(x))

#Assignment operator
x = 5
x += 3
y = 6 
y -= 3
z = 8
z *= 10
a = 2
a /=7
print(x,y,z,a)

#Comparison operators
b = 10
c = 20
print(b == c)
print(b != c)
print(b >= c)
print(b <= c)

#Logical operators
print(True and False)
print(False or True)
print(False or False)
print(not(True))
print(not(False))
print(1>2 or 2>1)
print(1<2 and 1>2)
print(not(1>2))

#Membership operator
my_list = [1,2,3,4,5]
my_string = "Python"
print(3 in my_list)
print(6 not in my_list)
print("P" in my_string)
print("z" not in my_string)
s = "pooja"
s2 = "poojashree"
print("c" in s)
print("p" not in s2)
print(("p" in s) and ("p" in s2))
print(("s" in s) or ("s" in s2))

#Bitwise operator
p = 5
q = 3
print(p & q)
print(p | q)
print(p ^ q)
print(~p)
print(p << 1)
print(p >> 1)