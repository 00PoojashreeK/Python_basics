#Tuples
genders = ("male", "female", "others")
print(genders)
print(type(genders))
print(len(genders))
print(genders[1])
print(genders[1:3])

#From tuple to a list
a = ('2',)
b = 'b'
l = list(a)
l.append(b)
print(tuple(l))

#To add longer list of items to append
a = ('2',)
items = ['o', 'k', 'l', 'p']
l = list(a)
for x in items:
    l.append(x)
print(tuple(l))

#Concatenation
tuple1 = (1, 3, 4)
tuple2 = (4, 5, 6)
combined_tuples = tuple1 + tuple2 
print(combined_tuples)

#Tuple repetition
repeated_tuple = (1,2 ) * 10
print(repeated_tuple)

#Checking membership
print("4" in tuple1)
 
#Tuple methods
print(genders.index("male")) # Indexing
print(combined_tuples.count(4)) # counting

#tuple inside the tuple
genders = ("male", "female", "others", (1, 2, 3))
print(genders)

#Sets
s = {1, 2, 3}
print(s)
print(type(s))
s1 = {20, 123, 2}
print(s1) # set is unordered
s2 = set((10, 20, 30, 40))
print(s2)
print(type(s2))

#Empty set
s = set()
print(s)
print(type(s))

#Set operations
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1 | s2) #union
print(s1 & s2) #intersection
print(s1 - s2) #difference

#sets method
s3 = {8, 9, 10}
s3.add(11)
s3.remove(8)
s3.discard(12)
s3.pop()
s3.clear()
print(s3)
